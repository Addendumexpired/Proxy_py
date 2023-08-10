from http.server import BaseHTTPRequestHandler, HTTPServer


class handler(BaseHTTPRequestHandler):

  def do_GET(self):
    
    text ="""<!DOCTYPE html>
<html>
<head>
    <title>简单的HTML示例</title>
</head>
<body>
    <h1>欢迎来到我的网页</h1>
    <p>这是一个简单的HTML示例，用于演示基本的HTML标记。</p>
    <a href="https://www.example.com">访问示例网站</a>
</body>
</html>
"""
    self.send_response(200)
    self.send_header('Content-type', 'text/html')
    self.end_headers()
    self.wfile.write(text.encode())
    return


