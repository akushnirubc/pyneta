# Create an nxapi_plumbing "Device" object for nxos1. 
# The api_format should be "jsonrpc" and the transport should be "https" (port 8443). 
# Use getpass() to capture the device's password. 
# Send the "show interface Ethernet1/1" command to the device, parse the output, and print out the following information:

# Interface: Ethernet1/1; State: up; MTU: 1500

from __future__ import unicode_literals, print_function
from getpass import getpass
from nxapi_plumbing import Device
from pprint import pprint

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

device = Device(
        api_format="jsonrpc",
        host="nxos1.lasthop.io",
        username="pyclass",
        password=getpass(),
        transport="https",
        port=8443,
        verify=False,
)

intf_output = device.show("show interface Ethernet1/1")
intf_output = intf_output["TABLE_interface"]["ROW_interface"]
pprint(intf_output)

print("\n\n")
print("Gather and print Ethernet1/1 data:")
print("-" * 20)
print("Interface: {interface}; State: {state}; Mtu: {eth_mtu}".format(**intf_output))
print("\n\n")