# ChangeMac
A simple program to change the MAC address

 - When run the program pass an interface and the new mac address as arguments

~~~Options:
  -h, --help            show this help message and exit
  -i INTERFACE, --interface=INTERFACE
                        Interface to change its MAC address
  -m NEW_MAC, --mac=NEW_MAC
                        New MAC address
~~~                       

- Example:
 
`> python3 mac_changer.py -i eth0 -m 22:44:66:33:55:77`
