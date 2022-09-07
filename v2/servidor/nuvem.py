import socket
import json

UDP_IP_ADDRESS = "127.0.0.1"
UDP_PORT_NO = 60000

#criando o server
serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSock.bind((UDP_IP_ADDRESS, UDP_PORT_NO)) #usamos o IP e a porta
dadosHidr = [] #criando lista p o json dos dados dos hidrometros
while True:
    data, addr = serverSock.recvfrom(1024)    
    dado = data.decode()
    consumo = {"id": dado[:-22],
               "lSomados": dado[-20:-6],
               "data": dado[-6:-4],
               "nVazao":dado[-4:]
    }
    jsonConsumo = json.dumps(consumo) #criando um Json
    dadosHidr.append(jsonConsumo)
    
    print('\nLitros utilizados: ' + dado[:-22])
    print('\nHorário/Data: ' + dado[-20:-6])
    print('\nVazão atual: ' + dado[-6:-4])
    print('\n ID:' + dado[-4:])
