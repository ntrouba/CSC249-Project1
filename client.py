import sys
from socket import *

def main():
    #Creates client socket
    client_socket = socket(AF_INET,SOCK_STREAM)
    #Connects socket to server
    host = sys.argv[1]
    port = int(sys.argv[2])
    client_socket.connect((host, int(port)))
    client_socket.sendall(f'GET /{sys.argv[3]} HTTP/1.1\r\n\r\n'.encode())
    message = client_socket.recv(1024)
    while message:
        print(message.decode(), end="")
        message = client_socket.recv(1024)
    client_socket.close()
    
main()