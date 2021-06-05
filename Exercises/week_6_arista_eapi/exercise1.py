# Using the pyeapi library, connect to arista3.lasthop.io and execute 'show ip arp'. 
# From this ARP table data, print out a mapping of all of the IP addresses and their corresponding MAC addresses.

import pyeapi
from getpass import getpass
from pprint import pprint


connection = pyeapi.client.connect(
    transport="https",
    host="arista3.lasthop.io",
    username="pyclass",
    password=getpass(),
    port="443",
)

device = pyeapi.client.Node(connection)
output = device.enable( "show ip arp")
# pprint(output[0]['result']['ipV4Neighbors'])
print()
print("-" * 40)
arp_list = output[0]['result']['ipV4Neighbors']
for arp_entry in  arp_list:
    mac_address = arp_entry['hwAddress']
    ip_address = arp_entry['address']
    # print(ip_address)
    # print(mac_address)
    print("{:15}{:^5}{:^15}".format(ip_address, "-->", mac_address))
print("-" * 40)
print()