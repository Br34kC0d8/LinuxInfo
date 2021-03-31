from time import sleep
import os 

class prints:
    def netMenu():
        print("""
            [+] Network Connections -> 1
            [+] TCP Connections -> 2
            [+] Network Connections with PID -> 3
            [+] Established Connections -> 4
            [+] Kill Process -> 5
            [+] Block Connection -> 6
            [+] Exit Program -> 7
        """)
    def mainM():
        os.system('clear')
        print("""
                                .-') _           ) (`-.                  .-') _                  
                                ( OO ) )           ( OO ).               ( OO ) )                        
            ,--.      ,-.-') ,--./ ,--,' ,--. ,--. (_/.  \_)-. ,-.-') ,--./ ,--,'    ,------. .-'),-----. 
            |  |.-')  |  |OO)|   \ |  |\ |  | |  |  \  `.'  /  |  |OO)|   \ |  |\ ('-| _.---'( OO'  .-.  '
            |  | OO ) |  |  \|    \|  | )|  | | .-') \     /\  |  |  \|    \|  | )(OO|(_\    /   |  | |  |
            |  |`-' | |  |(_/|  .     |/ |  |_|( OO ) \   \ |  |  |(_/|  .     |/ /  |  '--. \_) |  |\|  |
        (|  '---.',|  |_.'|  |\    |  |  | | `-' /.'    \_),|  |_.'|  |\    |  \_)|  .--'   \ |  | |  |
            |      |(_|  |   |  | \   | ('  '-'(_.-'/  .'.  \(_|  |   |  | \   |    \|  |_)     `'  '-'  '
            `------'  `--'   `--'  `--'   `-----'  '--'   '--' `--'   `--'  `--'     `--'         `-----' 
        """)
        sleep(0.5)
        print("""
            [+] Network Connections Info -> 1
            [+] Linux System Info -> 2
            [+] "Cover your tracks" -> 3
            [+] Exit Program -> 4
        """)
    def retMenu():
        print("""
            [+] Network Menu -> 1
            [+] OS/user Info -> 2
            [+] "cover your tracks" Menu -> 3
            [+] Exit -> 4
        """)
    def infoMn():
        print("""
            [+] User Info -> 1
            [+] OS info -> 2
            [+] Exit Programm -> 3
        """)
        
          
        
    
