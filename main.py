# Port-Switch Control for FritzBox from Samuel Zielke
# Erstellt: 09.05.2022
# ...

# Modul Import
from os import system, name
from colorama import Fore, Back
import time
from yaml import load, Loader, dump
from fritzconnection import FritzConnection

#VARs
cfg = {}
port_intern = 0
port_extern = 0
host_intern = ""

def clear():
      
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def look_up():

    clear() #Fenster Inhalt löschen

    print()
    print(Fore.WHITE + '----------------------------')
    print(Fore.WHITE + 'Fritz-PortControl from M0nk3y500')
    # time.sleep(0.2)
    print(Fore.WHITE + 'Version 2.0 - 09.05.2022')
    # time.sleep(0.2)
    print(Fore.WHITE + '----------------------------\n')
    # time.sleep(0.2)
    print("\nÜberprüfe Einstellungen ...\n")
    # time.sleep(0.2)

    checkSettings()
    time.sleep(0.2)

    task_to_take()
    time.sleep(0.2)


def checkSettings():
    with open("config.yml", "r") as ymlfile:
        cfg = load(ymlfile, Loader=Loader)


    SettingCheckResult = ""
    MyErrorLog = []

    if cfg["host"] == None:
        # SettingCheckResult += Fore.RED + "\n\U0001F5A8  -> " + "HOST EMPTY!"
        print(Fore.RED + "\U0001F4DF  -> " + "HOST EMPTY!")
        MyErrorLog.append("host")
    else:
        # SettingCheckResult += Fore.WHITE + "\n\U0001F5A8  -> " + con_settings["host"]
        print(Fore.WHITE + "\U0001F4DF -> " + cfg["host"])

    if cfg["user"] == None:
        # SettingCheckResult += Fore.RED + "\n\U0001F522 -> " + "PORT EMPTY!"
        print(Fore.RED + "\U0001F522 -> " + "User EMPTY!")
        MyErrorLog.append("port")
    else:
        # SettingCheckResult += Fore.WHITE + "\n\U0001F522 -> " + str(con_settings["port"])
        print(Fore.WHITE + "\U0001F522 -> " + str(cfg["user"]))

    if cfg["password"] == None:
        # SettingCheckResult += Fore.RED + "\n\U0001F511 -> " + "API-KEY EMPTY!"
        print(Fore.RED + "\U0001F511 -> " + "Password EMPTY!")
        MyErrorLog.append("api-key")
    else:
        # SettingCheckResult += Fore.WHITE + "\n\U0001F511 -> " + con_settings["api-key"]
        print(Fore.WHITE + "\U0001F511 -> " + "******") #cfg["password"])
    
    
    if len(MyErrorLog) > 0:
           
        for error in MyErrorLog:
            question = input(Fore.BLACK + Back.WHITE + "\nJetzt neuen " + error + " eingeben [j/n]?" + Fore.WHITE + Back.BLACK + "\n>")
            if question == "j":
                newData = input(Fore.BLACK + Back.WHITE + "\nJetzt neue " + error + "-Daten eingeben:" + Fore.WHITE + Back.BLACK + "\n>")
                with open('config.yml') as f:
                    settings = load(f, Loader=Loader)

                if error == "port":
                    newData = int(newData)

                settings[error] = newData

                with open('config.yml', 'w') as f:
                    dump(settings, f)

            elif question == "n": 
                clear()
                a = Fore.RED + "\n\U0001F534 EINSTELLUNGEN"
                a += "\nError with settings of: " + str(MyErrorLog) + "\n"
                a += "\nProzess nach Fehler beendet"

                print(a)
                exit()

            else:
                clear()
                print(Fore.RED + "Eingabe Ungültig! Bitte erneut starten und eingeben!")
                exit()


    else: 
        a= Fore.GREEN + "\n\U0001F44C EINSTELLUNGEN"
        print(a)

def task_to_take():

    print("\nMit Eingabe beginnen ...\n")
    host_intern = input("Host eingeben:\n" + Fore.BLACK)
    port_intern = input("\nPort-Intern eingeben:\n" + Fore.BLACK)
    port_extern = input("\nPort-Extern eingeben:\n" + Fore.BLACK)
    

    # Dictonary erstellen für die Daten übergabe zur Fritzbox (TR-064 läuft über XML)
    datas_create = {
        "NewRemoteHost": "",  # bei leer wird 0.0.0.0 gesetzt
        "NewExternalPort": port_extern,  # Der Port der nach außen weiter geht
        "NewProtocol": "TCP",  # Protocoltyp
        "NewInternalPort": port_intern,  # der Port des Clients
        "NewInternalClient": host_intern,  # die Ip des Client
        "NewEnabled": "1",  # status ob ein oder aus 1=ein 0=aus
        "NewPortMappingDescription": "HTTP-Server",  # Beschreibung die in der FritzBox dabei steht
        "NewLeaseDuration": "0"  # Dauer der status setzung... wird aber nur 0 akzeptiert
    }

    username = cfg["user"] # auslesen der ersten Zeile
    kennwort = cfg["password"] # auslesen der zweiten Zeile
    host = cfg["host"] # auslesen der dritten Zeile

    # Variable für die Verbindung zu FritzBox festlegen
    fc = FritzConnection(address=host,user=username,password=kennwort)

    # Action senden (WANPPPConnection1 = Service) (AddPortMapping = Action)
    fc.call_action("WANPPPConnection1", "AddPortMapping", arguments=datas_create)


look_up()