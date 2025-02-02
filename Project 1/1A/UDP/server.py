
# the protocol should be as follows:
    # 1. Client reads data from its keyboard and sends data to server
    # 2. Server receives data and converts chars to uppercase
    # 3. Server sends modified data to client
    # 4. Client receives modified data and displays like on its screen

# use the .upper() method for this in python
from socket import *

serverPort = 7070

# pass AF_INET and SOCK_DGRAM to specify UDP
serverSocket = socket(AF_INET, SOCK_DGRAM)

# only bind on server side, not client side.
serverSocket.bind("", serverPort)


