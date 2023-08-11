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


        target_url = "https://github.com/"
        raw_url = "https://raw.githubusercontent.com/" #raw文件
        allfile_url = "https://codeload.github.com/" #所有文件


        match_raw = re.match(r"/([^/]+)/([^/]+)/raw/([^/]+)/([^/]+)", self.path) #单个文件都是raw
        match_allfile =re.match(r"/([^/]+)/([^/]+)/archive/refs/heads/([^/]+).zip", self.path)
        



        if match_raw:
            response = requests.get(raw_url + f"/{match_raw.group(1)}/{match_raw.group(2)}/{match_raw.group(3)}/{match_raw.group(4)}", headers=headers)
        elif match_allfile:
            response = requests.get(allfile_url + f"/{match_allfile.group(1)}/{match_allfile.group(2)}/zip/refs/heads/{match_allfile.group(3)}", headers=headers)
        else:
            response = requests.get(target_url + self.path, headers=headers)

        

        # 获取响应内容和状态码
        response_content = response.content
        response_status = response.status_code

        
        self.send_response(response_status)

            
        self.send_header("Content-type", response.headers["Content-type"])
        self.end_headers()
        self.wfile.write(response_content)

        return
