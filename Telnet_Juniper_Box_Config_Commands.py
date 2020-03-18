# -*- coding: utf-8 -*-
"""
Created on Mon 9 March 2020
@author: Mohamed Abd-moneim

"""

# This is telent code can be run from windows or Linux machines to add configuration to Juniper device

# you need to install Python 3 on your PC first to run the code and you can edit code by notepad++ or any text editor

# you should edit below HOST IP to your router or switch IP where you need to run the configuration

# to install needed packages on linux you connect machine to internet and run below commands to install packages which are used in code

"""
For Fedora, RHEL & CentOS machine commands
sudo yum update
sudo yum install nano
sudo yum install python3

For Ubuntu, Mint, and Debian 
sudo apt-get update
sudo apt-get install nano

For Windows install python3 and pip3 then run below commands
python -m ensurepip --default-pip
python -m pip install --upgrade pip

"""

import getpass
import telnetlib

#Edit your device IP below

HOST = "10.20.62.84"
user = input("Enter username: ")

password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"login:")
tn.write(user.encode('ascii') + b"\n")

if password:
    tn.read_until(b"Password:")
    tn.write(password.encode('ascii') + b"\n")

#Edit commands you want to add to Juniper device, you can add or remove below commands according to your needs

tn.write(b"conf\n")
tn.write(b"set routing-options autonomous-system 65000\n")
tn.write(b"set protocols bgp family inet unicast\n")
tn.write(b"set protocols bgp family inet-vpn unicast\n")
tn.write(b"set protocols bgp family inet6 unicast\n")
tn.write(b"set protocols bgp family inet6-vpn unicast\n")
tn.write(b"set protocols bgp family l2vpn signaling\n")
tn.write(b"set protocols bgp group ibgp-peers type internal\n")
tn.write(b"set protocols bgp group ibgp-peers local-address 10.10.10.10\n")
tn.write(b"set protocols bgp group ibgp-peers cluster 1.1.1.1\n")
tn.write(b"set protocols bgp group ibgp-peers neighbor 20.20.20.20\n")
tn.write(b"set protocols ospf reference-bandwidth 1000g\n")
tn.write(b"set protocols ospf area 0.0.0.0 interface lo0\n")
tn.write(b"set protocols ospf area 0.0.0.0 interface ge-0/0/0.0\n")
tn.write(b"set protocols ospf area 0.0.0.0 interface ge-0/0/5.0 passive\n")
tn.write(b"set interfaces ge-0/0/2 description DNS-AAA\n")
tn.write(b"set interfaces ge-0/0/2 vlan-tagging\n")
tn.write(b"set interfaces ge-0/0/2 encapsulation flexible-ethernet-services\n")
tn.write(b"set interfaces ge-0/0/2 unit 0 description DNS-AAA-server\n")
tn.write(b"set interfaces ge-0/0/2 unit 0 vlan-id 100\n")
tn.write(b"set interfaces ge-0/0/2 unit 0 family inet address 192.168.55.1/30\n")
tn.write(b"commit\n")
tn.write(b"exit\n")
tn.write(b"exit\n")
print(tn.read_all().decode('ascii'))
