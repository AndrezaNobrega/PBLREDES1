import socket

UDP_IP_ADDRESS = "127.0.0.1"
UDP_PORT_NO = 60000

#criando o server
serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSock.bind((UDP_IP_ADDRESS, UDP_PORT_NO)) #usamos o IP e a porta

while True:
    data, addr = serverSock.recvfrom(1024)
    print ("Recebendo: " + data.decode())
