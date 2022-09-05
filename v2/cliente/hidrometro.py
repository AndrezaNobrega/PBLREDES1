import socket
import threading
from time import sleep
import datetime

UDP_IP_ADDRESS = "127.0.0.1"
UDP_PORT_NO = 60000

clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #criando o socket cliente

class Hidrometro:
    def __init__(self, id):
        self.id = id
        self.bloqueado = False        
    
    def enviaDado(self, dado):
        if self.bloqueado != True:
            while self.bloqueado != True:
                data = datetime.datetime.now() #horário atual
                dataAux = str(data) #convertendo para string
                dataAux= dataAux[:16] #recortando horas e segundos                
                litros= str(dado + ' litros \nHorário:\n' + dataAux)
                print (litros)
                litros = litros.encode()
                clientSock.sendto(litros, (UDP_IP_ADDRESS, UDP_PORT_NO))                                                  
                sleep(3)
        else:
            print('bloqueado')



