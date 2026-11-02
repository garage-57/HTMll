from http.server import BaseHTTPRequestHandler,HTTPServer

hostName = 'localhost'
serverPorts = 63342

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("{message: 'OK'}", "utf-8"))