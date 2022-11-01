from socket import *
import sys
import time
import threading
from concurrent.futures import ThreadPoolExecutor

def thread(connectionSocket):
    try:
        message = connectionSocket.recv(1024)
        print(message)
        #Extracts the path of the requested object from the message
        filename = message.split()[1]
        #Reads the extracted path of the HTTP request from the second character
        f = open(filename[1:])
        #Stores contents of file in a temporary buffer
        outputdata = f.read()
        #Sends one HTTP header line into socket
        connectionSocket.send('HTTP/1.1 200 OK\r\n\r\n'.encode())
        
        #Sends contents of the file to client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        print("Close connection to client")
        connectionSocket.close()

    except IOError:
        #Sends response message for file not found
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n".encode()) 
        outputdata = "404 not found"
        #Sends error message to the client

        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        #Closes client socket
        connectionSocket.close()

def main(): 
    server_socket = socket(AF_INET, SOCK_STREAM)
    #Assigns a port number 
    socket_port = 1979
    #Binds the socket to server IP/server port
    server = "0.0.0.0"
    print(server)
    server_socket.bind((server, socket_port))
    server_socket.listen(10)
    print("Web server is running on port:", socket_port)
    threadExecutor = ThreadPoolExecutor()

    while True:
        #Confirms the connection
        print('Ready to serve...') 
        #Sets up a new connection from the client
        connectionSocket, addr = server_socket.accept()
        print("Accepting from:", addr)
        threadExecutor.submit(thread, connectionSocket)
        
    server_socket.close()
    sys.exit() 

if __name__=="__main__":
    main()