# -*- coding:utf-8 -*-
import socket
import threading

def tcp_link(sock,addr):
    sock.send(b'hello I`m Sever!')
    while True:
        data = sock.recv(1024)
        if data.decode('utf-8') == 'exit' or not data:
            break
        else:
            sock.send(('u input %s' % data.decode('utf-8')).encode('utf-8'))
    sock.close()

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind(('127.0.0.1',9999))
s.listen(5)

while True:
    sock,addr = s.accept()
    t = threading.Thread(target=tcp_link,args=(sock,addr))
    t.start()