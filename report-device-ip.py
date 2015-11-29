#!/usr/bin/env python3
import netifaces
import requests
import sys

def get_ip_addresses():
    ip_list = []

    for interface in netifaces.interfaces():
        info = netifaces.ifaddresses(interface)
        if netifaces.AF_INET in info:
            for inet in info[netifaces.AF_INET]:
                ip_list.append(inet["addr"])
    return ip_list

def post_data(url, data):
    r = requests.post(url, data = {"data" : data})
    print(r.text);

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: report-device-ip.py <post-url>")
        sys.exit(1)

    post_data(sys.argv[1], " ".join(get_ip_addresses()))
