# PA3Server_Gonzalez_Houser_Pettit_Reed.py
# Marcus Gonzalez, Adam Houser, Jason Pettit, Colin Reed

# placeholder code below
from socket import *
from socket import socket
from _thread import *
import threading

serverPort = 12000

# Create a TCP socket
# Notice the use of SOCK_STREAM for TCP packets
serverSocket = socket(AF_INET,SOCK_STREAM)

# Assign IP address and port number to socket
serverSocket.bind(('',serverPort)) 
serverSocket.listen(1)
print ('The server is ready to receive')

while True:
    connectionSocket, addr = serverSocket.accept()
    sentence1 = connectionSocket.recv(1024).decode()
    #sentence2 = connectionSocket.recv(1024).decode()
    #capitalizedSentence = sentence1 + 'received before' + sentence2
    capitalizedSentence = sentence1 + ' received before '

    connectionSocket.send(capitalizedSentence.encode())
    connectionSocket.close()

    print('Sent acknowledgement to both X and Y')
