
import os
from time import sleep

from libss.network import network
from libss.info import info
from libss.clear import clear
from util.prints import prints
class menu:
    def MainMenu():
        os.system('clear')
        prints.mainM()
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
        elif res == '4':
            exit()   

    
        

   