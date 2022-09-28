import subprocess

interface = input("interface > ") # get the interface to change
new_mac = input("new MAC > ") # get the MAC address

print(f"\n[+] Changing MAC address for {interface} to {new_mac}")


subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["ifconfig", interface, "up"])