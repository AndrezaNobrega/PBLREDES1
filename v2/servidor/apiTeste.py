import http.server
import socketserver

class myhandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/index':
            self.path = 'v2\servidor\index.html'
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

PORT = 5002
handler = myhandler

myserver = socketserver.TCPServer(("", PORT), handler)
myserver.serve_forever()
print('Server started')