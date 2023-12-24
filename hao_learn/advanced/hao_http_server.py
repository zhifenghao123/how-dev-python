import http.server
import socketserver
import urllib.parse

HOST = ''  # 监听所有可用接口
PORT = 8000  # 监听的端口号


class MyHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        # 解析请求路径和查询参数
        parsed_path = urllib.parse.urlparse(self.path)
        path = parsed_path.path

        if path == '/test':
            # 处理/test请求
            self.send_response(200)  # 设置响应状态码为200（成功）
            self.send_header('Content-type', 'text/plain; charset=utf-8')  # 设置响应头的内容类型
            self.end_headers()  # 结束响应头的发送
            self.wfile.write('good luck'.encode('utf-8'))  # 发送响应体内容
        else:
            # 处理其他请求
            self.send_response(404)  # 设置响应状态码为404（未找到）
            self.send_header('Content-type', 'text/plain; charset=utf-8')  # 设置响应头的内容类型
            self.end_headers()  # 结束响应头的发送
            self.wfile.write('Not Found'.encode('utf-8'))  # 发送响应体内容


if __name__ == '__main__':
    server_address = (HOST, PORT)
    httpd = socketserver.TCPServer(server_address, MyHandler)
    print(f"Serving HTTP on {HOST} port {PORT} ...")
    httpd.serve_forever()