import socket
from cmds import command
class connection():
    def __init__(self,conn : socket.socket,addr : tuple[str,int]):
        self.conn = conn
        self.addr = addr

class event():
    def __init__(self,conn : connection, data : str) -> None:
        self.conn = conn
        self.data = data
class eventLoop:
    def __init__(self,server : socket.socket):
        self.connections : list[connection] = []
        self.events : list[event] = []
        self.firedEvents = []
        self.connectionCount : int  = 0
        self.serv : socket.socket = server
        
    def fireEvetnts(self):
        for event in self.events:
            print(event.data)
            # WORK ON THE EVENT add it to the firedEvents
            cmd = command(rawCommand=event.data)
            cmd.decodeCommand()
            if cmd.type :
                if cmd.type == "echo":
                    event.conn.conn.send(f"{len(cmd.content)}\r\n{cmd.content}".encode())
                    
        for connection in self.connections:
            print(f'connected to : {connection.addr}')
            
def acceptIncommingConnections(loop : eventLoop):
    while True:
        conn,addr = loop.serv.accept()
        loop.connections.append(connection(conn = conn,addr = addr))
        loop.connectionCount += 1
        
def getIncommingEvents(loop : eventLoop):
    if loop.connectionCount > 0:
        for connection in loop.connections:
            data = connection.conn.recv(1028)
            loop.events.append(event(connection,data.decode()))
    
        
