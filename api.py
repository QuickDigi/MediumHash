from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse
import json

from src.MediumHash import MediumHash

hasher = MediumHash()

class HashAPIHandler(BaseHTTPRequestHandler):
    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "*")
        self.end_headers()

    def _set_headers(self, code=200):
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")  # ✅ CORS
        self.end_headers()

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        params = urllib.parse.parse_qs(parsed.query)

        if parsed.path == "/hash":
            msg = params.get("msg", [""])[0].encode()
            h = hasher.hash(msg)

            response = {
                "input": msg.decode(errors="ignore"),
                "hash": h.hex() if isinstance(h, bytes) else str(h)
            }

            self._set_headers(200)
            self.wfile.write(json.dumps(response).encode())
        else:
            self._set_headers(404)
            self.wfile.write(b"Not Found")

def run(server_class=HTTPServer, handler_class=HashAPIHandler, port=8080):
    server_address = ("", port)
    httpd = server_class(server_address, handler_class)
    print(f"Serving hash API on port {port}...")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
