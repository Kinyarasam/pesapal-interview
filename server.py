#!/usr/bin/env python3
"""TCP server that accepts and holds a maximum of N clients
"""
import socket
import random


# Standard loopback interface address (localhost)
HOST = socket.gethostbyname(socket.gethostname())
# port to listen on (non-priveleged ports are > 1023)
PORT = 5010


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind((HOST, PORT))
    server.listen()
    print("[+] OK: Server started on port: {}".format(PORT))

    print("[+] OK: Listening . . .")

    connection, address = server.accept()


    with connection:
        print("\t[+] Connected by {}".format(address))
        while True:
            data = connection.recv(1024)
            if not data:
                print("\t[-] No Data Found")
                break

            connection.sendall(data)
