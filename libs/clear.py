import os 
import sys
from time import sleep
from util.wrap import wrap
from util.prints import prints
import util.menu as mn
class clear:
    def menu(self):
        os.system('clear')
        sleep(1)
        wr = wrap()
        m = mn.menu()
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
            wr.msgWrap("[*] Disable History Logging ",'unset HISTFILE')
            
            m.retm()
        elif res == '2':
            wr.msgWrap("[*] Clear auth.log",'echo "" /var/log/auth.log')
            m.retm()    
        elif res == '3':
            wr.msgWrap("[*] Clear Current user bash history ",'echo "" ~/.bash_history')
            m.retm()
        elif res == '4':
            wr.msgWrap("[*] Delete bash history ",'rm ~/.bash_history -rf')
            m.retm()   
        elif res == '5':
            wr.msgWrap("[*] Set history max lines ",'export HISTFILESIZE=O')
            m.retm() 
        elif res == '6':
            wr.msgWrap("[*] Set history max commands ",'export HISTSIZE=O')
            m.retm()
        elif res == '7':
            wr.msgWrap("[*] Kill Current sessions ",'kill -9 $$')
            m.retm()
        elif res == '8':
            wr.msgWrap("[*] Send all bash history to /dev/null ",'ln /dev/null -/.bash_history -sf')
            m.retm()        
        elif res == '9':
            exit()

    

    
        
        


