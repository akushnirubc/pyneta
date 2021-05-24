# .bashrc

# Source global definitions
if [ -f /etc/bashrc ]; then
    . /etc/bashrc
fi

# Set PATH to include netmiko-tools
export PATH=/home/akushnir/netmiko_tools/netmiko_tools:/home/akushnir/bin:$PATH

# Modify PYTHONPATH to get extra libraries
export PYTHONPATH=~/python-libs

# Ignore Python Warnings (cryptography, pyyaml, ssl, etc.)
export PYTHONWARNINGS=ignore::Warning

# Setup Django environment variables
export DJANGO_SETTINGS_MODULE=djproject.settings
export PYTHONPATH=$PYTHONPATH:~/DJANGOX/djproject/

# REST-API for NetBox
export NETBOX_TOKEN=63aa375e2590159ca3171c5269931043b85d33cf

# Login to the virtualenv
source /home/akushnir/VENV/py3_venv/bin/activate

