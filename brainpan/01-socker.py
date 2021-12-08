#!/usr/bin/python3
#_*_ coding: utf8 _*_
#@JoshuaProvoste

import socket,argparse

"""
Project repository: https://github.com/JoshuaProvoste/Stack-Buffer-Overflow-Python-Toolkit 
"""

parser = argparse.ArgumentParser()
parser.add_argument("-ip","--host", type=str, required=True, help="IP host to pwn")
parser.add_argument("-sp","--port", type=int, required=True, help="Port of vulnerable service")
args = parser.parse_args()

try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((args.host,args.port))
    print(sock.recv(1024).decode("utf-8"))
    command = input("Command: ")
    command_encoded = command.encode("utf-8") 
    sock.send(command_encoded)
    for a in sock.recv(1024).decode("utf-8").split("\n"):
        print(a)
    else:
        sock.close()
        print("\nConnection closed. Bye!")
        exit()
except socket.error:
    sock.close()
    print("Connection error. Review the IP address or port.")
    exit()
except socket.timeout:
    sock.close()
    print("\nConnection error. Timeout!")
    exit()
except KeyboardInterrupt:
    sock.close()
    print("\n\nConnection closed. Bye!")
    exit()