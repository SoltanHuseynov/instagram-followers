from tkinter import*
import time


class window_insta:
    def __init__(self):
        self.window3=Tk()
        self.window3.title("insta_Reg")
        self.window3.geometry("240x340")
        self.window3.resizable(False,False)
        self.window3.iconbitmap(True,"image\\admin.ico")

        #Email
        self.lab1=Label(self.window3,text="Email",font=("bold",10,"italic"),fg="#3897f0")
        self.lab1.place(relx=0.1)
        self.gmail=Entry(self.window3,font="bold",bd=0.6)
        self.gmail.place(relx=0.1,rely=0.1)


        #surname
        self.lab2=Label(self.window3,text="Name and Surname",font=("bold",10,"italic"),fg="#3897f0")
        self.lab2.place(relx=0.1,rely=0.2)
        self.name=Entry(self.window3,font="bold",bd=0.6)
        self.name.place(relx=0.1,rely=0.3)


        #username
        self.lab3=Label(self.window3,text="Username",font=("bold",10,"italic"),fg="#3897f0")
        self.lab3.place(relx=0.1,rely=0.4)
        self.username=Entry(self.window3,fon="bold",bd=0.6)
        self.username.place(relx=0.1,rely=0.5)


        #Password
        self.lab4=Label(self.window3,text="Password",font=("bold",10,"italic"),fg="#3897f0")
        self.lab4.place(relx=0.1,rely=0.6)
        self.password=Entry(self.window3,font="bold",show="*",bd=0.6)
        self.password.place(relx=0.1,rely=0.7)
 
        # Register
        self.but=Button(self.window3,text="Register",bg="#3897f0",fg="red",width=25,height=2,command=self.server)
        self.but.place(relx=0.1,rely=0.8)
        
    
    def server(self):
        Email=self.gmail.get()
        Surname=self.name.get()
        Use=self.username.get()
        Password=self.password.get()



        

        
