from pprint import pprint
from my_devices import network_devices
from my_functions import open_napalm_connection, create_backup


if __name__ == "__main__":
    connections = []
    for device in network_devices:
        conn = open_napalm_connection(device)
        connections.append(conn)

#  Pretty print the arp table for each of these devices. Gather this information using the appropriate NAPALM Getter.

    print("\n\n")
    print("Print arp table of all devices")
    print("-" * 20)
    for conn in connections:
        print("-" * 6)
        pprint(conn.get_arp_table())
        print("-" * 6)

# Attempt to use the get_ntp_peers() method against both of the devices. Does this method work? 
# Your code should gracefully handle any exceptions that occur. 
# In other words, an exception that occurs due to this get_ntp_peers() method, should not cause the program to crash.    

    print("\n\n")
    print("Print NTP peers if available")
    print("-" * 20)
    for conn in connections:
        print("-" * 6)
        try:
            pprint(conn.get_ntp_peers())
        except NotImplementedError:
            print(
                "NTP Peers Getter not implemented for device type {}".format(
                    conn.platform
                )
            )
        print("-" * 6)

# Create another function in "my_functions.py". This function should be named "create_backup" and should accept a NAPALM connection object as an argument. 
# Using the NAPALM get_config() method, the function should retrieve and write the current running configuration to a file. The filename should be 
# unique for each device. In other words, "cisco3" and "arista1" should each have a separate file that stores their running configuration. 
# Note, get_config() returns a dictionary where the running-config is referenced using the "running" key. 
# Call this function as part of your main exercise2 and ensure that the configurations from both cisco3 and arista1 are backed up properly.

    print("\n\n")
    print("Capture and write backup to disk")
    print("-" * 20)
    for conn in connections:
        create_backup(conn)
        #close the NAPALM connection
        conn.close
    print("\n\n")