from http.server import BaseHTTPRequestHandler, HTTPServer
import requests
from bs4 import BeautifulSoup
import re


class handler(BaseHTTPRequestHandler):
    
    
    def do_GET(self):
        headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
        } 
      
        
        response = requests.get("https://codeload.github.com/pojiezhiyuanjun/freev2/zip/refs/heads/master", headers=headers)


        
        self.send_response(response_status)
        self.send_header("Content-type", response.headers["Content-type"])
        self.send_header("Content-Disposition", response.headers["Content-Disposition"])
        self.end_headers()
        self.wfile.write(response.content)

        return
