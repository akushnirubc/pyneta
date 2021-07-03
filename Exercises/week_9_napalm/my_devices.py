# Create a Python file named "my_devices.py" that defines the NAPALM connection information for both the 'cisco3' device and the 'arista1' device. 
# Use getpass() for the password handling. 
# This Python module should be used to store the device connection information for all of the exercises in this lesson.


#!/usr/bin/env python
from getpass import getpass
import os


# Device definitions
username = "pyclass"
password = os.getenv("PYNET_PASWORD") if os.getenv("PYNET_PASSWORD") else getpass()

cisco3 = {
    "hostname": "cisco3.lasthop.io",
    "username": username,
    "password": password,
    "platform": "ios",
}

arista1 = {
    "hostname": "arista1.lasthop.io",
    "username": username,
    "password": password,
    "platform": "eos",
}

nxos1 = {
    "hostname": "nxos1.lasthop.io",
    "username": username,
    "password": password,
    "platform": "nxos",
    "optional_args": {"port": 8443},

}

# List of devices (only cisco3 and arista1)
network_devices = [cisco3, arista1]