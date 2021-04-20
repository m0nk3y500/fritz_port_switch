from fritzconnection import FritzConnection
import time

user = "dafd_server"
password = "dafdraspberry"
address = "192.168.178.1"
fc = FritzConnection(address=address, user=user, password=password)

def datas_create(status):
    datas_create = {
            "NewRemoteHost": "",
            "NewExternalPort": "8888",
            "NewProtocol": "TCP",
            "NewInternalPort": "8888",
            "NewInternalClient": "192.168.178.27",
            "NewEnabled": status,
            "NewPortMappingDescription": "Dashboard",
            "NewLeaseDuration": "0"
        }

    fc.call_action("WANPPPConnection1", "AddPortMapping", arguments=datas_create)


def datas_close(status):
    datas_create = {
        "NewRemoteHost": "",
        "NewExternalPort": "8888",
        "NewProtocol": "TCP",
        "NewInternalPort": "8888",
        "NewInternalClient": "192.168.178.27",
        "NewEnabled": status,
        "NewPortMappingDescription": "Dashboard",
        "NewLeaseDuration": "0"
    }

    fc.call_action("WANPPPConnection1", "AddPortMapping", arguments=datas_create)


if __name__ == '__main__':
    datas_create(1)
    time.sleep(900)
    datas_close(0)