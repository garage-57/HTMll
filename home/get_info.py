from http.server import BaseHTTPRequestHandler,HTTPServer

hostName = 'localhost'
serverPorts = 8080

class MyServer(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        with open('contacts.html', 'r', encoding='UTF-8') as file:
            home = file.read()
        self.wfile.write(bytes(home, "utf-8"))

if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPorts), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPorts))
    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass
    webServer.server_close()
    print("Server stopped.")