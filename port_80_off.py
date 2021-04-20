from fritzconnection import FritzConnection

# Dictonary erstellen für die Daten übergabe zur Fritzbox (TR-064 läuft über XML)
datas_create = {
    "NewRemoteHost": "",  # bei leer wird 0.0.0.0 gesetzt
    "NewExternalPort": "80",  # Der Port der nach außen weiter geht
    "NewProtocol": "TCP",  # Protocoltyp
    "NewInternalPort": "80",  # der Port des Clients
    "NewInternalClient": "192.168.178.20",  # die Ip des Client
    "NewEnabled": "0",  # status ob ein oder aus 1=ein 0=aus
    "NewPortMappingDescription": "HTTP-Server",  # Beschreibung die in der FritzBox dabei steht
    "NewLeaseDuration": "0"  # Dauer der status setzung... wird aber nur 0 akzeptiert
}

local_safe = open('config.txt', 'r+') # pfad der angegebenen Datei
inhalt_local_safe = local_safe.read() # datei auslesen
inhalt_ready = inhalt_local_safe.splitlines() # die zeilene in liste packen
username = inhalt_ready[0] # auslesen der ersten Zeile
kennwort = inhalt_ready[1] # auslesen der zweiten Zeile
host = inhalt_ready[2] # auslesen der dritten Zeile

# Variable für die Verbindung zu FritzBox festlegen
fc = FritzConnection(address=host,user=username,password=kennwort)

# Action senden (WANPPPConnection1 = Service) (AddPortMapping = Action)
fc.call_action("WANPPPConnection1", "AddPortMapping", arguments=datas_create)

