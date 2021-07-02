# Open a connection to the srx2 device and acquire a configuration lock. 
# Validate that the configuration session is indeed locked by SSH'ing into the device and attempting to enter configuration mode ("configure"). 
# Reuse, the 'srx2' device definition from the jnpr_devices.py file that you created in exercise2.

from jnpr.junos import Device
from jnpr.junos.exception import LockError
from jnpr.junos.utils.config import Config
from jnpr_devices import srx2
from getpass import getpass

my_device = Device(**srx2)
my_device.open()

# Create device Config object
my_device_cfg = Config(my_device)

# Lock device configuration
my_device_cfg.lock()

# You should receive a prompt similar to the following: 

# pyclass@srx2> configure
# Entering configuration mode
# Users currently editing the configuration:
#   pyclass (pid 30316) on since 2019-03-08 18:30:51 PST
#       exclusive

# Add code to attempt to lock the configuration again. Gracefully handle the "LockError" exception (meaning the configuration is already locked).

# Try to acquire Lock again
print()
try:
    my_device_cfg.lock()
    print("Lock acquired!")
except LockError:
    print("Device is already locked.")


# 3b. Use the "load" method to stage a configuration using a basic set command, for example, "set system host-name python4life".

# Stage a config to change the device hostname
my_device_cfg.load("set system host-name python4life", format="set", merge=True)

# 3c. Print the diff of the current configuration with the staged configuration. Your output should look similar to the following: 

# [edit system]
# -  host-name srx2;
# +  host-name python4life;

# Check the diff of the staged vs running config
print()
print("Check diff of staged vs running config")
print("-" * 28)
print(my_device_cfg.diff())



# 3d. Rollback the staged configuration. Once again, print out the diff of the staged 
# and the current configuration (which at this point should be None).

# Rollback staged configuration
my_device_cfg.rollback(0)


# Check the diff after the rollback operation
print()
print("Check diff of staged-config vs running-config")
print("-" * 20)
print(my_device_cfg.diff())
print()