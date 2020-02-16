from socket import *
from socket import socket
import threading
# Thread function
def thread_accept(index, message, lock, sockets):
    connectionSocket, addr = serverSocket.accept()  # accept a client connection
    sockets.append(connectionSocket)                # store client sockets
    #lock.acquire()                                  # acquire a lock to prevent simultaneous writes to message
    sentence = connectionSocket.recv(1024).decode() # sentence = Client X: Alice or Client Y: Bob
    message.append(sentence)                        # keep track of which sentence arrived first
    #lock.release()                                  # release the lock
# START SERVER SETUP
#Assign TCP port number
serverPort = 12000
# Create a TCP socket
# Notice the use of SOCK_STREAM for TCP packets
serverSocket = socket(AF_INET,SOCK_STREAM)
#Assign IP address and port number to socket
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print('The server is ready to receive')
#END SERVER SETUP
while True:
    sockets = list()        # keep track of the sockets to send our final message to
    threads = list()        # keep track of threads
    message = list()        # keep track of which message arrived first
    lock = threading.Lock() # lock to keep multiple clients from writing simultaneously
    # Start two threads
    for index in range(2):
        x = threading.Thread(target=thread_accept, args=(index,message,lock,sockets))
        threads.append(x)
        x.start()
    # Join two threads
    for index, thread in enumerate(threads):
        thread.join()
    print('Sent acknowledgement to both X and Y')

    for i in sockets:
        if message[0] == "Client X: Alice":
            returnSentence = "X: Alice received before Y: Bob"
        elif message[0] == "Client Y: Bob":
            returnSentence = "Y: Bob received before X: Alice"
        else:
            returnSentence = "Something weird happened"
        i.send(returnSentence.encode())
        i.close()