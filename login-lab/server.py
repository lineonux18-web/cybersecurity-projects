from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse

class LoginHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        with open("login.html", "r") as file:
            self.wfile.write(file.read().encode())

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        data = urllib.parse.parse_qs(post_data.decode())

        username = data.get("username", [""])[0]
        password = data.get("password", [""])[0]

        # 🔥 VULNERABLE LOGIN LOGIC
        if username == "admin" and password == "1234":
            response = "Welcome admin!"
        else:
            response = "Login failed"

        self.send_response(200)
        self.end_headers()
        self.wfile.write(response.encode())

server = HTTPServer(("localhost", 8000), LoginHandler)
print("Server running on http://127.0.0.1:8000")
server.serve_forever()
