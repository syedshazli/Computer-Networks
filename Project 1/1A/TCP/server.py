# the protocol should be as follows:
    # 1. Client reads data from its keyboard and sends data to server
    # 2. Server receives data and converts chars to uppercase
    # 3. Server sends modified data to client
    # 4. Client receives modified data and displays like on its screen

# use the .upper() method for this in python
from socket import *

serverPort = 7077
serverhost = ''
# pass AF_INET and SOCK_STREAM to specify TCP
serverSocket = socket(AF_INET, SOCK_STREAM)

# only bind on server side, not client side.
serverSocket.bind((serverhost, serverPort))

print("The server has connected with the client")

serverSocket.listen()

connection, address = serverSocket.accept()

while True:
    message = connection.recv(2048)
    message = message.upper()
    connection.sendall(message)

