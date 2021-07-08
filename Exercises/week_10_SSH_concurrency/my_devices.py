# As you have done in previous classes, create a Python file named "my_devices.py". 
# In this file, define the connection information for: 'cisco3', 'arista1', 'arista2', and 'srx2'. T
# his file should contain all the necessary information to create a Netmiko connection. Use getpass() for the password handling. 
# Use a global_delay_factor of 4 for both the arista1 device and the arista2 device. 
# This Python module should be used to store the connection information for all of the exercises in this lesson.

import os
from getpass import getpass

username = "pyclass"
password = os.getenv("PYNET_PASSWORD") if os.getenv("PYNET_PASSWORD") else getpass()

cisco3 = {
    "host": "cisco3.lasthop.io",
    "username": username,
    "password": password,
    "device_type": "cisco_ios",
}

arista1 = {
    "host": "arista1.lasthop.io",
    "username": username,
    "password": password,
    "device_type": "arista_eos",
    "global_delay_factor": 4,
}

arista2 = {
    "host": "arista2.lasthop.io",
    "username": username,
    "password": password,
    "device_type": "arista_eos",
    "global_delay_factor": 4,
}

srx2 = {
    "host": "srx2.lasthop.io",
    "username": username,
    "password": password,
    "device_type": "juniper_junos",
}

network_devices = [cisco3, arista1, arista2, srx2]