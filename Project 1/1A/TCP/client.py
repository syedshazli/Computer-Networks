# the protocol should be as follows:
    # 1. Client reads data from its keyboard and sends data to server
    # 2. Server receives data and converts chars to uppercase
    # 3. Server sends modified data to client
    # 4. Client receives modified data and displays like on its screen

#  The following system calls are allowed on a TCP socket: 
#       Close(), Bind(), Accept(), Connect(), Write(), Read(), and Setsockopt(). 
#       So no using sendto or recvfrom

from socket import *
# must read socket man page
serverPort = 7077
HOST = '127.0.0.1'


# Now, connect to the server via socket system call
# "The Socket() call accepts three arguments: family, type, and protocol"

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((HOST,serverPort))
# How user input works in python:
    # username = input("Enter username:")

# get message from user
userMessage = input('Enter lowercase sentence:')
userMessage = userMessage.encode("UTF-8")



# send message to server
clientSocket.sendall(userMessage)

message = clientSocket.recv(2048)

if not message:
    print("We couldn't get the message properly, please try again")
else:
    message = message.decode()
    print(message)

# close client socket

clientSocket.close()
