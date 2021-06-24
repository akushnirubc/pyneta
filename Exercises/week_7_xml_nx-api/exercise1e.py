# Create a variable named "trust_zone". 
# Assign this variable to be the first "zones-security" element in the XML tree.
# Access this newly created variable and print out the text of 
# the "zones-security-zonename" child.

from __future__ import unicode_literals, print_function
from lxml import etree

# Using a context manager read in the XML file
with open("show_security_zones.xml") as infile:
    # parse string using etree.fromstring
    show_security_zones = etree.fromstring(infile.read())

print("\n\n")
print("Create 'trust_zone' variable and print text of the 'name' child tag")
print("-" * 20)
trust_zone = show_security_zones[0]
print(f"Security zone: {trust_zone[0].text}")