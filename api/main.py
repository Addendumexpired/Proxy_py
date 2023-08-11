from http.server import BaseHTTPRequestHandler, HTTPServer
import requests

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
        }

        # 请求网址1，获取重定向的位置
        url1 = "https://github.com/pojiezhiyuanjun/freev2/archive/refs/heads/master.zip"
        response1 = requests.get(url1, allow_redirects=False)

        
            
        redirect_url = response1.headers['Location']

            # 请求网址2
        response2 = requests.get(redirect_url, headers=headers)

            
        self.send_response(200)
        self.send_header("Content-type", "application/zip")
        self.send_header("Content-Disposition", "attachment; filename=master.zip")
        self.send_header("Content-Length", len(response2.content))
        self.end_headers()

                
        self.wfile.write(response2.content)
        return

