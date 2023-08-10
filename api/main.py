from http.server import BaseHTTPRequestHandler, HTTPServer
import http.client

class handler(BaseHTTPRequestHandler):

    def do_GET(self):

        target_host = "www.baidu.com"
        target_path = self.path             #api/main.py


        # 创建到目标服务器的连接
        target_connection = http.client.HTTPConnection(target_host)
        target_connection.request("GET", target_path)

        # 获取目标服务器的响应
        target_response = target_connection.getresponse()
        target_response_headers = target_response.getheaders()
        target_response_body = target_response.read()

        # 发送目标服务器的响应给客户端
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(str(target_path).encode())
        return
