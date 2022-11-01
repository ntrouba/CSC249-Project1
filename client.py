import sys
from socket import *

def main():
    #Creates client socket
    clientSocket = socket(AF_INET,SOCK_STREAM)
    #Connects socket to server
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