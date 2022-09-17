from __future__ import print_function
import os.path
from googleapiclient.discovery import build
#from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

# If modifying these scopes, delete the file token.json.
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
    global globalValues    
    contador = 0
    listaConta = []    
    for globalValues in globalValues:
        if globalValues[3] == id:
            contador = contador + 1
            print (contador ,globalValues)
            listaConta.append(globalValues)

    return listaConta

def getLitrosID(listaConta):
   for listaConta in listaConta:
    aux = listaConta[0]
    print(aux)
    


 


    
getValues() #chamando aqui
id = input('Digite aqui:')
listaConsumo = getId(id)
getLitrosID(listaConsumo)