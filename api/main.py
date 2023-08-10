from http.server import BaseHTTPRequestHandler, HTTPServer
import http.client
import requests
from bs4 import BeautifulSoup


class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Content-Type": "application/x-www-form-urlencoded",  # 设置正确的 Content-Type
            "Content-Length": str(content_length)
        }

        target_url = "https://sshocean.com"  # 目标 URL

        # 发起 POST 请求
        response = requests.post(target_url + self.path, headers=headers, data=post_data)

        # 获取响应内容和状态码
        response_content = response.content
        response_status = response.status_code

        # ... (修改 reCAPTCHA Site Key，类似您之前的代码)

        self.send_response(response_status)
        self.send_header("Content-type", response.headers["Content-type"])
        self.end_headers()
        self.wfile.write(response_content)


    
    def do_GET(self):
        headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
        }


        target_url = "https://sshocean.com/"  # 目标 URL
       
        # 发起 GET 请求
        response = requests.get(target_url + self.path, headers=headers)

        # 获取响应内容和状态码
        response_content = response.content
        response_status = response.status_code

        





        soup = BeautifulSoup(response_content, "html.parser")
        recaptcha_element = soup.find("div", class_="g-recaptcha")
        
        if recaptcha_element:
            new_data_sitekey = "6LfkF5cnAAAAAJ9oC_mQ8G3NTIjvGn7QnFXNXEsm"  # 替换为您想要的新 Site Key
            recaptcha_element["data-sitekey"] = new_data_sitekey

        

        self.send_response(response_status)

            
        self.send_header("Content-type", response.headers["Content-type"])
        self.end_headers()
        self.wfile.write(str(soup).encode())

        return



    

 
       

       

  

        
    
