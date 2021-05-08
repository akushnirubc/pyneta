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
# Use the write_channel() method to send the 'disable' command down the SSH channel.
#  Note, write_channel is a low level method so it requires that you add a newline to the end of your 'disable' command.

from netmiko import ConnectHandler
from getpass import getpass


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
print ("\n>>>>>>>")
# print("Config mode check: {}".format(net_connect.exit_config_mode())
print("Current Prompt: {}".format(net_connect.find_prompt()))
print()

net_connect.disconnect()