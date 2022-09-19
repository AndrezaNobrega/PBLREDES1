from telnetlib import STATUS
import threading
import time
from inputimeout import inputimeout, TimeoutOccurred
import hidrometro
import random
import socket
import datetime



vazao = 11 #a vazão inicia com 11
litroConsumidos = 0
status = False

sem = threading.Semaphore() #semaforo
hidrometroiD = str(random.randint(1024,5000))
hidrometro1 = hidrometro.Hidrometro(hidrometroiD) #cria objeto

def getData():
        data = datetime.datetime.now() #pega o horário atual
        dataAux = str(data) #convertendo horário para string
        dataAux= dataAux[:16] #recortando horas e segundos da String
        return dataAux


"Metodo que altera a vazão do usuário"
def recebeValor(): #pede o valor
    global vazao
    global status
    while True:
        if status == False:
            sem.acquire()
            try:
                vazao = int(inputimeout(prompt='digite o valor da vazão:\n', timeout=5)) # no try ele vai mudar o valor
                print('você digitou', vazao)                    
            except TimeoutOccurred:
                print('Valor permanece o mesmo')                     
            sem.release()
            time.sleep(2) 
        else:
            print('Seu hidrometro está bloqueado, realize o pagamento.')
            time.sleep(2)     

def somaEnvia():   #soma, recolhe dados e os envia   
    global litroConsumidos
    global vazao
    id = hidrometro1.getId()    
    global status
    HOST = '127.0.0.1'     # Endereco IP do Servidor
    PORT = 5000            # Porta que o Servidor esta
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    dest = (HOST, PORT)
    tcp.connect(dest)     
    while True:
        if status == False:        
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
        else:
            vazao = 0
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


def escuta():
    import socket
    global hidrometroiD
    UDP_IP_ADDRESS = "127.0.0.1"
    UDP_PORT_NO = int(hidrometroiD)
    global status
    data = 0
    serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    serverSock.bind((UDP_IP_ADDRESS, UDP_PORT_NO))
    print('esperando conexão')
    while True:
        data, addr = serverSock.recvfrom(1024)
        print('Hidrômetro sendo bloqueado')
        if data == "1":
            status = False
        else:
            status = True
print('\nA VAZÃO DEVE SER SEMPRE NO FORMATO XX \n')

t = threading.Thread(target = recebeValor)
t.start()
t2 = threading.Thread(target = somaEnvia)
t2.start()
t3 = threading.Thread( target = escuta)
t3.start()
