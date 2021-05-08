# On both the NXOS1 and NXOS2 switches configure five VLANs including VLAN names (just pick 5 VLAN numbers between 100 - 999). 
# Use Netmiko's send_config_from_file() method to accomplish this. 
# Also use Netmiko's save_config() method to save the changes to the startup-config.

import os
from netmiko import ConnectHandler
from getpass import getpass
from datetime import datetime

def display_output(output):
    print()
    print("#" * 80)
    print("CFG Change: ")
    print(output)
    print("#" * 80)
    print()

password = os.getenv("PYNET_PASSWORD") if os.getenv("PYNET_PASSWORD") else getpass()

nxos1 = {
    "host": "nxos1.lasthop.io",
    "username": "pyclass",
    "password": getpass(),
    "device_type": "cisco_nxos",
}

nxos2 = {
    "host": "nxos2.lasthop.io",
    "username": "pyclass",
    "password": getpass(),
    "device_type": "cisco_nxos",
}

for device in (nxos1, nxos2):
    net_connect = ConnectHandler(**device)
    print(net_connect.find_prompt())

    output = net_connect.send_config_from_file(config_file='vlans.txt')
    display_output(output)

    save_out = net_connect.save_config()
    print(save_out)

    net_connect.disconnect()