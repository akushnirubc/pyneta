import os
from netmiko import ConnectHandler
from getpass import getpass

# For one of the Cisco IOS devices, use Netmiko and the send_command() method to retrieve 'show version'. Save this output to a file in the current working directory.


password = os.getenv("PYNET_PASSWORD") if os.getenv("PYNET_PASSWORD") else getpass()

cisco3 = {
    "host": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": password,
    "device_type": "cisco_nxos",
}


net_connect = ConnectHandler(**cisco3)
output = net_connect.send_command("show version")


with open("show_version.txt", "w") as f:
    f.write(output)

net_connect.disconnect()