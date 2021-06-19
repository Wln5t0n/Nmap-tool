#!/usr/bin/python3
import sys
from os import system as cmd

print(" \n Nmap scanning tool by 'sar1m' follow on github. \n\n")

if len(sys.argv)==2:
        
        ip = ('10.10.10.'+sys.argv[1]) 
        
        cmd('nmap '+ip+' -oA normalscan')
       
        cmd("cat normalscan.nmap | grep open | awk -F/ '{print $1}' ORS=',' | rev | cut -c 2- | rev > opened-ports.txt")
       
        f=open("opened-ports.txt", "r")
        ports = f.read()
        print("\nOPENED PORTS:")
        print(ports)
        
        cmd('nmap -sC -sV '+ip+' -p'+ports)
        
        cmd('rm opened-ports.txt normalscan.gnmap normalscan.xml normalscan.nmap')

else:
        sys.stderr.write("Usage: {0} <last digits of IP>\n\n".format(sys.argv[0]))
        
print("\n\n follow me on:- https://github.com/sar1m")
