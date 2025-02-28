#please note that you only need to run the server on your local host, or on a different device on the same local network as the client. The wpi server will not allow you to have a port open for test. 

import sys, time
from datetime import datetime
from socket import *

# Get the server hostname and port as command line arguments
#fill in start
if len(sys.argv) <= 2:
    print('Usage : "python UDPPingerClient.py serverPort serverName "\n')
    sys.exit(2)

# use argv[1] to get server hostname
# use argv[2] to get server port
serverPort = sys.argv[2]
serverHost = sys.argv[1] # may have to encode serverHost with .encode()



#fill in end

timeout = 1 # in second
 
# Create UDP client socket, note the use of SOCK_DGRAM for UDP datagram packet
#fill in start
clientSocket = socket(AF_INET, SOCK_DGRAM)
#fill in end

# Set socket timeout as specified
#fill in start
clientSocket.settimeout(1) # sets 1 second timeout
#fill in end
# Command line argument is a string, change the port into integer
#fill in start
serverPort = int(serverPort)
#fill in end

# Sequence number of the ping message
ptime = 0  

# Ping for 10 times
while ptime < 10: 
    ptime += 1
    # Format the message to be sent
    #fill in start
    userMessage = input('Enter the message you would like to send: ')
    userMessage.encode('UTF-8')
    #fill in end   

    try:
	# Get the message sent time
        #fill in start
        messageSentTime = time.time()
	#fill in end
	# Send the UDP packet with the ping message
        #fill in start
        
        clientSocket.sendto(userMessage.encode(), (serverHost, serverPort))
        print("Ping #",ptime)
	#fill in end
	# Receive the server response
        #fill in start
        serverMessage, address = clientSocket.recvfrom(serverPort) # check if it should be serverHost
	#fill in end
	# Get Received time
        messageReceivedTime = time.time()
        
        #fill in start
	#fill in end
	# Display the server response as an output
     
	#fill in start
        print("Server response: ", serverMessage.decode())
	#fill in end
	# Round trip time is the difference between sent and received time
	#fill in start
        roundTrip = messageReceivedTime-messageSentTime
        current_datetime = datetime.now()

        # Format the datetime object as a string
        formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
        print(formatted_datetime)
        print("Round trip time: ", roundTrip, " seconds")
	#fill in end
    except:
        print("The packet was lost. Sending over the packet again.")
        # Server does not response, and assume the packet is lost
        # we must send the packet again??
        messageSentTime = time.time()
        clientSocket.sendto(userMessage.encode(), (serverHost, serverPort))
        serverMessage, address = clientSocket.recvfrom(serverPort)
        messageReceivedTime = time.time()
        print("Server response: ", serverMessage.decode())
        roundTrip = messageReceivedTime-messageSentTime
        # Format the datetime object as a string
        formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
        print(formatted_datetime)
        print("Round trip time: ", roundTrip, " seconds")
        continue
        
	#fill in start
     
	#fill in end
	    

# Close the client socket
#fill in start
clientSocket.close()
#fill in end 
