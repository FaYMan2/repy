import socket
import time
serv = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

serv.connect(("localhost",6379))
serv.send(b'echo\r\nping haah!!')
print('sent ping')
res = serv.recv(512)
print(res.decode())
serv.shutdown(1)
serv.close()


serv1 = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serv1.connect(("localhost",6379))
serv1.send(b'set\r\nfoo\r\nbar\r\npx\r\n1000')
print('sent set')
res1 = serv1.recv(512)
print(res1.decode())
serv1.shutdown(1)
serv1.close()

time.sleep(2)

serv2 = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serv2.connect(("localhost",6379))
serv2.send(b'get\r\nfoo')
print('sent get')
res2 = serv2.recv(512)
print(res2.decode())
serv2.shutdown(2)
serv2.close()
