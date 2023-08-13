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

        target_url = "https://codeload.github.com/pojiezhiyuanjun/freev2/zip/refs/heads/master"
       
        response = requests.get(target_url, headers=headers)
'''
        range_header = self.headers.get("Range")
        if range_header:
            start, end = range_header.strip("bytes=").split("-")
            start = int(start)
            end = int(end) if end else None
            content_range = f"bytes {start}-{end if end else ''}/{len(response.content)}"
            content_length = end - start + 1 if end else (len(response.content) - start)
            self.send_response(206)
            self.send_header("Content-type", "application/octet-stream")
            self.send_header("Content-Range", content_range)
            self.send_header("Content-Length", str(content_length))
        else:
            self.send_response(200)
            self.send_header("Content-type", "application/octet-stream")

        self.end_headers()
        
        if range_header:
            self.wfile.write(response.content[start:end+1])
        else:
            self.wfile.write(response.content)
'''

        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write("hello".encode('utf-8'))
        return




     

        
