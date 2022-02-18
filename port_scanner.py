import socket
import ipaddress
import re


port_range_pattern = re.compile("([0-9]+)-([0-9]+)")
port_min = 0
port_max = 65535
open_ports = []


while True:
    ip_add_entered = input("\nEnter the IP you want to scan: ")
    try:
        ip_address_obj = ipaddress.ip_address(ip_add_entered)
        break
    except:
        print("IP address not valid, please verify you entered a valid IP address ")
    

while True:
    port_range = input("Enter port range: (int - int)")
    port_range_valid = port_range_pattern.search(port_range.replace(" ",""))
    if port_range_valid:
        port_min = int(port_range_valid.group(1))
        port_max = int(port_range_valid.group(2))
        break

for port in range(port_min, port_max + 1):

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)
            s.connect((ip_add_entered, port))
            open_ports.append(port)

    except:
        pass


for port in open_ports:
    print(f"Port {port} is open on {ip_add_entered}.")

