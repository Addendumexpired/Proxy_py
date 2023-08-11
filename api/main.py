from http.server import BaseHTTPRequestHandler, HTTPServer
import requests

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
        }

        response = requests.get("https://codeload.github.com/pojiezhiyuanjun/freev2/zip/refs/heads/master", headers=headers)

        zip_filename = "master.zip"
        self.send_response(200)
        self.send_header("Content-type", "application/zip")
        self.send_header("Content-Disposition", f"attachment; filename={zip_filename}")
        self.send_header("Content-Length", len(response.content))
        self.end_headers()

        chunk_size = 8192  # Adjust the chunk size as needed
        for i in range(0, len(response.content), chunk_size):
            self.wfile.write(response.content[i:i + chunk_size])

        return
