# On your AWS lab server, look at the ntc-templates index file (at ~/ntc-templates/templates/index). Look at some of the commands available for cisco_ios (you can use 'cat ~/ntc-templates/templates/index | grep cisco_ios' to see this). 
# Also look at some of the abbreviated forms of Cisco IOS commands that are supported in the index file.

# Create a script using Netmiko that executes 'show version' and 'show lldp neighbors' against the Cisco4 device with use_textfsm=True.

# What is the outermost data structure that is returned from 'show lldp neighbors' (dictionary, list, string, something else)? 
# The Cisco4 device should only have one LLDP entry (the HPE switch that this router connects to). From this LLDP data, print out the remote device's interface. 
# In other words, print out the port number on the HPE switch that Cisco4 connects into.

from netmiko import ConnectHandler
from getpass import getpass

device = {
    "host": 'cisco4.lasthop.io', 
    "username": 'pyclass', 
    "password": getpass(), 
    "device_type": 'cisco_ios', 
    "session_log": 'my_session.txt',
}

net_connect = ConnectHandler(**device)
print(net_connect.find_prompt())
print()
cmds = ["show version", "show lldp neighbors"]
for cmd in cmds:
    output = net_connect.send_command(cmd, use_textfsm=True)
    print("*" *80)
    print(cmd)
    print("*" * 80)
    print(output)
    print("*" * 80)

    if cmd == "show lldp neighbors":
        print("LLDP Data structure type {}".format(type(output)))
        print("test {}".format(output[0]))
        print("HPE Switch connection port{}".format(output[0]["neighbor_interface"]))


net_connect.disconnect()