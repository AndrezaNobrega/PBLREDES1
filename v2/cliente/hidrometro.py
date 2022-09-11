import socket
import _thread
from time import sleep
import datetime

UDP_IP_ADDRESS = "127.0.0.1" #ip local
UDP_PORT_NO = 60000 #porta da máquina

clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #criando o socket cliente, conexão UDP

class Hidrometro: #construtor
    def __init__(self, id):
        self.id = id
        self.bloqueado = False 

    def getId(self): #retorna ID
        return self.id

    def setBloqueado(self): #Bloquear e desbloquear hidrometro
        if self.bloqueado == False:
            bloqueado = True
            self.bloqueado = bloqueado
        else:
            self.bloqueado = False
        return self.bloqueado
# A função enviaDado(self, dado) é utilizada para concatenar os dados, somar os litros e enviar via sockets
    def enviaDado(self, dado): #envia dados para nuvem
        id = str(self.id) #recupera ID
        if self.bloqueado != True:             
            vazao = dado #para salvar a vazão   -variavel aux       
            while self.bloqueado != True:  #roda enquanto for bloqueado
                vazao = int(vazao)  #conversão
                dado = int(dado)    #conversão            
                dado = str(dado)    #conversão
                vazao = str(vazao)  #conversão 
                data = datetime.datetime.now() #pega o horário atual
                dataAux = str(data) #convertendo horário para string
                dataAux= dataAux[:16] #recortando horas e segundos da String              
                litros= str(dado + dataAux +vazao + id) #concatenando todas as informações enviadas
                print ('\n ID:', id ,'\nLitros utilizados:', dado, '\nData do envio:', dataAux, '\nVazão atual:', vazao) #visualização do envio
                litros = litros.encode() #encodando para que possa ser enviado
                clientSock.sendto(litros, (UDP_IP_ADDRESS, UDP_PORT_NO))  #enviando dados                                              
                sleep(3)
                vazao = int(vazao)  #conversão
                dado = int(dado)    #conversão           
                dado = dado+vazao   #somando para que seja enviado todos os litros consumidos pela residência
                dado = str(dado)    #conversão
                vazao = str(vazao)  #conversão
        else:
            print('bloqueado') #caso o hidrometro esteja bloqueado

    def threadEnvia(self, dado): #chamamos a enviaDado() como uma thread
        _thread.start_new_thread(self.enviaDado(dado))

