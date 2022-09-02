#cliente
import socket

HOST = '127.0.0.1' #ip
PORT = 50000 #a porda deve ser a msm para a comunicação

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #família de protocolo
s.connect((HOST, PORT)) #solicitamos a conexão
s.sendall(str.encode('Hello World'))
data = s.recv(1024)

print('Mensagem ecoada:', data.decode())