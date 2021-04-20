from fritzconnection import FritzConnection


def create_port(fc, dicty):
    create = fc.call_action("WANPPPConnection1", "AddPortMapping", arguments=dicty)
    print(create)
    print(dicty)
    print(fc)

def getPortEntry(fc):
    anzahl = fc.call_action("WANPPPConnection1", "GetPortMappingNumberOfEntries")
    portinfo = fc.call_action("WANPPPConnection1", "GetGenericPortMappingEntry", arguments={"NewPortMappingIndex": "0"})
    infos = []
    info = "Anzahl: " +str(anzahl['NewPortMappingNumberOfEntries']) + " | Ports: " +str(infos)
    return info

def close_port(fc, dicty):
    exit_port = fc.call_action("WANPPPConnection:1", "AddPortMapping", arguments=dicty)
    print(exit_port)


if __name__ == '__main__':
    port = input("Port eingeben: ")

    datas_create = {
        "NewRemoteHost": "",
        "NewExternalPort": port,
        "NewProtocol": "TCP",
        "NewInternalPort": port,
        "NewInternalClient": "192.168.178.20",
        "NewEnabled": "1",
        "NewPortMappingDescription": "HTTP-Server",
        "NewLeaseDuration": "0"
    }

    datas_close = {
        "NewRemoteHost": "",
        "NewExternalPort": port,
        "NewProtocol": "TCP",
        "NewInternalPort": port,
        "NewInternalClient": "192.168.178.20",
        "NewEnabled": "0",
        "NewPortMappingDescription": "HTTP-Server",
        "NewLeaseDuration": "0"
    }

    user = "dafd_server"
    password = "dafdraspberry"
    address = "192.168.178.1"
    fc = FritzConnection(address=address, user=user, password=password)

    modus = input("Port Freigeben? [f] | Port Sperren? [s] | Port Info? [i]")
    if modus == "f":
        create_port(fc, datas_create)
    elif modus == "s":
        close_port(fc, datas_close)
    elif modus == "i":
        print(getPortEntry(fc))
