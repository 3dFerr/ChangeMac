import subprocess
import optparse 

parser = optparse.OptionParser()

parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")

parser.parse_args()

interface = input("interface > ") # get the interface to change
new_mac = input("new MAC > ") # get the MAC address

print(f"\n[+] Changing MAC address for {interface} to {new_mac}")


subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["ifconfig", interface, "up"])