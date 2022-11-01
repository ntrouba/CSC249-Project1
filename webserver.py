# from socket import *
# import sys # In order to terminate the program
# import datetime

# serverSocket = socket(AF_INET, SOCK_STREAM)

# # -------------
# # Fill in start
# # -------------
# serverHost='localhost'
# serverPort= 80
# serverSocket.bind(('',serverPort))
# serverSocket.listen(1)


#   # TODO: Assign a port number
#   #       Bind the socket to server address and server port
#   #       Tell the socket to listen to at most 1 connection at a time

# # -----------
# # Fill in end
# # -----------

# while True:
    
#     # Establish the connection
#     print('Ready to serve...') 
    
#     # -------------
#     # Fill in start
#     # -------------
#     connectionSocket, addr = serverSocket.accept() # TODO: Set up a new connection from the client
#     # -----------
#     # Fill in end
#     # -----------

#     try:
        
#         # -------------
#         # Fill in start
#         # -------------
#         message = connectionSocket.recv(1024).decode() # TODO: Receive the request message from the client
       
#         message.split()[1]
         
#         # -----------
#         # Fill in end
#         # -----------
        
#         # Extract the path of the requested object from the message
# 		# The path is the second part of HTTP header, identified by [1]
#         filename = message.split()[1]

#         # Because the extracted path of the HTTP request includes 
# 		# a character '\', we read the path from the second character
#         f = open(filename[1:])
        
#         # -------------
#         # Fill in start
#         # -------------
#         outputdata = f.read() # TODO: Store the entire contents of the requested file in a temporary buffer
#         print ("outputdata:"), outputdata
#         now = datetime.datetime.now()

        
#         # -----------
#         # Fill in end
#         # -----------

#         # -------------
#         # Fill in start
#         # -------------
#             # TODO: Send one HTTP header line into socket
#         first_header = "HTTP/1.1 200 OK"

#         header_info = {
# 			"Date": now.strftime("%Y-%m-%d %H:%M"),
# 			"Content-Length": len(outputdata),
# 			"Keep-Alive": "timeout=%d,max=%d" %(10,100),
# 			"Connection": "Keep-Alive",
# 			"Content-Type": "text/html"
# 		}
		
#         following_header = "\r\n".join("%s:%s" % (item, header_info[item]) for item in header_info)
#         print ("following_header:"), following_header
#         connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode())
#         connectionSocket.send(outputdata.encode())
        
#         # -----------
#         # Fill in end
#         # -----------

#         # Send the content of the requested file to the client
#         for i in range(0, len(outputdata)):
#             connectionSocket.send(outputdata[i].encode())
#             connectionSocket.send("\r\n".encode())
            
        

#         connectionSocket.close()

#     except IOError:
#         # -------------
#         # Fill in start
#         # -------------
#             # TODO: Send response message for file not found
#             #       Close client socket
#         connectionSocket.send('\nHTTP/1.1 404 Not Found\n\n'.encode())
#         print ("404 Page Not Found")
#         # -----------
#         # Fill in end
#         # -----------

# serverSocket.close()
# sys.exit()  #Terminate the program after sending the corresponding data
#Import socket module

# from socket import *

# import socket # Alternative (better) syntax

# # Create a TCP server socket

# #(AF_INET is used for IPv4 protocols)

# #(SOCK_STREAM is used for TCP)

# # serverSocket = socket(AF_INET, SOCK_STREAM)

# serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Alternative (better) syntax

# # Assign a port number

# serverPort = 80

# # Bind the socket to server address and server port

# serverSocket.bind(("", serverPort))

# # or

# # serverSocket.bind((gethostname(), serverPort))

# # serverSocket.bind((socket.gethostname(), serverPort)) # Alternative (better) syntax

# # Listen to at most 1 connection at a time

# serverSocket.listen(1)

# # Server should be up and running and listening to the incoming connections

# while True:

#     print ('Ready to serve...')

    

#     # Set up a new connection from the client

#     connectionSocket, addr = serverSocket.accept()

    

#     # If an exception occurs during the execution of try clause

#     # the rest of the clause is skipped

#     # If the exception type matches the word after except

#     # the except clause is executed

#     try:

#         # Receives the request message from the client

#         message = connectionSocket.recv(1024).decode()

#         print ('Message is: '), message

#         # Extract the path of the requested object from the message

#         # The path is the second part of HTTP header, identified by [1]

#         filename = message.split()[1]

#         print ('File name is: '), filename

#         # Because the extracted path of the HTTP request includes

#         # a character '/', we read the path from the second character

#         f = open(filename[1:])

#         # Store the entire contenet of the requested file in a temporary buffer

#         outputdata = f.read()

#         # Send the HTTP response header line to the connection socket

#         connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode())

#         # Send the content of the requested file to the connection socket

#         for i in range(0, len(outputdata)):

#             connectionSocket.send(outputdata[i].encode())

#         connectionSocket.send("\r\n".encode())

        

#         # Close the client connection socket

#         connectionSocket.close()

#     except IOError:

#         # Send HTTP response message for file not found

#         connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n".encode())

#         connectionSocket.send("<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n".encode())

#         # Close the client connection socket

#         connectionSocket.close()

# serverSocket.close()
from socket import *
import sys # In order to terminate the program
import time
import threading
from concurrent.futures import ThreadPoolExecutor



# socket.recv(bufsize[, flags]) Receive data from the socket. The return value is a bytes object representing the data received. The maximum amount of data to be received at once is specified by bufsize. Bufszie 1024 - relatively small power of 2. (docs.python.org) 
      # decode converts from byte object to string
def one_thread(connectionSocket):
    try:
        message = connectionSocket.recv(1024)
        print(message)
        # -----------
        # Fill in end
        # -----------
        
        # Extract the path of the requested object from the message
        # The path is the second part of HTTP header, identified by [1]
        filename = message.split()[1]

        # Because the extracted path of the HTTP request includes 
            # a character '\', we read the path from the second character
        f = open(filename[1:])
    
        # -------------
        # Fill in start
        # -------------
        outputdata = f.read()
        # TODO: Store the entire contents of the requested file in a temporary buffer
        
        # -----------
        # Fill in end
        # -----------

        # ------------
        # Fill in start
        # -------------
        # TODO: Send one HTTP header line into socket
        connectionSocket.send('HTTP/1.1 200 OK\r\n\r\n'.encode())
        # -----------
        # Fill in end
        # -----------

        # Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        print("Close connection to client")
        connectionSocket.close()
    except IOError:
        # -------------
        # Fill in start
        # -------------
        # TODO: Send response message for file not found
        #       Close client socket
        #\r\n is new line for text formats on the internet
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n".encode())
        # create output data for the error message 
        outputdata = "404 not found"
        # Send the content of the error message to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.close()

def main(): 
    serverSocket = socket(AF_INET, SOCK_STREAM)
      # TODO: Assign a port number 
    socketPort = 1979
      #       Bind the socket to server IP address and server port (IP address is server's current IP address)
    server = "0.0.0.0"
      # Print so we can see the IP address to enter the link into browser
    print(server)
    serverSocket.bind((server, socketPort))
      #       Tell the socket to listen to at most 1 connection at a time with listen func and param 1
    serverSocket.listen(10)
    print("The web server is up on port:", socketPort)
    executor = ThreadPoolExecutor()

    while True:
        
        # Establish the connection
        print('Ready to serve...') 
        
      # TODO: Set up a new connection from the client
      # The socket must be bound to an address and listening for connections. The return value is a pair (conn, address) where conn is a new socket object usable to send and receive data on the connection, and address is the address bound to the socket on the other end of the connection. (docs.python.org)
        connectionSocket, addr = serverSocket.accept()
        print("Accepting from:", addr)
        executor.submit(one_thread, connectionSocket)
        # TODO: Receive the request message from the client

    serverSocket.close()
    sys.exit()  #Terminate the program after sending the corresponding data

if __name__=="__main__":
    main()