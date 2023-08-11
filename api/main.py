from http.server import BaseHTTPRequestHandler, HTTPServer
import http.client
import requests
from bs4 import BeautifulSoup


class handler(BaseHTTPRequestHandler):
    

               
              
                
                
                
    
    def do_GET(self):
        headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
        }

        url1 = "https://github.com/pojiezhiyuanjun/freev2/archive/refs/heads/master.zip"
        response1 = requests.get(url1, allow_redirects=False)

        redirect_url = response1.headers['Location']
        response2 = requests.get(redirect_url, headers=headers)
      
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        self.wfile.write(str(response2.content[1:30]).encode('utf-8'))

        if response2.status_code == 200:
            self.send_response(200)
            self.send_header("Content-type", "application/zip")
            self.send_header("Content-Disposition", "attachment; filename=master.zip")
            self.send_header("Content-Length", len(response2.content))
            self.end_headers()
            self.wfile.write(response2.content[1:30])
            return
