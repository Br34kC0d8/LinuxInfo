
import os 
from time import sleep
import sys

class info:
    def menu(self):
        os.system('clear')
        print("""
            [+] User Info -> 1
            [+] OS info -> 2
            [+] Exit Programm -> 3
        """)
        res = str(input('L0g1c4lB0mb ➮ '))
        if res == '1':
            self.userinfo()
        elif res == '2':
            self.OSinfo()
        elif res == '3':
            exit()

    def userinfo(self):
        os.system('clear')
        print("""
            [+] Current Username -> 1
            [+] Logged Users -> 2
            [+] Last User Logged -> 3
            [+] Current User Info -> 4
            [+]  Users list -> 5
        """)
        print('\n')
        res = str(input('L0g1c4lB0mb ➮ '))
        
        if res == '1':
            os.system('clear')
            sleep(0.4)
            os.system('id')
        elif res == '2':
            os.system('clear')
            sleep(0.4)
            os.system('w')
        elif res == '3':
            os.system('clear')
            sleep(0.4)
            os.system('last -a')
        elif res == '4':
            os.system('clear')
            sleep(0.4)
            os.system('who -a')
        elif res == '5':
            os.system('clear')
            sleep(0.4)
            os.system('getent passwd')
        print('\n')
        sleep(1)
        print('[+] Go to Linux Info Menu/Local User Info Menu -> [y/n]')
        res = str(input('L0g1c4lB0mb ➮ ').lower())
        if res == 'y':
            self.menu()
        elif res == 'n':
            self.userinfo()
    def OSinfo(self):
        os.system('clear')
        sleep(1)
        print("""
            [+] Disk Usage -> 1
            [+] Process Listing -> 2
            [+] Kernel Version/Kernel info -> 3
            [+] OS info/OS version info -> 4
            [+] Mounted Filesystems -> 5
            [+] Exit Program -> 6
        """)
        sleep(1)
        res = str(input('L0g1c4lB0mb ➮ '))
        if res == '1':
            os.system('clear')
            sleep(0.4)
            os.system('df -h')
        elif res == '2':
            os.system('clear')
            sleep(0.4)
            os.system('ps -ef')
        elif res == '3':
            os.system('clear')
            os.system('uname -a')
            print('\n')
            os.system('cat /proc/version')
        elif res == '4':
            #os.system('clear')
            os.system('cat /etc/issue')
            print('\n')
            #os.system("cat /etc/'release'")
        elif res == '5':
            os.system('mount')
        elif res == '6':
            exit()
        
        print('\n')
        sleep(1)
        print('[+] Go to Linux  Info Menu/Local OS Info Menu -> [y/n]')
        res = str(input('L0g1c4lB0mb ➮ ').lower())
        if res == 'y':
            self.menu()
        elif res == 'n':
            self.OSinfo()


