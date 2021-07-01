# Create a PyEZ Device object from the jnpr.junos Device class. 
# This device object should connect to "srx2.lasthop.io". Use getpass() to enter the device's password. 
# Pretty print all of the device's facts. 
# Additionally, retrieve and print only the "hostname" fact.


import os
from getpass import getpass
from pprint import pprint
from jnpr.junos import Device


password = os.getenv("PYNET_PASSWORD") if os.getenv("PYNET_PASSWORD") else getpass()
# Create pyez Device object for srx2
my_dev = Device(host="srx2.lasthop.io", user="pyclass", password=password)

# Create NETCONF connection to device
my_dev.open()

print()
print("Print device facts")
print("-" * 20)
pprint(my_dev.facts)

print("\n\n")
print("Print hostname from device facts")
print("-" * 20)
pprint(my_dev.facts['hostname'])
print("and the version yeah")
pprint(my_dev.facts['version'])
print()