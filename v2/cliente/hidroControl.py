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
pressao = 1 #aqui é a pressão que está sendo exercida no hidrometro
UDP_IP_ADDRESS = "172.16.103.7" #ip do hidrometro

sem = threading.Semaphore() #semaforo
hidrometroiD = str(random.randint(1024,5000))
hidrometro1 = hidrometro.Hidrometro(hidrometroiD) #cria objeto

def getData():
        data = datetime.datetime.now() #pega o horário atual
        dataAux = str(data) #convertendo horário para string
        dataAux= dataAux[:16] #recortando horas e segundos da String
        return dataAux

def vazamento(pressao):    
    if pressao == 0:
        return '0' #significa que está ocorrendo um vazamento
    else:
        return '1' #não há vazamento



"Metodo que altera a vazão do usuário"
def recebeValor(): #pede o valor
    global pressao
    global vazao
    global status
    pressao = str(random.randint(0,9)) #fica sendo gerado um valor entre 0 e 10, caso esse valor seja zero, significa que há algum problema nos canos
    while True:
        if status == False:
            sem.acquire()
            try:
                print('*'*40)
                vazao = int(inputimeout(prompt='digite o valor da vazão:\n', timeout=5)) # no try ele vai mudar o valor
                print('*'*40)
                print('você digitou', vazao)                    
            except TimeoutOccurred:
                print('*'*40)
                print('Valor permanece o mesmo') 
                print('*'*40)                    
            sem.release()
            time.sleep(2) 
        else:
            print('*'*40)
            print('Seu hidrometro está bloqueado, realize o pagamento.')
            print('*'*40)
            time.sleep(2)     

def somaEnvia():   #soma, recolhe dados e os envia   
    global litroConsumidos
    global vazao
    global pressao
    global UDP_IP_ADDRESS 
    vaza = 0
    id = hidrometro1.getId()    
    global status
    HOST = '172.16.103.4'     # Endereco IP do Servidor
    PORT = 5000            # Porta que o Servidor esta
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    dest = (HOST, PORT)
    tcp.connect(dest)     
    while True:
        if status == False:        
            sem.acquire()
            data = getData() #pegando o momento da consumo        
            print('A vazão atual é de:', vazao) 
            litroConsumidos = int(litroConsumidos + vazao)
            print('Temos', litroConsumidos, 'L consumidos')  
            litroConsumidos = str(litroConsumidos)
            vazao = str(vazao) 
            vaza = vazamento(pressao)
            infoHidro = litroConsumidos + ',' + data + ',' +vazao+ ',' +id+ ',' +vaza+ ',' + UDP_IP_ADDRESS + ','
            print('______________________________________________________________________') 
            print ('\n ID:', id ,'\nLitros utilizados:', litroConsumidos, '\nData do envio:', data, '\nVazão atual:',vazao,  '\nSituação do vazamento', vaza) #visualização do envio
            print('______________________________________________________________________') 
            infoHidro = infoHidro.encode() #encodando para que possa ser enviado
            tcp.send(infoHidro)  #enviando dados 
            litroConsumidos = int(litroConsumidos)
            vazao = int(vazao)        
            sem.release()
            time.sleep(2)            
        else:
            vazao = 0
            sem.acquire()
            sem.acquire()
            data = getData() #pegando o momento da consumo        
            print('A vazão atual é de:', vazao) 
            litroConsumidos = int(litroConsumidos + vazao)
            print('Temos', litroConsumidos, 'L consumidos')  
            litroConsumidos = str(litroConsumidos)
            vazao = str(vazao) 
            vaza = vazamento(pressao)
            infoHidro = litroConsumidos + ',' + data + ',' +vazao+ ',' +id+ ',' +vaza+ ',' + UDP_IP_ADDRESS + ','
            print('______________________________________________________________________') 
            print ('\n ID:', id ,'\nLitros utilizados:', litroConsumidos, '\nData do envio:', data, '\nVazão atual:',vazao,  '\nSituação do vazamento', vaza) #visualização do envio
            print('______________________________________________________________________') 
            infoHidro = infoHidro.encode() #encodando para que possa ser enviado
            tcp.send(infoHidro)  #enviando dados 
            litroConsumidos = int(litroConsumidos)
            vazao = int(vazao)        
            sem.release()
            time.sleep(2)            
    tcp.close()

#funão que faz o hidrometro ficar escutando o tempo todo para bloquear # essa conexão é udp
def escuta():
    import socket
    global hidrometroiD
    global UDP_IP_ADDRESS
    UDP_PORT_NO = int(hidrometroiD) #porta que o hidrometro está se conectando
    global status
    data = 0
    serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    serverSock.bind((UDP_IP_ADDRESS, UDP_PORT_NO))
    print('esperando conexão')
    while True:
        data = serverSock.recvfrom(1024)      
        data = str(data[0])       
        if data == "b'1'":
            status = True 
            print('Hidrômetro sendo bloqueado')             
            print('Bloqueado')
            time.sleep(3)
        else:
            status = False
            print('Hidrômetro sendo desbloqueado')             
            print('Desbloqueado!')
            time.sleep(3)      

#startamos os sockets
t = threading.Thread(target = recebeValor)
t.start()
t2 = threading.Thread(target = somaEnvia)
t2.start()
t3 = threading.Thread( target = escuta)
t3.start()
