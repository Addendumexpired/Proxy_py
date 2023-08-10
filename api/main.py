from http.server import BaseHTTPRequestHandler
import http.client
import json


class handler(BaseHTTPRequestHandler):
 
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
     
        target = http.client.HTTPConnection("www.baidu.com")
        target.request("GET", self.path)

    # 获取目标服务器的响应
        response = target.getresponse()
        response_headers = dict(response.getheaders())

    # 构建返回给客户端的响应
        proxy_response = {
            "statusCode": response.status,
            "headers": response_headers,
            "body": response.read().decode('utf-8')
        }
        self.wfile.write(proxy_response.encode('utf-8'))
        return
