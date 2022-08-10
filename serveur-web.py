import http.server

def readFile(path):
    return open(path, 'rb').read().decode('utf-8')

def obtenirDocument(path):
    #print(path)
    return readFile('documents' + path)

def mimeType(path):
    if path[-5:] == '.html': return 'text/html'
    if path[-4:] == '.css':  return 'text/css'
    if path[-3:] == '.js':   return 'text/javascript'
    if path[-3:] == '.py':   return 'text/python'
    if path[-4:] == '.svg':  return 'image/svg+xml'
    return 'text/plain'

class ServeurWeb(http.server.BaseHTTPRequestHandler):

    def do_GET(self):

        path = self.path
        if path == '/favicon.ico': return
        if path == '/': path = '/index.html'

        doc = obtenirDocument(path)

        self.send_response(200)
        self.send_header('Content-type', mimeType(path))
        self.end_headers()
        self.wfile.write(doc.encode('utf-8'))

    def log_message(self, format, *args):
        pass

http.server.HTTPServer(('localhost', 8000), ServeurWeb).serve_forever()
