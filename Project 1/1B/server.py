
#Programming Assignment 1B: Web Server

#import socket module
from socket import *
serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a sever socket


serverPort = 8090
serverHost = ''
serverSocket.bind((serverHost, serverPort))

print("The server has connected with the client")

serverSocket.listen()



while True:
    #Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()

    try:
        message = connectionSocket.recv(2048).decode() 
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read() # read the file, set the contents to outputdata for printing
        print(outputdata)

        #Send one HTTP header line into socket
        connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode())


        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.close()

    except IOError:
        #Send response message for file not found
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n".encode())
        connectionSocket.send("<html><body><h1>404: File Not Found</h1></body></html>".encode())
        # close client socket
        connectionSocket.close()
        
        
# never reached, but good practice nonetheless
serverSocket.close()
