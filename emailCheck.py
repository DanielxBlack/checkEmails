# /usr/bin/env python3

# Import required modules
from validate_email import validate_email

""" This script uses py3DNS, but does not require import of the module"""

"""This will eventually become a tool to test company emails and their naming conventions"""


# This is a test name
firstName = input("Enter target's first name: ")
midName = input("Enter target's middle name. (if none,leave blank:) ")
lastName = input("Enter target's last name: ")

# Strip extra characters or spaces
firstName = firstName.strip()
midName = midName.strip()
lastName = lastName.strip()


# Change to lowercase
firstName = firstName.lower()
midName = midName.lower()
lastName = lastName.lower()

# Domain
domainName = input("Enter a TLD: ")
domainName = domainName.strip()
domainName = domainName.lower()
domainName = "@" + domainName

# Now let's figure out some emails
a = (f"{firstName}{midName}{lastName}")
b = (f"{firstName}{lastName}")
c = (f"{firstName}")
d = (f"{firstName[0]}{lastName}")
e = (f"{firstName[0]}{midName[:1]}{lastName}")
f = (f"{firstName}.{lastName}")
g = (f"{midName}.{lastName}")

possibilities = [a, b, c, d,e,f,g]

#simple print test
for addy in possibilities:
    theEmail = (f"{addy}{domainName}")
    if validate_email(theEmail,verify=True) == True:
        print(theEmail)
    else:
        ()
