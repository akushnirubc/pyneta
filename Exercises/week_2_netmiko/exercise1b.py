# 1. Use the extended 'ping' command and Netmiko on the 'cisco4' router. This should prompt you for additional information as follows:

# cisco4#ping
# Protocol [ip]: 
# Target IP address: 8.8.8.8
# Repeat count [5]: 
# Datagram size [100]: 
# Timeout in seconds [2]: 
# Extended commands [n]: 
# Sweep range of sizes [n]: 
# Type escape sequence to abort.
# Sending 5, 100-byte ICMP Echos to 8.8.8.8, timeout is 2 seconds:
# !!!!!
# Success rate is 100 percent (5/5), round-trip min/avg/max = 1/1/4 ms



# b. Use send_command() and the expect_string argument to handle the additional prompting. Once again specify a target IP address of '8.8.8.8'.

from netmiko import ConnectHandler
from getpass import getpass

device = {
    "host": 'cisco4.lasthop.io', 
    "username": 'pyclass', 
    "password": getpass(), 
    "device_type": 'cisco_ios', 
    "session_log": 'my_session.txt'
}

net_connect = ConnectHandler(**device)
print(net_connect.find_prompt())


output = net_connect.send_command(
    "ping", expect_string=r"Protocol", strip_command=False
)
output += net_connect.send_command(
    "\n", expect_string=r"Target IP", strip_prompt=False, strip_command=False
)
output += net_connect.send_command(
    "8.8.8.8", expect_string=r"Repeat count", strip_prompt=False, strip_command=False
)
output += net_connect.send_command(
    "\n", expect_string=r"Datagram size", strip_prompt=False, strip_command=False
)
output += net_connect.send_command(
    "\n", expect_string=r"Timeout in seconds", strip_prompt=False, strip_command=False
)
output += net_connect.send_command(
    "\n", expect_string=r"Extended commands", strip_prompt=False, strip_command=False
)
output += net_connect.send_command(
    "\n", expect_string=r"Sweep range of sizes", strip_prompt=False, strip_command=False
)
output += net_connect.send_command(
    "\n", expect_string=r"#", strip_prompt=False, strip_command=False
)


net_connect.disconnect()

print()
print(output)
print()