#!/bin/bash/env python3

# Author:                       Marcus Nogueira
# Date of latest revision:      02/27/2024
#
# The below Python script shows one possible method to return the cookie from a site that supports cookies.

import requests
import os

# targetsite = input("Enter target site:") # Uncomment this to accept user input target site
# Comment this out if you're using the line above
targetsite = "http://www.whatarecookies.com/cookietest.asp"
response = requests.get(targetsite)
cookie = response.cookies


def bringforthcookiemonster():  # Because why not!
    print('''

              .---. .---.
             :     : o   :    me want cookie!
         _..-:   o :     :-.._    /
     .-''  '  `---' `---' "   ``-.
   .'   "   '  "  .    "  . '  "  `.
  :   '.---.,,.,...,.,.,.,..---.  ' ;
  `. " `.                     .' " .'
   `.  '`.                   .' ' .'
    `.    `-._           _.-' "  .'  .----.
      `. "    '"--...--"'  . ' .'  .'  o   `.

        ''')


bringforthcookiemonster()
print("Target site is " + targetsite)
print(cookie)

# Add here some code to make this script perform the following:


# - Send the cookie back to the site and receive a HTTP response
res = requests.get(targetsite, cookie)

# - Generate a .html file to capture the contents of the HTTP response

with open("temp/cookiemonster.html", 'w', encoding='utf-8') as file:
    file.write(res.text)

# - Open it with Firefox
os.system("firefox temp/cookiemonster.html")
