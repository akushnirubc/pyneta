# Create a new file named my_functions.py. Move your function from exercise1 to this file. Name this function "ssh_command".

from netmiko import ConnectHandler

def ssh_command(device, command):
    """Establish an SSH connection. Execute show command, return results."""
    device = ConnectHandler(**device)
    output = device.send_command(command)
    device.disconnect()
    print("\n")
    print("-" * 20)
    print(output)
    print("-" * 20)
    print("\n")
    return


# Create a new function that is a duplicate of your "ssh_command" function. Name this function "ssh_command2". 
# This function should eliminate all printing to standard output and should instead return the show command output. 
# Note, in general, it is problematic to print in the child thread as you can get into race conditions between the threads

def ssh_command2(device, command):
    """Establish an SSH connection. Execute show command, return results."""
    device = ConnectHandler(**device)
    output = device.send_command(command)
    device.disconnect()
    return output
