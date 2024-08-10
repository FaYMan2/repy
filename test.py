import socket

serv = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

serv.connect(("localhost",6379))
serv.send(b'ping haha !!!')
