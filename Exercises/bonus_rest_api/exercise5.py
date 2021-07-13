# Building on the script from exercise 4, 
# add a description to the the IP address object that you just created. 
# Accomplish this using an HTTP PUT. 
# The HTTP PUT operation will require all of the mandatory fields in the object (in this case, the "address" field). 
# Print the status code and the response.json() from your PUT operation. 
# The HTTP PUT operation will use same URL as exercise 4b (i.e. the URL of the newly created IP address object including its ID).

import os
import json
import requests
from pprint import pprint

from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)


# Constants, including ID from prev created object
BASE_URL = "https://netbox.lasthop.io/api/"
ADDRESS_ID = "364"
# ADDRESS_ID = input("Enter Address ID that was created in exercise4: ")


def main():

    token = os.environ["NETBOX_TOKEN"]

    # HTTP PUT needs the "Content-Type" header instead of "accept"
    http_headers = {}
    http_headers["Content-Type"] = "application/json; version=2.4;"
    http_headers["accept"] = "application/json; version=2.4;"
    http_headers["Authorization"] = f"Token {token}"

    # Add a description field to our IP object
    data = {"address": "192.0.2.123/32", "description": "Rest-API Test1-2-3"}

    # PUT (see noptes in lesson about PATCH) to update IP with a description
    resp = requests.put(
        f"{BASE_URL}ipam/ip-addresses/{ADDRESS_ID}/",
        headers=http_headers,
        verify=False,
        data=json.dumps(data)
    )
    print()
    print(f"Response code: {resp.status_code}")
    print("Returned JSON:")
    print("-" * 12)
    pprint(resp.json())
    print()


if __name__ == "__main__":
    main()

