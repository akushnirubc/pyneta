# Using a context manager, the ProcessPoolExecutor, and the map() method, 
# create a solution that executes "show ip arp" on all of the devices defined in my_devices.py.
#  Note, the Juniper device will require "show arp" instead of "show ip arp" so your solution 
#  will have to properly account for this.

from concurrent.futures import ProcessPoolExecutor
import time
from my_devices import network_devices
from my_functions import ssh_command2

def main():
    """
    Use concurrent futures processing to simultaneously gather "show version" output from devices.
    Wait for all threads to complete. Record the amount of time required to do this.
    """   
    start_time = time.time()
    max_procs = 5

    # Create the process pool
    with ProcessPoolExecutor(max_procs) as pool:
        
    # Create list to append processes to
        cmd_list = []
        for device in network_devices:
            if "junos" in device["device_type"]:
                cmd_list.append("show arp")
            else:
                cmd_list.append("show ip arp")
        results = pool.map(ssh_command2, network_devices, cmd_list)

        print("\n\n")
        for result in results:
            print("-" * 40)
            print(result)
            print("-" * 40)
        print("\n\n") 

        end_time = time.time()
        print(f"Finished in {end_time - start_time:.2f}")
        print("\n\n")


if __name__ == "__main__":
    main()

