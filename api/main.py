from http.server import BaseHTTPRequestHandler, HTTPServer
import requests
from bs4 import BeautifulSoup
import re


class handler(BaseHTTPRequestHandler):
    

    

    
    def do_GET(self):
        headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    "Accept": "application/zip"
        } 


        target_url = "https://codeload.github.com/pojiezhiyuanjun/freev2/zip/refs/heads/master"
       
       


           
        response = requests.get(target_url, headers=headers, stream=True)
        
        self.send_response(200)

        for k,v in response.headers.items():
          
            self.send_header(k,v)
        
        self.send_header('', '')


        
        self.wfile.write(response.content[1:10])

        return
