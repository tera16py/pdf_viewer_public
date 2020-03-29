from http.server import SimpleHTTPRequestHandler, HTTPServer

print('\n Access here : http://localhost:8000/toppage.html')
server = HTTPServer(('', 8000), SimpleHTTPRequestHandler)
server.serve_forever()
