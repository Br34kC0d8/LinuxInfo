import os 
from time import sleep
import sys
from util.prints import prints
from util.wrap import wrap
from libss.info import info
from libss.clear import clear
class network:  
    def menu(self):
        os.system('clear')
        wr = wrap()
        sleep(1)
        
        prints.netMenu() 
        res = str(input('L0g1c4lB0mb ➮ '))
        if res == '1':
            self.networkcon()
            
        elif res == '2':
            wr.init('netstat -ant')
            self.retm() 
        elif res == '3':
            wr.init('netstat -tulnp')
            self.retm()
        elif res == '4':
            wr.init('lsof -i')
            self.retm()
        elif res == '5':
            print('PID to kill ')
            res = str(input('L0g1c4lB0mb ➮ '))
            self.killProcess(res)
            self.retm()
        elif res == '6':
            os.system('clear')
            print('[+] IPs to kick  --> ')
            print('\n')
            os.system("netstat -ant | awk '{print $5}' ")
            print('\n')
            print(' IP  to kick')
            ip = str(input('L0g1c4lB0mb ➮ '))
            sleep(0.5)
            print('Connection port')
            port = str(input('L0g1c4lB0mb ➮ '))
            self.killcon(ip,port)
            self.retm()
        elif res == '7':
            os.system('clear')
            exit()

    def networkcon(self):
        os.system('clear')
        sleep(0.2)
        print("[+] CTRL + C back to network menu")
        sleep(3)
        os.system('watch ss -tp')
        self.menu()

                

    def killProcess(self,proc):
        os.system('kill %s' % proc)
        self.menu()

    def killcon(self,ip,port):
        os.system('sudo ss -K dst %s dport = %s' % (ip,port))
        print('[+] Block Connection --> [y/n]')
        res = str(input('L0g1c4lB0mb ➮ ').lower())
        if res == 'y':
            print('---killing connection')
            os.system('iptables -A INPUT -s %s -p tcp --dport  %s:%s -j DROP' % (ip,port,port))
            sleep(1)
            self.menu()
        elif res == 'n':
            self.menu()
    def retm(self):
        prints.retMenu()
        res = str(input('L0g1c4lB0mb ➮ '))
        if res == '1':
            self.menu()
        elif res == '2':
            inf = info()
            inf.menu()
        elif res == '3':
            clr = clear()
            clr.menu()


