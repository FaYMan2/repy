import socket
from cmds import command
from collections import deque
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
        self.events : deque[event] = deque([])
        self.firedEvents = []
        self.connectionCount : int  = 0
        self.serv : socket.socket = server
        self.store : dict[str:str] = {}
        
    def fireEvetnts(self):
        eventCopy = self.events.copy()
        for event in eventCopy:
            print(event.data)
            # WORK ON THE EVENT add it to the firedEvents
            cmd = command(rawCommand=event.data)
            cmd.decodeCommand()
            if cmd.type:
                if cmd.type == "echo":
                    event.conn.conn.send(f"${len(cmd.content)}\r\n{cmd.content}".encode())
                elif cmd.type == "set":
                    self.store[cmd.content[0]] = cmd.content[1:]
                    print('sending set foo bar response')
                    event.conn.conn.send(f"+OK\r\n".encode())
                elif cmd.type == "get":
                    data : str = self.store.get(cmd.content[0],-1)
                    if data != -1:
                        event.conn.conn.send(f"${len(data)}\r\n{data}".encode())
                    else:
                        event.conn.conn.send(f"-DATA NOT FOUND\r\n")
                        
            event.conn.conn.close()
            self.events.popleft()
                        
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
    
        

    
