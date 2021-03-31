import os
from time import sleep


class wrap:
    def init(self,cmd):
        os.system('clear')
        sleep(0.3)
        os.system(cmd)
        print('\n')
        sleep(2) 
        
    def msgWrap(self,msg,comm):
        print(msg)
        sleep(0.5)
        os.system(comm)
        sleep(1)
        os.system('clear')

