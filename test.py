import socket

serv = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

serv.connect(("localhost",6379))
serv.send(b'echo\r\npint haah!!')
res = serv.recv(512)
print(res)