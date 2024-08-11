import socket
from eventLoop import eventLoop
from eventLoop import acceptIncommingConnections
from _thread import start_new_thread
import asyncio
def stillConnected(connection):
    try:
        connection.send(b'')
        return True
    except:
        return False
    
def main():
    servSock = socket.create_server(("localhost",6379))
    loop = eventLoop(server=servSock)
    while True:
        #print(f'no connected = {loop.connectionCount}')
        acceptIncommingConnections(loop)
        if loop.connectionCount:
            loop.fireEvetnts()
            print(loop.events)

if __name__ == "__main__":
    main()