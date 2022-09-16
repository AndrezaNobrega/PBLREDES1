import threading
import time
from inputimeout import inputimeout, TimeoutOccurred
import hidrometro
import random
import socket
import datetime

HOST = '127.0.0.1'     # Endereco IP do Servidor
PORT = 5000            # Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)
tcp.connect(dest)

vazao = 11 #a vazão inicia com 11
litroConsumidos = 0

sem = threading.Semaphore() #semaforo
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
        tcp.send(infoHidro)  #enviando dados 
        litroConsumidos = int(litroConsumidos)
        vazao = int(vazao)        
        sem.release()
        time.sleep(2)
    tcp.close()
print('\nA VAZÃO DEVE SER SEMPRE NO FORMATO XX \n')
t = threading.Thread(target = recebeValor)
t.start()
t2 = threading.Thread(target = somaEnvia)
t2.start()
