# -*- coding: utf-8 -*-
import os 
from time import sleep
import sys
from libss.network import network
from libss.info import info

if os.geteuid() != 0:
    exit("Run the script as root")
if sys.version_info < (3, 0):
    input = raw_input

def MainMenu():
    os.system('clear')
    sleep(0.5)
    print("""
        [+] Network Connections Info -> 1
        [+] Linux System Info -> 2
        [+] Exit Program -> 3
    """)
    sleep(0.5)
    res = str(input('L0g1c4lB0mb ➮ '))
    if res == '1':
        net = network()
        net.menu()
    elif res == '2':
        inf = info()
        inf.menu()    
        
if __name__ == '__main__':
    MainMenu()
