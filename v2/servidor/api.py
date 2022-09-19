import http.server
import socketserver
import json
import getData

class myhandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/index':
            self.path = 'v2/servidor'
            return http.server.SimpleHTTPRequestHandler.do_GET(self)
        
        if self.path == '/users': #endpoint #aqui lista o histórico do consumo do hidrômetro por sua ID
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
        
        if self.path == '/litros': #endpoint #aqui busca o valor dos litros consumidos por id do hidrometro
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
                
            data = (getData.getLitrosID(str(input_data['search']))) #Buscar com a função getData o id da entidade desejada(Hidrômetro)

            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()

            output_data = {'Litros gastos': data} #montar o dicionário chave => valor 
            output_json = json.dumps(output_data) #transformar em JSON

            self.wfile.write(output_json.encode('utf-8')) #enviar a resposta pro cliente/insomnia
        
        if self.path == '/valor': #endpoint #aqui retorna o valor da conta com base na id do hidrômetro
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
                
            data = (getData.calculoConta(str(input_data['search']))) #Buscar com a função getData o id da entidade desejada(Hidrômetro)

            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()

            output_data = {'Valor da conta': data} #montar o dicionário chave => valor 
            output_json = json.dumps(output_data) #transformar em JSON

            self.wfile.write(output_json.encode('utf-8')) #enviar a resposta pro cliente/insomnia
        
        if self.path == '/status': #endpoint #aqui retorna se o cliente está em débito (com a conta atrasada), com base em sua ID
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
                
            data = (getData.emDebito(str(input_data['search']))) #Buscar com a função getData o id da entidade desejada(Hidrômetro)

            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()

            output_data = {'Status do cliente': data} #montar o dicionário chave => valor 
            output_json = json.dumps(output_data) #transformar em JSON

            self.wfile.write(output_json.encode('utf-8')) #enviar a resposta pro cliente/insomnia

        if self.path == '/admin': #endpoint #aqui retorna a lista dos clientes, com o status e o valor a ser pago  
            #n precisa enviar nada no insomnia            
            data = (getData.listaHidro()) #Busca a lista de todos os hidrômetros 
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()

            output_data = {'Relatório dos Hidrômetroes': data} #montar o dicionário chave => valor 
            output_json = json.dumps(output_data) #transformar em JSON

            self.wfile.write(output_json.encode('utf-8')) #enviar a resposta pro cliente/insomnia


    def do_POST(self): #aqui modificações
        #HTTP Client
        if self.path == '/bloqueia': #endpoint #aqui o cliente é bloqueado 
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
                
            data = (getData.bloqueiaHidro(str(input_data['search']))) #Buscar com a função getData o id da entidade desejada(Hidrômetro)

            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()

            output_data = {data: 'Foi bloqueado'} #montar o dicionário chave => valor 
            output_json = json.dumps(output_data) #transformar em JSON

            self.wfile.write(output_json.encode('utf-8')) #enviar a resposta pro cliente/insomnia
        #HTTP Client
        if self.path == '/desbloqueia': #endpoint #aqui o cliente é desbloqueado
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
                
            data = (getData.desbloqueiaHidro(str(input_data['search']))) #Buscar com a função getData o id da entidade desejada(Hidrômetro)

            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()

            output_data = {data: 'Foi desbloqueado'} #montar o dicionário chave => valor 
            output_json = json.dumps(output_data) #transformar em JSON

            self.wfile.write(output_json.encode('utf-8')) #enviar a resposta pro cliente/insomnia

        

PORT = 5002
handler = myhandler
print('Iniciando o server')
myserver = socketserver.TCPServer(("", PORT), handler)
myserver.serve_forever()
