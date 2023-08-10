from http.server import BaseHTTPRequestHandler, HTTPServer
import http.client

class handler(BaseHTTPRequestHandler):

    def do_GET(self):

        target_host = "www.baidu.com"
        target_path = self.path             #当前目录路径


        # 创建到目标服务器的连接
        target_connection = http.client.HTTPConnection(target_host)
        target_connection.request("GET", target_path)

        # 获取目标服务器的响应
        target_response = target_connection.getresponse()
        target_response_headers = target_response.getheaders()
        target_response_body = target_response.read()

        self.send_response(target_response.status)
        for header, value in target_response_headers:
            self.send_header(header, value)   
        self.end_headers()
        self.wfile.write(target_response_body)
        return
