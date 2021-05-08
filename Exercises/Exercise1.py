import os
from netmiko import ConnectHandler
from getpass import getpass

# In the lab environment use Netmiko to connect to one of the Cisco NX-OS devices. You can find the IP addresses and username/passwords of the Cisco devices in the 'Lab Environment' email or 
# alternatively in the ~/.netmiko.yml file. 
# Simply print the router prompt back from this device to verify you are connecting to the device properly.

password = os.getenv("PYNET_PASSWORD") if os.getenv("PYNET_PASSWORD") else getpass()
nxos1 = {
    "host": "nxos1.lasthop.io",
    "username": "pyclass",
    "password": password,
    "device_type": "cisco_nxos"
}

net_connect = ConnectHandler(**nxos1)
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