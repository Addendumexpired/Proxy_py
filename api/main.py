from http.server import BaseHTTPRequestHandler, HTTPServer
import requests

class handler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
        } 

        target_url = "https://baidu.com"
        response = requests.get(target_url, headers=headers, stream=True)
        
        response_status = response.status_code
        response_headers = response.headers
        
        self.send_response(response_status)
        for k, v in response_headers.items():
            self.send_header(k, v)
        self.end_headers()
        
        
        self.wfile.write(response_content)
        
        return
