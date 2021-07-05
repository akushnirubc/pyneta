# For both cisco3 and arista1, use the load_merge_candidate() method to stage the candidate configuration. 
# In other words, use load_merge_candidate() and your loopback configuration file to stage a configuration change. 
# Use the NAPALM compare_config() method to print out the pending differences (i.e. the differences between the running configuration and the candidate configuration).

#!/usr/bin/env python
from getpass import getpass
from my_devices import network_devices
from my_functions import open_napalm_connection

if __name__ == "__main__":

    connections = []
    for device in network_devices:
        conn = open_napalm_connection(device)
        connections.append(conn)

    for conn in connections:
        print("\n\n")
        print("-" * 20)
        # stage configurations
        conn.load_merge_candidate(filename="{}-loopbacks".format(conn.hostname))
        print("DIFF before committing to device {}".format(conn.hostname))
        diff = conn.compare_config()
        print(">" * 8)
        print(diff)
        print(">" * 8)
        if diff:
            conn.commit_config()
        print("\nDiff after commiting for device {}".format(conn.hostname))
        print(">" * 8)
        print(conn.compare_config())
        print(">" * 8)
        conn.close()
    print("\n\n")