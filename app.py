# -*- coding: utf-8 -*-
import os 
from time import sleep
import sys
from util.menu import menu
if os.geteuid() != 0:
    exit("Run the script as root")
if sys.version_info < (3, 0):
    input = raw_input

        
if __name__ == '__main__':
    menu.MainMenu()
