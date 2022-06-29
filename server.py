from socket import *

#function to respond to client message 
def ServerReply(message):
    if message == "Salam Server":
        return "Hello client"
    elif message == "Chetorii?":
        return "I'm fine. How are you?"
    elif message == "Manam khobam":
        return "That's good!"
    elif message == "Kari nadari?":
        return "No"
    elif message == "Khoda Negahdar":
        return "Bye. Have a great day..."
    else :
        return "Can't undersatand"

#connection port for the UDP socket
serverPort = 8080
serverName = '127.0.0.1'

#making a new UDP socket (as server) to intract with the intermediate program
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind((serverName, serverPort))

print ("The server is ready to receive")
while 1:
    #receiving message from intermediate
    message, clientAddress = serverSocket.recvfrom(2048)
    
    #printing what has been received 
    print("server recive: ",message.decode('utf-8'))

    #calling function to reply to the message
    ans = ServerReply(message.decode('utf-8'))

    #printing reply
    print ("Server sending message--> ", ans)

    #sending reply to interpreter
    serverSocket.sendto(ans.encode('utf-8'), clientAddress)
