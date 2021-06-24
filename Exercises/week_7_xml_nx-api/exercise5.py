# Load the show_version.xml file (originally from a Cisco NX-OS device) using the etree.fromstring() method. 
# Note this XML document, unlike the previous documents, contains the document encoding information. Because the document encoding is at the top of the file, 
# you will need to read the file using "rb" mode (the "b" signifies binary mode). 
# Print out the the namespace map of this XML object. You can accomplish this by using the .nsmap attribute of your XML object.



from __future__ import unicode_literals, print_function
from lxml import etree


def read_xml(filename):
    # Encoding in document forces the read to be binary
    with open(filename, "rb") as infile:
        return etree.fromstring(infile.read())


if __name__ == "__main__":
    filename = "show_version.xml"
    show_version = read_xml(filename)


    print("\n\n")
    print("Print default document namespace mapping")
    print("-" * 20)
    print("Document default Namespace:\n {}".format(show_version.nsmap))


# Similar to earlier exercises, use the find() method to access the text of the "proc_board_id" element (serial number). 
# As this XML object contains namespace data, you will need to use the {*} namespace wildcard in the find() method. 
# Your find call should look as follows:

# find(".//{*}proc_board_id")

# The {*} is a namespace wildcard and says to match ALL namespaces

    print("\n\n")
    print("Print the proc_board_id element using namespace wildcard")
    print("-" * 20)
    serial_number = show_version.find(".//{*}proc_board_id").text
    print(serial_number)