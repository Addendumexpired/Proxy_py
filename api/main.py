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


        response = requests.get("https://objects.githubusercontent.com/github-production-release-asset-2e65be/199570071/8e83f100-3d17-462f-beef-b77102ab3267?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAIWNJYAX4CSVEH53A%2F20230813%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230813T012439Z&X-Amz-Expires=300&X-Amz-Signature=5fbb25132f2baef27769dfbda925611c7d3689f5c85c2513b70ac1d4dac9282b&X-Amz-SignedHeaders=host&actor_id=130726953&key_id=0&repo_id=199570071&response-content-disposition=attachment%3B%20filename%3Dzz_v2rayN-With-Core-SelfContained.7z&response-content-type=application%2Foctet-stream", headers=headers)
        


        self.send_response(200) 
        self.send_header("Content-Disposition","attachment; filename=test.7z")
        self.send_header("Content-Length",str(len(response.content)))
        self.send_header("Content-Type","application/octet-stream")
        self.end_headers()
        
        
        self.wfile.write(response.content)


        return




     

        #self.send_response(200)
        #self.send_header("Content-Type", "text/plain")
       # self.end_headers()
