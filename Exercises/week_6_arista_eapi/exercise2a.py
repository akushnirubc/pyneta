# Define an Arista device in an external YAML file (use arista4.lasthop.io for the device). 
# In your YAML file, make sure the key names exactly match the names required for use with pyeapi and the connect() method. In other words, 
# you should be able to execute 'connect(**device_dict)' where device_dict was retrieved from your YAML file. Do not store the lab password 
# in this YAML file, instead set the password using getpass() in your Python program. 
# Using this Arista device information stored in a YAML file, repeat the 'show ip arp' retrieval using pyeapi. 
# Once again, from this ARP table data, print out a mapping of all of the IP addresses and their corresponding MAC addresses.

import pyeapi
from getpass import getpass
import yaml

filename="arista_devices.yml"

with open(filename, "r") as f:    
    yaml_out = yaml.load(f)

devices = yaml_out

for name, device_dict in devices.items():
    device_dict["password"] = getpass()
    connection = pyeapi.client.connect(**device_dict)
    device = pyeapi.client.Node(connection)
    output = device.enable( "show ip arp")

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


