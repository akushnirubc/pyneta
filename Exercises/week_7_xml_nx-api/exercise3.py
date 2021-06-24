# Open the following two XML files: show_security_zones.xml and show_security_zones_single_trust.xml. Use a generic function that accepts an argument "filename" to open and read a file. 
# Inside this function, use xmltodict to parse the contents of the file. Your function should return the xmltodict data structure. 
# Using this function, create two variables to store the xmltodict data structure from the two files.
# create a second function that uses xmltodict to read and parse a filename that you pass in. 
# This function should support a "force_list" argument that is passed to xmltodict.parse(). 
# Reminder, the force_list argument of xmltodict takes a dictionary where the dictionary key-name is the XML element that is required to be a list. 
# For example:

# force_list={"zones-security": True}

# Use this new function to parse the "show_security_zones_single_trust.xml". 
# Verify the Python data type is now a list for the ['zones-information']['zones-security'] element.

from __future__ import unicode_literals, print_function
import xmltodict

def read_xml_forcelist(filename, force_list=None):
    if force_list is None:
        force_list = {}
    with open(filename, "r") as infile:
        return xmltodict.parse(infile.read(), force_list = force_list)

def read_xml(filename):
    with open(filename, "r") as infile:
        return xmltodict.parse(infile.read())


if __name__ == "__main__":

    filename = "show_security_zones.xml"
    show_security_zones = read_xml(filename)

    filename = "show_security_zones_trust.xml"
    show_security_zones_single = read_xml(filename)

    print("\n\n")
    print("Type of 'zones-security' in the first XML file:")
    print("-" * 20)
    print(type(show_security_zones["zones-information"]["zones-security"]))

    print("\n\n")
    print("Type of 'zones-security' in the single-zone XML file:")
    print("-" * 20)
    print(type(show_security_zones_single["zones-information"]["zones-security"]))

    print("\n\n")
    print("Type of 'zones-security' in the single-zone XML file using force_list:")
    print("-" * 20)
    filename = "show_security_zones_trust.xml"
    show_security_zones_single = read_xml_forcelist(
        filename, force_list={"zones-security": True}
    )
    print(type(show_security_zones_single["zones-information"]["zones-security"]))
    print("\n\n")


# Compare the Python "type" of the elements at ['zones-information']['zones-security']. What is the difference between the two data types? Why?
