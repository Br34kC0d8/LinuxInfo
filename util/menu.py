

import os
from time import sleep
from util.prints import prints
import libss.info as inf
import libss.network as nt
import libss.clear as cl
class menu:
    def MainMenu():
        os.system('clear')
        prints.mainM()
        sleep(0.5)
        res = str(input('L0g1c4lB0mb ➮ '))
        if res == '1':
            mn = nt.network()
            mn.menu()
        elif res == '2':
            info = inf.info()
            info.menu()
        elif res == '3':
            clr = cl.clear()
            clr.menu() 
        elif res == '4':
            exit()   

    def retm(self):
        prints.retMenu()
        res = str(input('L0g1c4lB0mb ➮ '))
        if res == '1':
            mn = nt.network()
            mn.menu()
        elif res == '2':
            info = inf.info()
            info.menu()
        elif res == '3':
            clr = cl.clear()
            clr.menu()
        elif res == '4':
            os.system('clear')
            exit(
