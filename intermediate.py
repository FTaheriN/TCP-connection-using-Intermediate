import socket
from socket import AF_INET, SOCK_STREAM

#port that receives data from client --> listening TCP
serverPort = 12000
#port that sends data to server --> UDP
serverPort1 = 8080

serverName = '127.0.0.1'

#TCP socket for client connection
serverSocket = socket.socket(AF_INET,SOCK_STREAM)
serverSocket.bind((serverName,serverPort))
serverSocket.listen(1)
print ("The server is ready to receive")

while 1:
    # as it is a TCP socket, it must first accept the connection request
    connectionSocket, addr = serverSocket.accept()
    # allowed to receive up to 1024 bit message
    ClientMessage = connectionSocket.recv(2048)

    # printing what has been received from client
    print ("message from client--> " ,ClientMessage.decode('utf-8'))

    # making a new UDP socket to intract with server
    clientSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    #sending the message received from client to server
    clientSocket.sendto(ClientMessage,(serverName, serverPort1)) 

    #getting a response from server
    ServerResponse, serverAddress = clientSocket.recvfrom(2048)

    # pringting what has been received from the server
    print ("send to client--> ",ServerResponse)

    # sending the message as a responce to client
    connectionSocket.send(ServerResponse)

    #closing TCP connection with the client
    connectionSocket.close()
