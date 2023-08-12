from http.server import BaseHTTPRequestHandler, HTTPServer
import requests
from bs4 import BeautifulSoup
import re


class handler(BaseHTTPRequestHandler):
    
    
    def do_GET(self):
        target_url ="https://codeload.github.com/pojiezhiyuanjun/freev2/zip/refs/heads/master"
        response = urllib.request.urlopen(target_url)
        
        self.send_response(response.status)
        for header, value in response.getheaders():
            self.send_header(header, value)
        self.end_headers()
        
        self.wfile.write(response.read())

        return
