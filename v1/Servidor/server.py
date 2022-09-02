#server
import socket

HOST = 'localhost' #ip
PORT = 50000 #número de porta, elevado p/ n ter interf em demais serviços

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #IPV4, estamos usando TCP
s.bind((HOST, PORT)) 
s.listen() #modo de escuta, está aguardando
print('Aguardando a conexão de um cliente')
conn, ender = s.accept() #aceitamos a conexão quando. ender é utilizado p/ mostrar o endereço 

print('Conectando em', ender)
while True:
    data = conn.recv(1024) #recebendo
    if not data: #quando não há mais dados
        print('Fechando a conexão')
        conn.close() 
        break
    conn.sendall(data) 