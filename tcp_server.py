#Description: Server side for TCP socket programming
#Author: Coleman Hill
#Date: September 28, 2021
import sys
from socket import *
#Creating the serverName or IP address
serverName = "localhost"
#Creating the port we will connect with
serverPort = 12000
#Creating socket
serverSocket = socket(AF_INET,SOCK_STREAM)
#Assigns IP address and port number to a sockets
serverSocket.bind((serverName,serverPort))
#Socket that will be used to accept incoming connection request
serverSocket.listen(1)
#Print statement saying the server is ready to receive
print("Server is ready to receive")
#continue looping
while True:
    #waits for accept for incoming requests
    connectionSocket, clientAddress = serverSocket.accept()
    #read bytes from socket
    messageFromClientBytes = ""
    messageFromClientBytes = connectionSocket.recv(1024)

    while messageFromClientBytes != "bye":
        #print(messageFromClientBytes, " from ", clientAddress)
        #print(messageFromClientBytes," from ",clientAddress)
        if bytes.decode(messageFromClientBytes) == "bye":
            #testing
            print("The client has quit.")
            print("Connection socket is closed.")
            connectionSocket.close()
            break
            #sys.exit()
        else:
            print(messageFromClientBytes, " from ", clientAddress)
            messageToClientBytes = messageFromClientBytes.upper()
            #sending upper case message to client side
            connectionSocket.send(messageToClientBytes)
            messageFromClientBytes = connectionSocket.recv(1024)


