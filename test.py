import socket

serv = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

serv.connect(("localhost",6379))
serv.send(b'echo\r\nping haah!!')
print('sent ping')
res = serv.recv(512)
print(res.decode())

serv.connect(("localhost",6379))
serv.send(b'set\r\nfoo\r\nbar')
print('sent set')
res1 = serv.recv(512)
print(res1.decode())

serv.connect(("localhost",6379))
serv.send(b'get\r\nfoo')
print('sent get')
res2 = serv.recv(512)
print(res2.decode())


serv.close()
