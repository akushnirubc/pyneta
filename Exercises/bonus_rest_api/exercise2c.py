# Execute another HTTP GET request to retrieve all of the endpoints under the "/api/dcim" parent. Pretty print out the response.json() from this output. 
# This should be a dictionary with the key being the next part of the URL after "/api/dcim" and the value being the full URL.
from pprint import pprint
import requests

from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)


# Constants
BASE_URL = "https://netbox.lasthop.io/api/"


def main():

    print()
    http_headers = {}
    http_headers["accept"] = "application/json; version=2.4;"

    # Retrieve /api/dcim/
    resp = requests.get(f"{BASE_URL}dcim/", headers=http_headers, verify=False)
    print("Child endpoints under DCIM:")
    pprint(resp.json())
    print()


if __name__ == "__main__":
    main()