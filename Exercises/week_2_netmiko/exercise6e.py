# Using SSH and netmiko connect to the Cisco4 router. In your device definition, specify both an 'secret' and a 'session_log'. Your device definition should look as follows: 

# password = getpass()
# device = {
#     "host": "cisco4.lasthop.io",
#     "username": "pyclass",
#     "password": password,
#     "secret": password,
#     "device_type": "cisco_ios",
#     "session_log": "my_output.txt",
# }
# Execute the following sequence of events using Netmiko:
#  time.sleep for two seconds and then use the read_channel() method to read the data that is currently available on the SSH channel. Print this to the screen.

from netmiko import ConnectHandler
from getpass import getpass
import time


password = getpass()
device = {
    "host": "cisco4.lasthop.io",
    "username": "pyclass",
    "password": password,
    "secret": password,
    "device_type": "cisco_ios",
    "session_log": "my_output.txt",
}

net_connect = ConnectHandler(**device)
print("\nExit priviledged exec (disable), Current prompt")
net_connect.write_channel("disable\n")
time.sleep(2)
print ("\n>>>>>>>")
output = net_connect.read_channel()
print(output)

net_connect.disconnect()