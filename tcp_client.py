# Description: Client side for TCP socket programming
# Author: Coleman Hill
# Date: September 28, 2021
import sys
from socket import *

# Declaring host/IP address
serverName = "localhost"
# port for connection
serverPort = 12000
# Creating socket
clientSocket = socket(AF_INET, SOCK_STREAM)

try:
    # Connecting socket
    clientSocket.connect((serverName, serverPort))
    # getting a message from the user
    message = ""
    #message = input("Enter a message: ")
    while message !=  "bye":
        message = input("Enter a message: ")
        # turning the string into bytes
        messageBytes = str.encode(message)
        # sending the message via socket
        clientSocket.send(messageBytes)
        # receiving message from server
        messageFromServerBytes = clientSocket.recv(1024)
        # printing the message and changing message from bytes to string
        print(bytes.decode(messageFromServerBytes), " from ", (serverName, serverPort))

    if message == "bye":
        clientSocket.close()
        sys.exit()
        #clientSocket.close()
# closing the socket
#clientSocket.close()
except gaierror as err:
    print("Invalid host")
    print(err)
    # sys.exit()

except OSError as err:
    print("Something went wrong", err)
clientSocket.close()
