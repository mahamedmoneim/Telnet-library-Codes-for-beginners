# -*- coding: utf-8 -*-
"""
Created on Mon 9 March 2020
@author: Mohamed Abd-moneim

"""

# This is telent code can be run from windows or Linux machines to add configuration to Cisco_IOS_XR device

# you need to install Python 3 on your PC first to run the code and you can edit code by notepad++ or any text editor

#you should edit below HOST IP to your router or switch IP where you need to run the configuration

#to install needed packages on linux you connect machine to internet and run below commands to install packages which are used in code

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

HOST = "10.120.33.27"
user = input("Enter username: ")

password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")

if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

#Edit commands you want to add to Cisco_IOS_XR device, you can add or remove below commands according to your needs

tn.write(b"conf\n")
tn.write(b"router ospf 1 area 0 \n")
tn.write(b"router ospf 1 mpls ldp sync\n")
tn.write(b"router ospf 1 auto-cost reference-bandwidth 100000\n")
tn.write(b"router ospf 1 area 0 interface Loopback0 \n")
tn.write(b"router ospf 1 area 0 interface Loopback0 passive enable\n")
tn.write(b"router ospf 1 area 0 interface GigabitEthernet0/1/0/4\n") 
tn.write(b"router ospf 1 area 0 interface GigabitEthernet0/1/0/4 bfd fast-detect\n")
tn.write(b"router ospf 1 area 0 interface GigabitEthernet0/1/0/4 network point-to-point\n")
tn.write(b"router ospf 1 area 0 interface GigabitEthernet0/1/0/4 passive disable\n")
tn.write(b"router ospf 1 area 0 interface GigabitEthernet0/1/0/14 network point-to-point\n")
tn.write(b"router ospf 1 area 0 interface GigabitEthernet0/1/0/14 passive disable\n")
tn.write(b"router bgp 65000\n")
tn.write(b"router bgp 65000 bgp router-id 10.10.10.10\n")
tn.write(b"router bgp 65000 bgp graceful-restart\n")
tn.write(b"router bgp 65000 address-family ipv4 unicast\n")
tn.write(b"router bgp 65000 address-family vpnv4 unicast\n")
tn.write(b"router bgp 65000 neighbor 10.20.33.5\n")
tn.write(b"router bgp 65000 neighbor 10.20.33.5 remote-as 65000\n")
tn.write(b"router bgp 65000 neighbor 10.20.33.5 update-source Loopback0\n")
tn.write(b"router bgp 65000 neighbor 10.20.33.5 address-family ipv4 unicast\n")
tn.write(b"interface GigabitEthernet0/0/1/5\n")
tn.write(b" cdp\n")
tn.write(b" mtu 9014\n")
tn.write(b" ipv4 address 12.12.13.1 255.255.255.252\n")
tn.write(b"ipv4 access-list ACL_TEST_2 10 permit ipv4 10.56.154.0 0.0.0.255 any\n")
tn.write(b"ipv4 access-list ACL_TEST_2 20 permit ipv4 10.56.158.0 0.0.0.255 any\n")
tn.write(b"ipv4 access-list ACL_TEST_2 30 permit ipv4 10.56.83.0 0.0.0.255 any\n")
tn.write(b"ipv4 access-list ACL_TEST_2 40 permit ipv4 any any\n")
tn.write(b"ipv4 access-list ACT_TEST\n")
tn.write(b" 10 permit tcp any any established\n")
tn.write(b" 20 permit icmp any any\n")
tn.write(b" 30 permit ipv4 any any\n")
tn.write(b" 40 permit ipv4 any any\n")
tn.write(b"commit\n")
tn.write(b"exit\n")
tn.write(b"exit\n")
print(tn.read_all())
