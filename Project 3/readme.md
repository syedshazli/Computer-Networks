Here are steps to run the program

1. Make sure UDPPingerClient.py & UDPPingerServer.py are in the same directory

2. Run the Server file by entering 'Python UDPPingerServer.py'

3. Run the Client file by entering the hostname and port you would like to connect to. 
   The server code specifies port 12000, so you can enter the following: python UDPPingerClient.py 127.0.0.1 120000

4. The client will prompt you to enter messages to send for the server to capitalise. 

    a. If the packet is dropped, you will see that the packet is dropped in the output via a message
    b. Otherwise you will be able to see the ping number, the server response with the message capitalised, round trip time, and time the ping was sent

5. Once you send 10 messages, the client will terminate, and the server will stay on.
