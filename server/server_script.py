import http.server
import base64
import socketserver

FLAG = "FLAG{MITM_Attack_Success_123!}"

class AuthRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Require Basic Auth
        auth_header = self.headers.get('Authorization')
        if not auth_header:
            self.send_auth_request()
            return
        
        # Basic Auth is typically "Basic <base64encoded>"
        if auth_header.startswith("Basic "):
            encoded_creds = auth_header.split(" ")[1]
            creds = base64.b64decode(encoded_creds).decode('utf-8')
            
            username, password = creds.split(":", 1)
            if username == "victimuser" and password == "SuperSecretPass":
                # Valid credentials => send the flag!
                self.send_response(200)
                self.send_header("Content-type", "text/plain")
                self.end_headers()
                self.wfile.write(f"Welcome, {username}! The flag is: {FLAG}\n".encode('utf-8'))
                return
        
        # If invalid credentials
        self.send_auth_request()
    
    def send_auth_request(self):
        self.send_response(401)
        self.send_header('WWW-Authenticate', 'Basic realm="MITM Demo"')
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"401 Unauthorized\n")

if __name__ == "__main__":
    HOST, PORT = "0.0.0.0", 80
    with socketserver.TCPServer((HOST, PORT), AuthRequestHandler) as httpd:
        print(f"Serving on {HOST}:{PORT}")
        httpd.serve_forever()
