import socket
import _thread
from time import sleep


UDP_IP_ADDRESS = "127.0.0.1" #ip local
UDP_PORT_NO = 60000 #porta da máquina

clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #criando o socket cliente, conexão UDP

class Hidrometro: #construtor
    def __init__(self, id):
        self.id = id
        self.bloqueado = False       

    def getId(self): #retorna ID
        id = str(self.id)
        return id

    def setBloqueado(self): #Bloquear e desbloquear hidrometro
        if self.bloqueado == False:
            bloqueado = True
            self.bloqueado = bloqueado
        else:
            self.bloqueado = False
        return self.bloqueado    

