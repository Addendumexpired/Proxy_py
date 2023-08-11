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


        target_url = "https://github.com/"
       
        # 发起 GET 请求
        response = requests.get(target_url + self.path, headers=headers)

        # 获取响应内容和状态码
        response_content = response.content
        response_status = response.status_code

      #https://github.com/pojiezhiyuanjun/freev2/archive/refs/heads/master.zip 

        self.send_response(response_status)

            
        self.send_header("Content-type", response.headers["Content-type"])
        self.end_headers()
        self.wfile.write(response_content)

        return
