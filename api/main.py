from http.server import BaseHTTPRequestHandler, HTTPServer
import requests
from bs4 import BeautifulSoup
import re


class handler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
        } 


        target_url = "https://codeload.github.com/pojiezhiyuanjun/freev2/zip/refs/heads/master"
       
           
        response = requests.get(target_url, headers=headers, stream=True)
        
    
            
        #self.send_response(200)
       # self.send_header("Content-Type","text/plain")
        #self.end_headers()
        
       # self.wfile.write(str(len(response.content)).encode('utf-8'))

            
        self.send_response(200)
        self.send_header("Content-Disposition", "attachment; filename=freev2-master.zip")
        self.send_header("Content-Type", "application/zip")
        self.end_headers()
        self.wfile.write(response.content[1:4500000])

        return
