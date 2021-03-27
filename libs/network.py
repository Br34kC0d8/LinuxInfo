import os 
from time import sleep
import sys
class network():
    def menu(self):
        os.system('clear')
        sleep(1)
        print("""
            [+] Network Connections -> 1
            [+] TCP Connections -> 2
            [+] Network Connections with PID -> 3
            [+] Established Connections -> 4
            [+] Kill Process -> 5
            [+] Block Connection -> 6
            [+] Exit Program -> 7
        """)       
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
        sleep(0.2)
        print("[+] CTRL + C back to network menu")
        sleep(3)
        os.system('watch ss -tp')
        self.menu()

    def tcpconn(self):
        os.system('clear')
        sleep(0.3)
        os.system('netstat -ant')
        print('\n')
        sleep(2) 
        print("""[+] Regresar al menu -> 1
            [+] Salir -> 2
        """)
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
        sleep(2)
        print("""
            [+] Regresar al menu -> 1
            [+] Salir -> 2
        """)
        sleep(1)
        res = str(input('L0g1c4lB0mb ➮ '))
        if res == '1':
            self.menu()
        elif res == '2':
            exit()

    def estbconn(self):
        os.system('clear')
        os.system('lsof -i')
        print('\n')
        sleep(2)
        print("""
            [+] Regresar al menu -> 1
            [+] Salir -> 2
        """)
        sleep(1)
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
