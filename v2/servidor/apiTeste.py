import http.server
import socketserver
import time
import json
import getData

class myhandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/index':
            self.path = 'v2/servidor'
            return http.server.SimpleHTTPRequestHandler.do_GET(self)
        
        if self.path == '/users': #endpoint
            #HTTP Client
            #Para consulta utilizar
            #{
	        #"search" : idHidrômetro
            #}            
            content_length = int(self.headers['Content-Length']) #json do insomnia
            
            
            if content_length:
                input_json = self.rfile.read(content_length)
                input_data = json.loads(input_json) #Dicionario
            else:
                input_data = None
                
            data = (getData.getId(str(input_data['search']))) #Buscar com a função getData o id da entidade desejada(Hidrômetro)

            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()

            output_data = {'Histórico do hidrometro': data} #montar o dicionário chave => valor 
            output_json = json.dumps(output_data) #transformar em JSON

            self.wfile.write(output_json.encode('utf-8')) #enviar a resposta pro cliente/insomnia

    def do_POST(self): #aqui enviamos informações
        if self.path == '/bloquear':            
            content_length = int(self.headers['Content-Length']) #json do insomnia
            
            
            if content_length:
                input_json = self.rfile.read(content_length)
                input_data = json.loads(input_json) #Dicionario
            else:
                input_data = None


            # data = blockUser(input_data['id'])


            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()

            # response = {'response' : 'O usuário do id x foi bloqueado'}

            # self.wfile.write(json.loads(response).encode('utf-8'))

            # self.wfile.write(bytes('{"time":"'+ date + '"}', "utf-8"))

        

PORT = 5002
handler = myhandler
print('Iniciando o server')
myserver = socketserver.TCPServer(("", PORT), handler)
myserver.serve_forever()
print('Server started')