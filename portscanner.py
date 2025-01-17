#!/bin/python3

import sys
import socket
from datetime import datetime

#Define target

if len(sys.argv) == 2:
        target = socket.gethostbyname(sys.argv[1]) #translate hostname to ipv4
else: 
        print("Invalid amount of arguments")
        print("Syntax: python3 scanner.py <ip or domain>")

#add banner

print("-" * 50)
print("Scanning target: "+target)
print("Time started: "+str(datetime.now()))
print("Developed by H45hc0d3")
print("-" * 50)

try:
        for port in range(1,65535):
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                socket.setdefaulttimeout(1)
                result = s.connect_ex((target,port)) #returns an error indicator
                if result == 0:
                        print("Port{} is open".format(port))
                        s.close()
except KeyboardInterrupt:
        print("\nExiting program.")
        sys.exit()
except socket.gaierror:
        print("Hostname could not be resolved.")
        sys.exit()
except socket.error:
        print("Hostname can not connect to server.")
        sys.exit()
