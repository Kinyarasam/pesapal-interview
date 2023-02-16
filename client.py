#!/usr/bin/env python3
"""Simple client connection
"""
import socket

HOSTNAME = socket.gethostname()
# Standard loopback interface address (localhost)
HOST = socket.gethostbyname(HOSTNAME)
PORT = 5040 # Same port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((HOST, PORT))
    client.sendall(b"Hello")

    data = client.recv(1024)

print("Received {}".format(data))
