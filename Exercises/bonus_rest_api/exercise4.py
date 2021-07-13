# Using an HTTP POST and the Python-requests library, create a new IP address in NetBox. 
# This IP address object should be a /32 from the 192.0.2.0/24 documentation block. Print out the status code and the returned JSON.
# The HTTP headers for this request should look as follows:

# http_headers = {}
# http_headers["Content-Type"] = "application/json; version=2.4;"
# http_headers["accept"] = "application/json; version=2.4;"
# http_headers["Authorization"] = f"Token {token}"

# The URL for the HTTP POST is:

# https://netbox.lasthop.io/api/ipam/ip-addresses/

# The JSON payload data for this request should be similar to the following:
# data = {"address": "192.0.2.100/32"}


import os
import json
import requests
from pprint import pprint

from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)


# Constants
BASE_URL = "https://netbox.lasthop.io/api/"

def main():

    token = os.environ["NETBOX_TOKEN"]

    # HTTP post needs the "Content-Type" header instead of "accept"
    http_headers = {}
    http_headers["Content-Type"] = "application/json; version=2.4;"
    http_headers["accept"] = "application/json; version=2.4;"
    http_headers["Authorization"] = f"Token {token}"

    # Required IP address data
    data = {"address": "192.0.2.123/32"}

    # Post the data
    resp = requests.post(
        f"{BASE_URL}ipam/ip-addresses/",
        headers=http_headers,
        verify=False,
        data=json.dumps(data),
    )
    print()
    print("creating IP address object:")
    print(f"response code: {resp.status_code}")
    print("Returned JSON:")
    print("-" * 12)
    pprint(resp.json())

# Using the response data from the HTTP POST that created the IP address entry in exercise 4a, capture the "id" of the newly created IP address object. 
# Using this ID, construct a new URL. Use this new URL and the HTTP GET method to retrieve only the API information specific to this IP address. Your IP address URL should be of the following form:
# https://netbox.lasthop.io/api/ipam/ip-addresses/{address_id}/
# where {address_id} is the ID of the object that you just created.
# Pretty print the response.json() data from this HTTP GET. Please note the ID of the address object that you just created.

    # Retrieve the new object ID and query that specific object
    print()
    print("Query newly created object...")
    address_id = resp.json()["id"]

    # New URL specific to our new IP address object
    url = f"{BASE_URL}ipam/ip-addresses/{address_id}/"
    resp = requests.get(url, headers=http_headers, verify=False)
    print("-" * 12)
    pprint(resp.json())

    print()
    print(f"IP Addreses ID: {address_id}")
    print()


if __name__ == "__main__":
    main()