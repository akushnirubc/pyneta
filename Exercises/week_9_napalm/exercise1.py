# Create a simple function that accepts the NAPALM device information from the my_devices.py file and creates a NAPALM connection object. 
# This function should open the NAPALM connection to the device and should return the NAPALM connection object.

#!/usr/bin/env python
from getpass import getpass
from pprint import pprint
from napalm import get_network_driver
from my_devices import network_devices


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

if __name__ == "__main__":
    connections = []
    for device in network_devices:
        conn = open_napalm_connection(device)
        connections.append(conn)

# Using your "my_devices.py" file and your NAPALM connection function, create a list of NAPALM connection objects to 'cisco3' and 'arista1'.


# Iterate through the connection objects, print out the device's connection object itself. 
# Additionally, pretty print the facts for each device and also print out the device's NAPALM platform type (ios, eos, et cetera).

    print("\n\n")
    print("Print facts for all devices in connections list")
    print("-" * 20)
    for conn in connections:
        print()
        print("-" * 6)
        print(conn)
        pprint("{} facts:".format(conn.platform))
        pprint(conn.get_facts())
        print("-" * 6)
        # close the NAPALM connection
        conn.close()
    print("\n\n")
