import os
from netmiko import ConnectHandler
from getpass import getpass

# Add a second NX-OS device to your first exercise. Make sure you are using dictionaries to represent the two NX-OS devices. 
# Additionally, use a for-loop to accomplish the Netmiko connection creation. Once again print the prompt back from the devices that you connected to.


password = os.getenv("PYNET_PASSWORD") if os.getenv("PYNET_PASSWORD") else getpass()
nxos1 = {
    "host": "nxos1.lasthop.io",
    "username": "pyclass",
    "password": password,
    "device_type": "cisco_nxos",
}

nxos2 = {
    "host": "nxos2.lasthop.io",
    "username": "pyclass",
    "password": password,
    "device_type": "cisco_nxos",
}


for device in (nxos1, nxos2):
    net_connect = ConnectHandler(**device)
    print(net_connect.find_prompt())


# nxos1:
#   device_type: cisco_nxos
#   host: nxos1.lasthop.io
#   username: pyclass
#   password: 88newclass
#   port: 22

#   nxos2:
#   device_type: cisco_nxos
#   host: nxos2.lasthop.io
#   username: pyclass
#   password: 88newclass
#   port: 22

#   cisco3:
#   device_type: cisco_ios
#   host: cisco3.lasthop.io
#   username: pyclass
#   password: 88newclass