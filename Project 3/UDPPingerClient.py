#please note that you only need to run the server on your local host, or on a different device on the same local network as the client. The wpi server will not allow you to have a port open for test. 

import sys, time
from socket import *

# Get the server hostname and port as command line arguments
#fill in start
if len(sys.argv) <= 2:
    print('Usage : "python UDPPingerClient.py serverPort serverName "\n')
    sys.exit(2)

# use argv[1] to get server port
# use argv[2] to get server hostname
serverPort = sys.argv[1]
serverHost = sys.argv[2] # may have to encode serverHost with .encode()


#fill in end

timeout = 1 # in second
 
# Create UDP client socket, note the use of SOCK_DGRAM for UDP datagram packet
#fill in start
clientSocket = socket(AF_INET, SOCK_DGRAM)
#fill in end
# Set socket timeout as specified
#fill in start
#fill in end
# Command line argument is a string, change the port into integer
#fill in start
#fill in end

# Sequence number of the ping message
ptime = 0  

# Ping for 10 times
while ptime < 10: 
    ptime += 1
    # Format the message to be sent
    #fill in start
    #fill in end   

    try:
	# Get the message sent time
        #fill in start
	#fill in end
	# Send the UDP packet with the ping message
        #fill in start
	#fill in end
	# Receive the server response
        #fill in start
	#fill in end
	# Get Received time
        #fill in start
	#fill in end
	# Display the server response as an output
	#fill in start
	#fill in end
	# Round trip time is the difference between sent and received time
	#fill in start
	#fill in end
    except:
        # Server does not response, and assume the packet is lost
	#fill in start
	#fill in end
	continue

# Close the client socket
#fill in start
#fill in end 
