from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        self.wfile.write('Riley Key UI:$2a$12$jrUfK7eM4O3zhZvwxqstW.WHmXqX3bXg/Fyyfq5E7Lb1vA1rVtdl2'.encode('utf-8'))
        return
