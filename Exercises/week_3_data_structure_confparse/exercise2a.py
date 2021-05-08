# Create a list where each of the list elements is a dictionary representing one of the network devices in the lab. Do this for at least four of the lab devices. 
# The dictionary should have keys corresponding to the device_name, host (i.e. FQDN), username, and password. 
# Use a fictional username/password to avoid checking the lab password into GitHub.

import yaml
from pprint import pprint


cisco3 = {"device_name": "cisco3", "host": "cisco3.lasthop.io" }

cisco4 = {"device_name": "cisco4", "host": "cisco4.lasthop.io" }

arista1 = {"device_name": "arista1", "host": "arista1.lasthop.io"}

arista2 = {"device_name": "arista2", "host": "arista2.lasthop.io"}


my_devices = [cisco3, cisco4, arista1, arista2]

for devices in my_devices:
    # print(devices["host"])
    devices["username"] = "admin"
    devices["password"] = "cisco123"

print()
pprint(my_devices)
print()