# -*- coding: utf-8 -*-
import os 
from time import sleep
import sys
if os.geteuid() != 0:
    exit("Run the script as root")
if sys.version_info < (3, 0):
    input = raw_input

class network():
    def menu(self):
        os.system('clear')
        sleep(1)
        print('[+] Network Connections -> 1')
        print('[+] TCP Connections -> 2')
        print('[+] Network Connections with PID -> 3')
        print('[+] Established Connections -> 4')
        print('[+] Kill Process -> 5')
        print('[+] Block Connection -> 6')
        print('[+] Exit Program -> 7')
        res = str(input('L0g1c4lB0mb ➮ '))
        if res == '1':
            self.networkcon()
        elif res == '2':
            self.tcpconn()
        elif res == '3':
            self.pidconn()
        elif res == '4':
            self.estbconn()
        elif res == '5':
            print('PID to kill ')
            res = str(input('L0g1c4lB0mb ➮ '))
            self.killProcess(res)
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
        elif res == '7':
            os.system('clear')
            exit()

    def networkcon(self):
        os.system('clear')
        os.system('watch ss -tp')
        self.menu()

    def tcpconn(self):
        os.system('clear')
        sleep(0.3)
        os.system('netstat -ant')
        print('\n')
        sleep(2)
        print('[+] Regresar al menu -> 1')
        sleep(1)
        print('[+] Salir -> 2')
        res = str(input('L0g1c4lB0mb ➮ '))
        if res == '1':
            self.menu()
        elif res == '2':
            exit()

    def pidconn(self):
        os.system('clear')
        sleep(0.5)
        os.system('netstat -tulnp')
        print('\n')
        sleep(3)
        print('[+] Regresar al menu -> 1')
        sleep(1)
        print('[+] Salir -> 2')
        res = str(input('L0g1c4lB0mb ➮ '))
        if res == '1':
            self.menu()
        elif res == '2':
            exit()


    def estbconn(self):
        os.system('clear')
        os.system('lsof -i')
        print('\n')
        sleep(3)
        print('[+] Regresar al menu -> 1')
        sleep(1)
        print('[+] Salir -> 2')
        res = str(input('L0g1c4lB0mb ➮ '))
        if res == '1':
            self.menu()
        elif res == '2':
            exit()

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
        



class info:
    def menu(self):
        os.system('clear')
        print('[+] User Info -> 1')
        print('[+] OS info -> 2')
        print('[+] Exit Programm -> 3')
        res = str(input('L0g1c4lB0mb ➮ '))
        if res == '1':
            self.userinfo()
        elif res == '2':
            self.OSinfo()
        elif res == '3':
            exit()

    def userinfo(self):
        os.system('clear')
        print('[+] Current Username -> 1')
        print('[+] Logged Users -> 2')
        print('[+] Last User Logged -> 3')
        print('[+] Current User Info -> 4')
        print('[+]  Users list -> 5')
        res = str(input('L0g1c4lB0mb ➮ '))
        print('\n')
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
        print('[+] Disk Usage -> 1')
        print('[+] Process Listing -> 2')
        print('[+] Kernel Version/Kernel info -> 3')
        print('[+] OS info/OS version info -> 4')
        print('[+] Mounted Filesystems -> 5')
        print('[+] Exit Program -> 6')
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



def MainMenu():
    os.system('clear')
    sleep(0.5)
    print('[+] Network Connections Info -> 1')
    print('[+] Linux System Info -> 2')
    print('[+] Exit Program -> 3')
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
