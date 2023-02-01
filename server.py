#!/usr/bin/env python3
"""TCP server that accepts and holds a maximum of N clients
"""
import socket
import random

HOST = socket.gethostbyname(socket.gethostname())
PORT = random.randint(5010, 5090)


server = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)

server.bind((HOST, PORT))
server.listen()

connection, address = server.accept()
print(PORT)
print(HOST)
print("{} {}".format(connection, address))

socket.close()
