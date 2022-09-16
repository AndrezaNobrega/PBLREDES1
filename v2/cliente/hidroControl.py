import threading
import time
from inputimeout import inputimeout, TimeoutOccurred
import hidrometro
import random
import socket
import datetime

UDP_IP_ADDRESS = "127.0.0.1" #ip local
UDP_PORT_NO = 60000 #porta da máquina

clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #criando o socket cliente, conexão UDP

vazao = 0
litroConsumidos = 0

sem = threading.Semaphore() #semaforo

id = random.randint(1000,9999) #gera a matrícula
hidrometroiD = str(random.randint(1000,9999))
hidrometro1 = hidrometro.Hidrometro(hidrometroiD) #cria objeto

def getData():
        data = datetime.datetime.now() #pega o horário atual
        dataAux = str(data) #convertendo horário para string
        dataAux= dataAux[:16] #recortando horas e segundos da String
        return dataAux

def recebeValor(): #pede o valor
    global vazao
    while True:
        sem.acquire()
        try:
            vazao = int(inputimeout(prompt='digite o valor da vazão:\n', timeout=5)) # no try ele vai mudar o valor
            print('você digitou', vazao)                    
        except TimeoutOccurred:
            print('Valor permanece o mesmo')                     
        sem.release()
        time.sleep(2)  

def somaEnvia():   #soma, recolhe dados e os envia   
    global litroConsumidos
    global vazao
    id = hidrometro1.getId()     
    while True:        
        sem.acquire()
        data = getData() #pegando o momento da consumo        
        print('A vazão atual é de:', vazao) 
        litroConsumidos = litroConsumidos + vazao
        print('Temos', litroConsumidos, 'L consumidos')  
        litroConsumidos = str(litroConsumidos)
        vazao = str(vazao)      
        infoHidro = litroConsumidos + data + vazao + id
        print ('\n ID:', id ,'\nLitros utilizados:', litroConsumidos, '\nData do envio:', data, '\nVazão atual:', vazao) #visualização do envio
        infoHidro = infoHidro.encode() #encodando para que possa ser enviado
        clientSock.sendto(infoHidro, (UDP_IP_ADDRESS, UDP_PORT_NO))  #enviando dados 
        litroConsumidos = int(litroConsumidos)
        vazao = int(vazao)        
        sem.release()
        time.sleep(2)

print('\nA VAZÃO DEVE SER SEMPRE NO FORMATO XX \n')
t = threading.Thread(target = recebeValor)
t.start()
t2 = threading.Thread(target = somaEnvia)
t2.start()
