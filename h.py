#! /usr/bin/python3.9
import psutil
ip = psutil.net_if_addrs()
if(ip["wlan0"][0].netmask == None):
    ip1 = "Not Connected"
else:
    ip1 = ip["wlan0"][0].address
if(ip["eth0"][0].netmask == None):
    ip2 = "Not Connected"
else:
    ip2 = ip["eth0"][0].address
print(ip1)
print(ip2)