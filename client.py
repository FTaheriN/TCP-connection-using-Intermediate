import socket

serverName = '127.0.0.1'

#port number to send message to 
serverPort = 12000

while 1:
    
    #making a new TCP socket 
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientSocket.connect((serverName,serverPort))

    #getting input from user
    message = input("Input message:")

    #sending the message to intermediate
    clientSocket.send(message.encode('utf-8'))

    #getting the respond from intermediate
    ReplyMessage = clientSocket.recv(2048)

    #printing the reply message
    print ("From Server:", ReplyMessage.decode('utf-8'))

    if ReplyMessage.decode('utf-8') == "Bye. Have a great day...":
        break


#closing the TCP connection
clientSocket.close()
