# PA3ClientX_Gonzalez_Houser_Pettit_Reed.py
# Marcus Gonzalez, Adam Houser, Jason Pettit, Colin Reed

from socket import *

# will want to change to host IP for mininet use
# specify host name and port for easier readability
serverName = 'Localhost'
serverPort = 12000

#create socket and set timeout
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))

# message sent to server
sentence = 'Client X: Alice'

# send message to server
clientSocket.send
clientSocket.send(sentence.encode())

# indicate that the message has been sent to the server
print ('To Server: ' + sentence)

# receive message from the server
modifiedSentence = clientSocket.recv(1024)
print ('From Server:', modifiedSentence.decode())
clientSocket.close()
