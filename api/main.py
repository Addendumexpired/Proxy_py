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


        response = requests.get("https://github.com/pojiezhiyuanjun/freev2/archive/refs/heads/master.zip", headers=headers)

       


        s = ""


        attrs = dir(response)


        for attr in attrs:
            if not attr.startswith("__"):  # 排除以双下划线开头的属性
                try:
                    attr_value = str(getattr(response, attr))
                    if isinstance(attr_value, str) and len(attr_value) > 100:
                        attr_value = attr_value[:30] + "..."
                    s += f"\nresponse.{attr}: {attr_value}\n"
                except Exception as e:
                    pass
        





        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(s.encode('utf-8'))


        return

