import os 
import sys
from time import sleep



class clear:
    def menu(self):
        os.system('clear')
        sleep(1)
        print("""
            [+] Disable history logging -> 1
            [+] Clear auth.log -> 2
            [+] Clear Current user bash history -> 3
            [+] Delete .bash_history -> 4
            [+] Set history max lines -> 5
            [+] Set history max commands-> 6
            [+] Kill Current session -> 7
            [+] Send all bash history to /dev/null -> 8
            [+] Exit -> 9
        """)
        res = str(input('L0g1c4lB0mb ➮ '))
        if res == '1':
            self.wrapp("[*] Disable History Logging ",'unset HISTFILE')
        elif res == '2':
            self.wrapp("[*] Clear auth.log",'echo "" /var/log/auth.log')     
        elif res == '3':
            self.wrapp("[*] Clear Current user bash history ",'echo "" ~/.bash_history')
        elif res == '4':
            self.wrapp("[*] Delete bash history ",'rm ~/.bash_history -rf')    
        elif res == '5':
            self.wrapp("[*] Set history max lines ",'export HISTFILESIZE=O')
        elif res == '6':
            self.wrapp("[*] Set history max commands ",'export HISTSIZE=O')
        elif res == '7':
            self.wrapp("[*] Kill Current sessions ",'kill -9 $$')
        elif res == '8':
            self.wrapp("[*] Send all bash history to /dev/null ",'ln /dev/null -/.bash_history -sf')        
        elif res == '9':
            exit()

    def wrapp(self,msg,comm):
        print(msg)
        sleep(0.5)
        os.system(comm)
        sleep(1)
        os.system('clear')
        self.menu()
        


