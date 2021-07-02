# Create a Python program that creates a PyEZ Device connection to "srx2" 
# (using the previously created Python module). 
# Using this PyEZ connection and the RouteTable and ArpTable views retrieve the routing table and the arp table for srx2.

# This program should have four separate functions:
# 1. check_connected() - Verify that your NETCONF connection is working. 
# You can use the .connected attribute to check the status of this connection.
# 2. gather_routes() - Return the routing table from the device.
# 3. gather_arp_table() - Return the ARP table from the device.
# 4. print_output() - A function that takes the Juniper PyEZ Device object, the routing table, 
# and the ARP table and then prints out the: hostname, NETCONF port, username, routing table, ARP table

from pprint import pprint
import sys

from jnpr.junos import Device
from jnpr.junos.op.routes import RouteTable
from jnpr.junos.op.arp import ArpTable

from jnpr_devices import srx2


def check_connected(device):
    print("\n\n")
    if device.connected:
        print(f"Device {device.hostname} is connected!")
    else:
        print(f"Device {device.hostname} failed to connect :(.")
        # If device is *not* connected; exit script
        sys.exit(1)

def gather_routes(device):
    # Create RouteTable view object
    routes = RouteTable(device)
    # Get all routes
    routes.get()
    return routes

def gather_arp_table(device):
    # Create ArpTable view object
    arp = ArpTable(device)
    # Get all arp information
    arp.get()
    return arp

def print_output(dev, routes, arp):
    print()
    print("Print out desired output from device, route, and arp information")
    print("-" * 20)
    device = {}
    device["hostname"] = dev.hostname
    device["connected_port"] = dev.port
    device["connected_user"] = dev.user
    device["route_table"] = routes.items()
    device["arp_table"] = arp.items()
    pprint(device)
    print()

if __name__ == "__main__":

    device = Device(**srx2)
    device.open()

    check_connected(device)
    routes = gather_routes(device)
    arp = gather_arp_table(device)

    print_output(device, routes, arp)

