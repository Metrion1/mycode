#!usr/bin/env python3
hostname = input("what value should we set for hostname?")
## Notice how the next line has changed
## here we use the str.lower() method to return a lowercase string
if hostname.lower() == "mtg":
    print("The hostname was found to be mtg")
    print("hostname matches expected config")

## Always print out the user
print("Exiting the script")
