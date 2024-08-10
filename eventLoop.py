import socket

class connection:
    def __init__(self,connection,addr):
        self.addr = addr
        self.conncFd = connection
    
class eventLoop:
    def __init__(self,server : socket.socket):
        self.connections : list[connection] = []
        self.events = []
        self.firedEvents = []
        self.connectionCount : int  = 0
        self.serv : socket.socket = server
        
    def fireEvetnts(self):
        #for event in self.events:
        #    print(event)
        #    # WORK ON THE EVENT add it to the firedEvents
        #    self.firedEvents.append(event)
        for connection in self.connections:
            print(f'connected to : {connection.addr}')
            
def acceptIncommingConnections(loop : eventLoop):
    while True:
        conn,addr = loop.serv.accept()
        loop.connections.append(connection(conn,addr))
        loop.connectionCount += 1
        

