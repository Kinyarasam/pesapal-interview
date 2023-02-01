#!/usr/bin/env python3
"""TCP server that accepts and holds a maximum of N clients
"""
import socket
import random

# Standard loopback interface address (localhost)
HOST = socket.gethostbyname(socket.gethostname())
# port to listen on (non-priveleged ports are > 1023)
PORT = random.randint(5010, 5090)


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind((HOST, PORT))
    server.listen()
    print("[+] OK: Server started on port: {}".format(PORT))

    print("[+] OK: Listening . . .")

    connection, address = server.accept()

    with conn:
        print("Connected by {}".format(address))
