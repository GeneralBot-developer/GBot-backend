import socket
from logging import getLogger, config, basicConfig, INFO
import json

json_open = open('config/log_config.json', 'r')
log_conf = json.load(json_open)
config.dictConfig(log_conf)
basicConfig(level=INFO)
LOG = getLogger(__name__)


class SocketServer:
    def __init__(self):
        self.ip_address = '127.0.0.1'
        self.port = 7010
        self.buffer_size = 4092

    def start(self):
        LOG.info("SocketServer is online.")
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.ip_address, self.port))
            s.listen(5)
            LOG.info("Request waiting.")
            while True:
                # 要求があれば接続の確立とアドレス、アドレスを代入
                conn, address = s.accept()
                # データを受信する
                data = conn.recv(self.buffer_size)
                print('data-> {}, address->{}'.format(data, address))
                # データを送信する
                conn.sendall(b'test')
