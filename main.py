import socket
from eventLoop import eventLoop
from eventLoop import acceptIncommingConnections
from _thread import start_new_thread
import asyncio
from argparse import ArgumentParser
def stillConnected(connection):
    try:
        connection.send(b'')
        return True
    except:
        return False
    
def main():
    parser = ArgumentParser("Redis server---;)")
    parser.add_argument("--port",type=int,default=6379)
    servSock = socket.create_server(("localhost",parser.parse_args().port))
    loop = eventLoop(server=servSock,role="master")
    while True:
        #print(f'no connected = {loop.connectionCount}')
        acceptIncommingConnections(loop)
        if loop.connectionCount:
            loop.fireEvetnts()
            print(loop.events)

if __name__ == "__main__":
    main()