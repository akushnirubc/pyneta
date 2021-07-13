# Retrieve a list of all the devices in NetBox. This will require authentication. 
# As in the previous task, create your headers manually and pass them into your request. In order to perform the NetBox authentication, you should do the following:

# import os
# # Set the token based on the NETBOX_TOKEN environment variable
# token = os.environ["NETBOX_TOKEN"]

# Then add the following key to your HTTP Headers:

# http_headers["Authorization"] = f"Token {token}"

# From this returned data structure (the NetBox "/api/dcim/devices/"), print out all of the device "display_names". 
# Note, the response.json() will contain a "results" key. This "results" key will refer to a list of dictionaries. 
# These dictionaries will contain information about each one of the devices in NetBox.
from pprint import pprint
import requests

from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
import os
token = os.environ["NETBOX_TOKEN"]

# Constants
BASE_URL = "https://netbox.lasthop.io/api/"

def main():

    print()
    http_headers = {}
    http_headers["accept"] = "application/json; version=2.4;"
    if token:
        http_headers["authorization"] = "Token {}".format(token)

    # Retrieve /api/dcim/devices
    resp = requests.get(f"{BASE_URL}dcim/devices", headers=http_headers, verify=False)

    #Get the JSON results key from out query
    results = resp.json()["results"]
    print()

    #Create a list of all of our devices with their friendly "display_name"
    devices = []
    for dev in results:
            devices.append(dev["display_name"])

    # Or if you prefer list-comprehensions
    # devices = [dev["display_name"] for dev in results]

    print()
    print(devices)
    print

if __name__ == "__main__":
    main()
