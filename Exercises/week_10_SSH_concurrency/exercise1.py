# Create a Python script that executes "show version" on each of the network devices defined in my_devices.py. 
# This script should execute serially i.e. one SSH connection after the other. 
# Record the total execution time for the script. 
# Print the "show version" output and the total execution time to standard output. 
# As part of this exercise, you should create a function that both establishes a Netmiko connection and that executes a single show command that you pass in as argument. 
# This function's arguments should be the Netmiko device dictionary and the "show-command" argument. The function should return the result from the show command.

import time
from netmiko import ConnectHandler
from my_devices import network_devices

def ssh_command(device, command):
    """Establish an SSH connection. Execute show command, return results."""
    device = ConnectHandler(**device)
    output = device.send_command(command)
    device.disconnect()
    return output

def main():
    """
    Serially gather show version output from devices. Record the amount of time required to do
    this.
    """
    start_time = time.time()
    for device in network_devices:
        output = ssh_command(device, "show version")
        print("\n\n")
        print("-" * 20)
        print(output)
        print("-" * 20)
    print("\n\n")
    end_time = time.time()
    print(f"Finished in {end_time - start_time:.2f} seconds")
    print("\n\n")


if __name__ == "__main__":
    main()