# from socket import *
# import sys

# server_host = sys.argv[1]
# server_port = sys.argv[2]
# filename = sys.argv[3]

# host_port = "%s:%s" %(server_host, server_port)
# try:
# 	client_socket = socket(AF_INET,SOCK_STREAM)
# 	client_socket.connect((server_host,int(server_port)))
# 	header = {
# 	"first_header" : "GET /%s HTTP/1.1" %(filename),
# 	"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
# 	"Accept-Language": "en-us",
# 	"Host": host_port,
# 	}
# 	http_header = "\r\n".join("%s:%s" %(item,header[item]) for item in header)
# 	print (http_header)
# 	client_socket.send("%s\r\n\r\n" %(http_header))

# except IOError:

# 	sys.exit(1)
# final=""
# response_message=client_socket.recv(1024)
# while response_message:
# 	final += response_message
# 	response_message = client_socket.recv(1024)

# client_socket.close()
# print ("final:"), final

import sys
from socket import *


def main():
    #create client socket to send out requests on
    clientSocket = socket(AF_INET,SOCK_STREAM)
    #make socket and address dynamic later
    #connect the socket to the server
    host = sys.argv[1]
    port = int(sys.argv[2])
    clientSocket.connect((host, int(port)))
    clientSocket.sendall(f'GET /{sys.argv[3]} HTTP/1.1\r\n\r\n'.encode())
    message = clientSocket.recv(1024)
    while message:
        print(message.decode(), end="")
        message = clientSocket.recv(1024)

    clientSocket.close()
    


main()