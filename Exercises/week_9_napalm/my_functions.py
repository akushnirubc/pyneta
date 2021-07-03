# Create a new file named "my_functions.py" that will store a set of reusable functions. 
# Move the "open_napalm_connection" function from exercise1 into this Python file. Import the network devices once again from my_devices.py 
# and create a list of connection objects (once again with connections to both cisco3 and arista1).


#!/usr/bin/env python
from napalm import get_network_driver


def open_napalm_connection(device):
    """Funtion to open napalm connection and return connection object"""
    # Copy dictionary to ensure original object is not modified
    device = device.copy()
    # Pop "platform" as this is an invalid kwarg to napalm
    platform = device.pop("platform")
    driver = get_network_driver(platform)
    conn = driver(**device)
    conn.open()
    return conn

def create_backup(conn):
    """Funtion use config getter and write running config to disk"""
    backup = conn.get_config()
    filename = f"{conn.hostname}-running.txt"
    with open(filename, "w") as f:
        f.write(backup["running"])


