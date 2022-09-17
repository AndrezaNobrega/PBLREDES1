from cgitb import text
from http.server import HTTPServer, BaseHTTPRequestHandler
import time

HOST = ''
PORT = 9999

class SimpleHTTP(BaseHTTPRequestHandler):
    
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()    
        self.wfile.write(bytes("<html><body><h1>HELLO WORLD!</h1></body></hmtl>","utf-8"))

    def do_POST(self): #aqui enviamos informações
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()

        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
        self.wfile.write(bytes('{"time":"'+ date + '"}', "utf-8"))

server = HTTPServer((HOST, PORT), SimpleHTTP )
print('Server rodando')
server.serve_forever()
server.server_close()
print('server parou')