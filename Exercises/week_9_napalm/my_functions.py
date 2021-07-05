# Create a new file named "my_functions.py" that will store a set of reusable functions. 
# Move the "open_napalm_connection" function from exercise1 into this Python file. Import the network devices once again from my_devices.py 
# and create a list of connection objects (once again with connections to both cisco3 and arista1).

# Create another function in "my_functions.py". This function should be named "create_backup" and should accept a NAPALM connection object as an argument.
# Using the NAPALM get_config() method, the function should retrieve and write the current running configuration to a file. The filename should be unique for each device.
#  In other words, "cisco3" and "arista1" should each have a separate file that stores their running configuration. 
#  Note, get_config() returns a dictionary where the running-config is referenced using the "running" key.
#  Call this function as part of your main exercise2 and ensure that the configurations from both cisco3 and arista1 are backed up properly.

# Create a new function named 'create_checkpoint'. Add this function into your my_functions.py file. 
# This function should take one argument, the NAPALM connection object. 
# This function should use the NAPALM _get_checkpoint_file() method to retrieve a checkpoint from 
# the NX-OS device. 
# It should then write this checkpoint out to a file.


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

def create_checkpoint(conn):
    """Function use config getter or get checkpoint file and write to disk"""
    if 'nxos' in conn.platform:
        filename = f"{conn.hostname}-checkpoint.txt"
        backup = conn._get_checkpoint_file()
        with open(filename, "w") as f:
            f.write(backup)
    else:
        raise ValueEror("Checkpoint requires NX-OS")
