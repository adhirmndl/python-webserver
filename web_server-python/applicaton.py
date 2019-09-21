import http.server
import socketserver

PORT = 9808
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
    socketserver.TCPServer(("", PORT), Handler)
    Handler = http.server.SimpleHTTPRequestHandler
    