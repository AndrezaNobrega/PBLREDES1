import socket
import threading
from time import sleep
import datetime

UDP_IP_ADDRESS = "127.0.0.1" #ip local
UDP_PORT_NO = 60000 #porta da máquina

clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #criando o socket cliente, conexão UDP

class Hidrometro:
    def __init__(self, id):
        self.id = id
        self.bloqueado = False 

    def getId(self): #retorna ID
        return id

    def setBloqueado(self): #Bloquear e desbloquear hidrometro
        if self.bloqueado == False:
            bloqueado = True
            self.bloqueado = bloqueado
        else:
            self.bloqueado = False
        return self.bloqueado

    def enviaDado(self, dado): #envia dados para nuvem
        if self.bloqueado != True:             
            vazao = dado #para salvar a vazão
            vazao = int(vazao)
            while self.bloqueado != True:  
                dado = int(dado)                
                dado = dado+vazao
                dado = str(dado)
                data = datetime.datetime.now() #horário atual
                dataAux = str(data) #convertendo para string
                dataAux= dataAux[:16] #recortando horas e segundos                
                litros= str(dado + dataAux)
                print (litros)
                litros = litros.encode()
                clientSock.sendto(litros, (UDP_IP_ADDRESS, UDP_PORT_NO))                                                  
                sleep(3)
        else:
            print('bloqueado')



