# Create a Python module named jnpr_devices.py. This Python module should contain a dictionary named "srx2". 
# This "srx2" dictionary should contain all of the key-value pairs needed to establish a PyEZ connection.
#  You should use getpass() for the password handling. 
# You should import this "srx2" device definition for all of the remaining exercises in class8

import os
from getpass import getpass

username = "pyclass"
password = os.getenv("PYNET_PASSWORD") if os.getenv("PYNET_PASSWORD") else getpass()

# Dictionary to define each SRX device
srx2 = {"host": "srx2.lasthop.io", "user": username, "password": password}

# List of all SRX devices
junos_devices = [srx2]