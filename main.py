import socket
from eventLoop import eventLoop
from eventLoop import acceptIncommingConnections,getIncommingEvents
from _thread import start_new_thread

def stillConnected(connection):
    try:
        connection.send(b'')
        return True
    except:
        return False
    
def main():
    servSock = socket.create_server(("localhost",6379))
    loop = eventLoop(server=servSock)
    start_new_thread(acceptIncommingConnections,(loop,))
    while True:
        #print(f'no connected = {loop.connectionCount}')
        getIncommingEvents(loop)
        if loop.connectionCount:
            loop.fireEvetnts()
            break

if __name__ == "__main__":
    main()