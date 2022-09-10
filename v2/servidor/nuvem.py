from __future__ import print_function
import socket
from time import sleep
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

UDP_IP_ADDRESS = "127.0.0.1"
UDP_PORT_NO = 60000

#criando o server
serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSock.bind((UDP_IP_ADDRESS, UDP_PORT_NO)) #usamos o IP e a porta

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
def main():
    #Script para conexão servidor/nuvem (google sheets)
    creds = None    
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
        # salvamos para o próximo acesso
        with open('token.json', 'w') as token: #Autenticação p/ acessar a planilha
            token.write(creds.to_json())

    service = build('sheets', 'v4', credentials=creds)

    """ #usar para receber
    sheet = service.spreadsheets() #resgata o arquivo
    result = sheet.values().get(spreadsheetId='1SDuvwzFTQ4_KIgtYVUgTLKVa2okDRYBc4gXl2Fn8fO0',
                                range='Página1!A1:D14').execute()
    values = result.get('values', []) # pegamos o valor da célula

    print(values) """

#recebendo no servidor e enviando para nuvem
    print('Servidor pronto')
    dadosHidr = [] #criando lista p os dados dos hidrometros
    sheet = service.spreadsheets() #resgata o arquivo
    while True:
        data, addr = serverSock.recvfrom(1024)    
        dado = data.decode()
        consumo = [dado[:-22], dado[-20:-6], dado[-6:-4], dado[-4:]]    #separando cada dado para uma célula
        dadosHidr.append(consumo)
        #envio para google sheets
        result = sheet.values().update(spreadsheetId='1SDuvwzFTQ4_KIgtYVUgTLKVa2okDRYBc4gXl2Fn8fO0', #id da planilha
                                    range='Página1!A2', 
                                    valueInputOption= 'USER_ENTERED', #tipo de input - Aqui só avisa como será tratado
                                    body= {"values": dadosHidr}).execute()
        
        print('\nLitros utilizados: ' + dado[:-22])
        print('\nHorário/Data: ' + dado[-20:-6])
        print('\nVazão atual: ' + dado[-6:-4])
        print('\n ID:' + dado[-4:])
        sleep(10)

if __name__ == '__main__':
    main()