import http.server
import http.client

class ReverseProxyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # 创建到目标服务器的连接
        target = http.client.HTTPConnection("www.baidu.com")
        target.request("GET", self.path)

        # 获取目标服务器的响应
        response = target.getresponse()

        # 设置本地服务器的响应
        self.send_response(response.status)
        for header, value in response.getheaders():
            self.send_header(header, value)
        self.end_headers()
        self.copyfile(response, self.wfile)

if __name__ == '__main__':
    server_address = ('', 8000)
    httpd = http.server.HTTPServer(server_address, ReverseProxyHandler)
    print('Starting reverse proxy server on port 8000...')
    httpd.serve_forever()
