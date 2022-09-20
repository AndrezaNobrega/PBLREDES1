from __future__ import print_function
from email import message
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
import json
from datetime import date, time, datetime, timedelta

#Scrip do google sheets que é utilizado para buscar as informações da planilha
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
globalValues = 0
def getValues():
    global globalValues
    #Script para conexão servidor/nuvem (google sheets)
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'v2/servidor/client_secret.json', SCOPES) #arquivo usado para fazer a primeira autenticação
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token: #Autenticação p/ acessar a planilha
            token.write(creds.to_json())

    service = build('sheets', 'v4', credentials=creds)
    
    #Transformando os valores em uma lista
    sheet = service.spreadsheets() #resgata o arquivo
    result = sheet.values().get(spreadsheetId='1SDuvwzFTQ4_KIgtYVUgTLKVa2okDRYBc4gXl2Fn8fO0',
                                range='Página1').execute()
    values = result.get('values', []) # pegamos o valor da célula
    globalValues = values  
    

def getId(id): #lista pelo ID
    getValues() 
    global globalValues    

    contador = 0
    listaConta = []    
    for globalValues in globalValues:
        if globalValues[3] == str(id):
            contador = contador + 1
            #print (contador ,globalValues)
            listaConta.append(globalValues)

    return listaConta

def getLitrosID(id): #método que pega o valor consumido com base na id
    getValues()     
    contador = 0
    listaConta = []
    global globalValues  
    for globalValues in globalValues:
        if globalValues[3] == str(id):
            contador = contador + 1            
            listaConta.append(globalValues)    
    aux = 0
    for listaConta in listaConta:
        aux = listaConta[0]        
    return aux

#retorna o valor da conta, com base na sua id
#usa como parametro a sua ID
def calculoConta(id): #calculando o valor da conta
    totalLitros = int(getLitrosID(id))

    metrosC = totalLitros/1000
    if totalLitros <= 6000:
        valorReais = 28,82
    if metrosC > 7 and 10:
        valorReais = (metrosC - 6)*1.17 + 28.82
    if metrosC > 11 and 15:
        valorReais = (metrosC - 11)*7.4 + 28.82
    if metrosC > 16 and 20:
        valorReais = (metrosC - 16)*8 + 28.82
    if metrosC > 21 and 25:
        valorReais = (metrosC - 21)*10.51 + 28.82
    if metrosC > 26 and 30:
        valorReais = (metrosC - 26)*11.71 + 28.82
    if metrosC > 31 and 40:
        valorReais = (metrosC - 31)*12.90 + 28.82
    if metrosC > 41 and 50:
        valorReais = (metrosC - 41)*14.79 + 28.82
    if metrosC > 50:
        valorReais = (metrosC - 50)*17.78 + 28.82
    return valorReais[:4]

# retorna se o hidrometro está em débito ou não
# parametro a id do hidrômetro que será consultado
def emDebito(id):
    devendo = str('Em débito')
    listaId = getId(id) #pega o histórico da id específica
    data = listaId[0][1] #pega a primeira data da conta
    print(data)
    ano = int(2022)
    mes = int(data[3:5])
    dia = int(data[6:8])
    hora = int(data[9:11])
    minuto = int(data[12:14])
    inicio = datetime(year=ano, month=mes, day=dia, hour=hora, minute=minuto, second=0)
    hoje = datetime.now()
    resultado = hoje - inicio #subtrai a primeira data da conta por agora
    if resultado == timedelta(minutes = 2) or resultado > timedelta(minutes = 2): #programei dois minutos para simulaçao
        print('Este usuário está em débito')
        devendo = str('Em debito')
    else:
        print('Quitado')
        devendo = str('Quitado')
    return devendo

# Retorna a listagem de todos os hidrometros com o status se está em débito ou não e o valor da conta a ser paga
def listaHidro():
    getValues()
    listado = []          
    global globalValues
    aux = 'ID'
    for globalValues in globalValues:              
        if globalValues[3] != aux:
            result = []            
            aux = globalValues[3]
            print( 'ID:', aux)
            result.append(aux)
            result.append(calculoConta(globalValues[3])) #verifica valor
            result.append(emDebito(globalValues[3])) #verifica se aquela id está em débito            
            listado.append(result)
    return listado

#enviar mensagem de bloqueio para o hidrometro
#usa como parametro a ID do hidrometro que será bloqueado
def bloqueiaHidro(id):
    import socket
    UDP_IP_ADDRESS = "127.0.0.1"
    UDP_PORT_NO = int(id)
    print('Bloqueando o hidrometro: \n', UDP_PORT_NO)
    Message = ("1") #envia a mensagem para bloquear o hidrometro
    clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print(Message)
    Message = Message.encode()    
    clientSock.sendto(Message, (UDP_IP_ADDRESS, UDP_PORT_NO))
    return id

#enviar mensagem parra desbloqueiar o hidrometro
#usa como parametro a ID do hidrometro
def desbloqueiaHidro(id):
    import socket
    UDP_IP_ADDRESS = "127.0.0.1"
    UDP_PORT_NO = int(id)
    print('Desbloqueando o hidrometro: \n', UDP_PORT_NO)
    Message = ("12") #envia mensagem para desbloquear o hidrometro
    clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print(Message)
    Message = Message.encode()    
    clientSock.sendto(Message, (UDP_IP_ADDRESS, UDP_PORT_NO))
    return id

# Retorna a listagem de todos os hidrometros que estão com vazamento
def listaVazamento():
    getValues()
    listado = []          
    global globalValues
    aux = 'ID'
    for globalValues in globalValues:              
        if globalValues[4] == '0':
           listado.append(globalValues)
    print(listado)
    return listado

listaVazamento()