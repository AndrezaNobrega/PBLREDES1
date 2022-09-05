import socket
import threading
from time import sleep
import datetime

UDP_IP_ADDRESS = "127.0.0.1"
UDP_PORT_NO = 60000

class Hidrometro:
    def __init__(self, id):
        self.id = id
        self.bloqueado = False        
    
    def enviaDado(self, dado):
        if self.bloqueado != True:
            while self.bloqueado != True:
                litros= (dado)
                litros = litros.encode()
                clientSock.sendto(litros, (UDP_IP_ADDRESS, UDP_PORT_NO))
                data = datetime.datetime.now() #horário atual
                dataAux = str(data) #convertendo para string
                print(dataAux[:16])                                       
                sleep(2)
        else:
            print('bloqueado')

clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #criando o socket cliente

hidrometro1 = Hidrometro(123) #cria o objeto
dado = '15'
hidrome = threading.Thread(target = hidrometro1.enviaDado(dado), name = 'gera') #executando como thread


while True:
    msg = str(input("Enter your message: "))
    msg = msg.encode()
    clientSock.sendto(msg, (UDP_IP_ADDRESS, UDP_PORT_NO))
    hidrome.start() #startando
    



