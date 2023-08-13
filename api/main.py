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


        response = requests.get("https://github.com/pojiezhiyuanjun/freev2/archive/refs/heads/master.zip", headers=headers,allow_redirects=False )

        self.send_response(response.status_code) #302
        self.send_header("Content-Length", response.headers["Content-Length"]) #0
        self.send_header("Content-Type", response.headers["Content-type"]) #text/html; charset=utf-8
        self.send_header("Location", response.headers["Location"]) #https://codeload.github.com/pojiezhiyuanjun/freev2/zip/refs/heads/master
        self.end_headers()
        
        html_content = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>{response.status_code}</title>
        </head>
        <body>
            <h1>Hello, World!</h1>
            <p>This is a simple HTML page.</p>
        </body>
        </html>
        """
        
        self.wfile.write(html_content.encode('utf-8'))


        return




     

        #self.send_response(200)
        #self.send_header("Content-Type", "text/plain")
       # self.end_headers()
