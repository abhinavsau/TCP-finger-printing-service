#! /usr/bin/python
#Author Abhinav Sau

import sys
from scapy.all import *

def main():
    ip = sys.argv[1]
    ans,unans=sr( IP(dst=ip)/TCP(dport=80,flags="S"))
    ans.summary( lambda(s,r) : r.sprintf("%IP.src% is alive"))

if __name__ == "__main__" : main()
