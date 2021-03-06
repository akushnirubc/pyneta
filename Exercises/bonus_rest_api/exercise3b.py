# Using the same device information retrieved in exercise 3a, 
# create and print a report to standard output. This report should contain the location, manufacturer, and status for each device.
#  Your output should look similar to the following:

# ------------------------------------------------------------
# arista1
# ----------
# Location: Fremont Data Center
# Vendor: Arista
# Status: Active
# ------------------------------------------------------------


# ------------------------------------------------------------
# arista2
# ----------
# Location: Fremont Data Center
# Vendor: Arista
# Status: Active
# ------------------------------------------------------------

# ...   # remaining devices

import os
import requests

from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)


# Constants
BASE_URL = "https://netbox.lasthop.io/api/"

def main():

    token = os.environ["NETBOX_TOKEN"]

    http_headers = {}
    http_headers["accept"] = "application/json; version=2.4;"
    http_headers["Authorization"] = f"Token {token}"

    # Retrieve all the devices
    resp = requests.get(f"{BASE_URL}dcim/devices/", headers=http_headers, verify=False)

    # Get the JSON results key from our query
    results = resp.json()["results"]

    # Create a report to standard output 
    for dev in results:
        print()
        print("-" * 60) 
        device_name = dev["display_name"]
        location = dev["site"]["name"]
        manufacturer =  dev["device_type"]["manufacturer"]["name"]
        status = dev["status"]["label"]
        print(device_name)
        print("-" * 10)
        print(f"Location: {location}")
        print(f"Vendor: {manufacturer}")
        print(f"Status {status}")
        print()


if __name__ == "__main__":
    main()