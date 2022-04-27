#!/usr/bin/python3

import socket

client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '192.168.0.30'
#client needs to know IP address of server

port = 444 
#must match server port

#connecting to port
client_sock.connect(host, port)

#set max data allowed to be transmitted
message = client_sock.recv(1024)

client_sock.close()

print(message.decode('ascii'))