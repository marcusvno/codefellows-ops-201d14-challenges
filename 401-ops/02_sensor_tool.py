'''
This is an Uptime Sensor Tool using ICMP packet pings and Python to determine if hosts on a LAN are up or down. 

REQUIREMENTS:
  - Transmit a single ICMP (ping) packet to a specific IP every two seconds.
  - Evaluate the response as either success or failure.
  - Assign success or failure to a status variable.
  - For every ICMP transmission attempted, print the status variable along with a comprehensive timestamp and destination IP tested.
  
  Example output: 
    2020-10-05 17:57:57.510261 Network Active to 8.8.8.8
'''


def user_ping():
    user_input = input("Enter ping to test: ")
    return user_input

def test_ping(address):
  


if __name__ == "__main__":
    ping_address = user_ping()
    test_ping(ping_address)