import socket
import sys
import threading

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# JonydeMacBook-Pro.local
host = socket.gethostname()

port = 9994

serversocket.bind((host, port))

MAX_CONNECT = 3

serversocket.listen(MAX_CONNECT)

# class Client:
#     def __init__(self, clientsocket, addr):
#         self.socket = clientsocket
#         self.addr = addr

#     def startRecv:
#         HandleClientMsgThread 

class HandleClientMsgThread (threading.Thread):
    def __init__(self, socket, addr):
        threading.Thread.__init__(self)
        ip,port = addr
        self.name = str(port)
        self.socket = socket
    def run(self):
        while True:
            msg = self.socket.recv(1024)
            print(self.name, msg.decode('utf-8'))
            returnMsg = 'recv success'
            self.socket.send(returnMsg.encode('utf-8'))
    
      

while True:
    print('listing:%s' % socket.gethostbyname(host))
    clientsocket,addr = serversocket.accept()
    print('连接地址:%s' % str(addr))

    HandleClientMsgThread(clientsocket, addr).start()
    # msg = 'Hello, '+ str(addr)
    # clientsocket.send(msg.encode('utf-8'))
    # clientsocket.close()

# print(host)
# print(socket.gethostbyname(host))

