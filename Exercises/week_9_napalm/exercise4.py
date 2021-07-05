# Manually copy the saved checkpoint to a new file and add an additional loopback interface 
# to the configuration
# Create a Python script that stages a complete configuration replace operation
# (using the checkpoint file that you just retrieved and modified). 
# Once your candidate configuration is staged perform a compare_config (diff) on the configuration 
# to see your pending changes. After the compare_config is complete, 
# then use the discard_config() method to eliminate the pending changes. 
# Next, perform an additional compare_config (diff) to verify that you have no pending configuration changes. 
# Do not actually perform the commit_config as part of this exercise.


#!/usr/bin/env python
from my_functions import open_napalm_connection, create_checkpoint
from my_devices import nxos1

# Disable Self-signed Certificate Warnings
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

NXOS_REPLACE_CANDIDATE = "nxos1_replacement_cfg"

if __name__ == "__main__":
    conn = open_napalm_connection(nxos1)

    # Create a checkpoint from the current configuration
    create_checkpoint(conn)

    print("\n\n")
    conn.load_replace_candidate(NXOS_REPLACE_CANDIDATE)
    print("Config Staged: pending differences {}".format(conn.hostname))
    print(">" * 8)
    print(conn.compare_config())
    print(">" * 8)

    print("\n\n")
    print("Discarding candidate configuaration for device {}".format(conn.hostname))
    conn.discard_config()
    print("Diff after discarding candidate config for device {}".format(conn.hostname))
    print(">" * 8)
    print(conn.compare_config())
    print(">" * 8)
    print("\n\n")
    conn.close()