import socket
from cmds import command
from collections import deque,defaultdict
import time
class connection():
    def __init__(self,conn : socket.socket,addr : tuple[str,int]) -> None:
        self.conn = conn
        self.addr = addr

class event():
    def __init__(self,conn : connection, data : str) -> None:
        self.conn = conn
        self.data = data
class eventLoop:
    def __init__(self,server : socket.socket,role : str):
        self.events : deque[event] = deque([])
        self.firedEvents = []
        self.connectionCount : int  = 0
        self.serv : socket.socket = server
        self.store : dict[str:str] = {}
        self.expiry : dict = defaultdict(int)
        self.role : str = role
    def fireEvetnts(self):
        eventCopy = self.events.copy()
        for event in eventCopy:
            print(event.data)
            # WORK ON THE EVENT add it to the firedEvents
            cmd = command(rawCommand=event.data)
            cmd.decodeCommand()
            print(f'expiry : {cmd.expiry}')
            if cmd.type:
                if cmd.type == "echo":
                    event.conn.conn.send(f"${len(cmd.content)}\r\n{cmd.content}".encode())
                elif cmd.type == "set":
                    self.store[cmd.content[0]] = cmd.content[1:]
                    if cmd.expiry:
                        self.expiry[cmd.content[0]] = time.time() * 1000 + int(cmd.expiry)
                    event.conn.conn.send(f"+OK\r\n".encode())
                elif cmd.type == "get":
                    if cmd.content[0] in self.expiry and (time.time() * 1000) - self.expiry[cmd.content[0]] < 0:
                       # print(f'expiry of get : {self.expiry[cmd.content[0]]}\n current time : {time.time() * 1000}\ndifference : {(time.time() * 1000) - self.expiry[cmd.content[0]]}')
                        data : list[str] = self.store.get(cmd.content[0],-1)
                        if data != -1:
                            event.conn.conn.send(f"${len(data)}\r\n{data}".encode())
                        else:
                            event.conn.conn.send(f"-DATA NOT FOUND\r\n".encode())
                    else:
                        del self.store[cmd.content[0]]
                        del self.expiry[cmd.content[0]]
                        event.conn.conn.send(b"-Data expired")
                elif cmd.type == "INFO":
                    event.conn.conn.send(f'+INFO\r\nROLE : {self.role}'.encode())
            event.conn.conn.shutdown(1)
            event.conn.conn.close()
            self.connectionCount -= 1
            self.events.popleft()
    
def acceptIncommingConnections(loop : eventLoop):
    conn,addr = loop.serv.accept()
    data : bytes = conn.recv(512)
    connData = connection(conn = conn,addr = addr)
    loop.events.append(event(connData,data.decode()))
    loop.connectionCount += 1
        

    
        

    
