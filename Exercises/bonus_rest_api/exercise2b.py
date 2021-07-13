# Repeat exercise 2a, except properly construct the HTTP request headers as follows:
# http_headers = {}
# http_headers["accept"] = "application/json; version=2.4;"

# You will need to pass these HTTP headers into your HTTP GET request. Once again print the HTTP status code, the response text, the JSON response, and the HTTP response headers. 


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

    # Get top level endpoints
    resp = requests.get(BASE_URL, headers=http_headers, verify=False)

    print()
    print(f"Response Code: {resp.status_code}")

    print()
    print("Response Text:")
    pprint(resp.text)

    print()
    print("Response JSON:")
    pprint(resp.json())

    print()
    print("Response Headers:")
    pprint(dict(resp.headers))
    print()


if __name__ == "__main__":
    main()
