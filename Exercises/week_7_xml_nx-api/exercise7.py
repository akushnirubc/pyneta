# Create an nxapi_plumbing "Device" object for nxos1. The api_format should be "xml" and the transport should be "https" (port 8443). 
# Use getpass() to capture the device's password. Send the "show interface Ethernet1/1" command to the device, parse the output, 
# and print out the following information:
# Interface: Ethernet1/1; State: up; MTU: 1500

from __future__ import unicode_literals, print_function
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from lxml import etree
from nxapi_plumbing import Device
from getpass import getpass
from pprint import pprint

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

device = Device(
    api_format="xml",
    host="nxos1.lasthop.io",
    username="pyclass",
    password=getpass(),
    transport="https",
    port=8443,
    verify=False,
)

intf_output = device.show("show interface Ethernet1/1")
# intf_output = etree.tostring(intf_output).decode()
pprint(intf_output)

print("\n\n")
print("Gather and print Ethernet1/1 data")
print("-" * 20)
print(
    "Interface: {}; state: {}; MTU: {}".format(
        intf_output.find(".//interface").text,
        intf_output.find(".//state").text,
        intf_output.find(".//eth_mtu").text,
    )
)

# Run the following two show commands on the nxos1 device using a single method and passing in a list of commands:
#  "show system uptime" and "show system resources". Print the XML output from these two commands.

print("\n\n")
print("Capture and print XML output from multiple show commands")
print("-" * 20)
show_output = device.show_list(["show system uptime", "show system resources"])
for output in show_output:
    print(etree.tostring(output, encoding="unicode"))
    print("-" * 20)
print("\n\n")


# Using the nxapi_plumbing config_list() method, 
# configure two loopbacks on nxos1 including interface descriptions. Pick random loopback interface numbers between 100 and 199.

print()
print("Create two new loopbacks with descriptions")
print("-" * 20)

cmds = [
    "interface loopback 106",
    "description test123",
    "no shutdown",
    "interface loopback 107",
    "description test 456",
    "no shutdown",
]

output = device.config_list(cmds)
print(etree.tostring(output[0]).decode())

# Look at the output XML for each configuration command
for msg in output:
    print(etree.tostring(msg, encoding="unicode"))