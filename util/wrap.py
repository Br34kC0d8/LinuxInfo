import os
from time import sleep


class wrap:
    def init(self,cmd):
        os.system('clear')
        sleep(0.3)
        os.system(cmd)
        print('\n')
        sleep(2) 
