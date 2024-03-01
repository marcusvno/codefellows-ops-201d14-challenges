
#!/usr/bin/env python3

# Author:      Abdou Rockikz
# Description: XSS Detection script for study and annotation.
# Date:        02/28/2024
# Modified by: Marcus Nogueira

# TODO: Install requests bs4 before executing this in Python3

# Import libraries

import requests
from pprint import pprint
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin

# Declare functions

# Function uses Beautiful Soup to parse the GET request from the target URL made using the requests library. After parsing the HTML response, the function then returns the forms found.
def get_all_forms(url):
    soup = bs(requests.get(url).content, "html.parser")
    return soup.find_all("form")

### This function gets passed an individual form info from scan_xss and pulls the relevant form attributes (and lowercases all text) and loops to find all input attributes from the forms before returning a dictionary.
def get_form_details(form):
    details = {}
    action = form.attrs.get("action").lower()
    method = form.attrs.get("method", "get").lower()
    inputs = []
    for input_tag in form.find_all("input"):
        input_type = input_tag.attrs.get("type", "text")
        input_name = input_tag.attrs.get("name")
        inputs.append({"type": input_type, "name": input_name})
    details["action"] = action
    details["method"] = method
    details["inputs"] = inputs
    return details

### Takes the target URL, scanned forms, and starts inputting a value parameter that was passed to this function (the JS snippet from the scan_xss function). Then it does a POST or GET request based on the method of the form and returns the response to be evaluated by the scan_xss function.
def submit_form(form_details, url, value):
    target_url = urljoin(url, form_details["action"])
    inputs = form_details["inputs"]
    data = {}
    for input in inputs:
        if input["type"] == "text" or input["type"] == "search":
            input["value"] = value
        input_name = input.get("name")
        input_value = input.get("value")
        if input_name and input_value:
            data[input_name] = input_value

    if form_details["method"] == "post":
        return requests.post(target_url, data=data)
    else:
        return requests.get(target_url, params=data)

# Calls and saves the return from get_all_forms function to a forms variable. Prints the number of forms found in the URL. It then uses a loop to test each form with a JS snippet that shouldn't work and examines the response to the POST requests and checks if the snippet appears in the website's code. If it does, it prints that XSS was discovered and which form it was that was vulnerable to XSS.
def scan_xss(url):
    forms = get_all_forms(url)
    print(f"[+] Detected {len(forms)} forms on {url}.")
    js_script = '<IMG """><SCRIPT>alert("Test")</SCRIPT>"\>'
    is_vulnerable = False
    for form in forms:
        form_details = get_form_details(form)
        content = submit_form(form_details, url, js_script).content.decode()
        if js_script in content:
            print(f"[+] XSS Detected on {url}")
            print(f"[*] Form details:")
            pprint(form_details)
            is_vulnerable = True
    return is_vulnerable

# Main


# Keeps the script from being run in other scripts as module. Determines the structure of the program. Runs an input for URL to test for XSS (Cross Site Scripting) vulnerabilities. Passes that URL variable to the scan_xss function and prints the results.
if __name__ == "__main__":
    url = input("Enter a URL to test for XSS:")
    print(scan_xss(url))

# TODO: When you have finished annotating this script with your own comments, copy it to Web Security Dojo
# TODO: Test this script against one XSS-positive target and one XSS-negative target
# TODO: Paste the outputs here as comments in this script, clearling indicating which is positive detection and negative detection
