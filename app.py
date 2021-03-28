# -*- coding: utf-8 -*-
import os 
from time import sleep
import sys
from libss.network import network
from libss.info import info
from libss.clear import clear
if os.geteuid() != 0:
    exit("Run the script as root")
if sys.version_info < (3, 0):
    input = raw_input



def MainMenu():
    os.system('clear')
    print("""
                             .-') _           ) (`-.                  .-') _                  
                            ( OO ) )           ( OO ).               ( OO ) )                        
        ,--.      ,-.-') ,--./ ,--,' ,--. ,--. (_/.  \_)-. ,-.-') ,--./ ,--,'    ,------. .-'),-----. 
        |  |.-')  |  |OO)|   \ |  |\ |  | |  |  \  `.'  /  |  |OO)|   \ |  |\ ('-| _.---'( OO'  .-.  '
        |  | OO ) |  |  \|    \|  | )|  | | .-') \     /\  |  |  \|    \|  | )(OO|(_\    /   |  | |  |
        |  |`-' | |  |(_/|  .     |/ |  |_|( OO ) \   \ |  |  |(_/|  .     |/ /  |  '--. \_) |  |\|  |
       (|  '---.',|  |_.'|  |\    |  |  | | `-' /.'    \_),|  |_.'|  |\    |  \_)|  .--'   \ |  | |  |
        |      |(_|  |   |  | \   | ('  '-'(_.-'/  .'.  \(_|  |   |  | \   |    \|  |_)     `'  '-'  '
        `------'  `--'   `--'  `--'   `-----'  '--'   '--' `--'   `--'  `--'     `--'         `-----' 
    """)
    sleep(0.5)
    print("""
        [+] Network Connections Info -> 1
        [+] Linux System Info -> 2
        [+] "Cover your tracks" -> 3
        [+] Exit Program -> 4
    """)
    sleep(0.5)
    res = str(input('L0g1c4lB0mb ➮ '))
    if res == '1':
        net = network()
        net.menu()
    elif res == '2':
        inf = info()
        inf.menu()
    elif res == '3':
        cl = clear()
        cl.menu()        
        
if __name__ == '__main__':
    MainMenu()
