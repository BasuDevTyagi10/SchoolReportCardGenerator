from tkinter import *
import tkinter.messagebox
from res import *
from dashboard import *

def LoginScreen(frame):
    MainFrame = Frame(frame,height=WINDOWY,width=WINDOWX,bg=COLOR_SKYBLUE)
    MainFrame.place(x=0,y=0)
    InnerFrame = Canvas(MainFrame,height=WINDOWY-50,width=WINDOWX-50,bg=COLOR_STEELBLUE)
    InnerFrame.place(x=25,y=25)        
    frame.usericon = usericon = PhotoImage(file=USERIMAGE)
    InnerFrame.create_image((325,20),image=usericon,anchor=NW)

    LoginFrame = Frame(InnerFrame,height=200,width=300,bg=COLOR_WHITE,relief=RIDGE)
    LoginFrame.place(x=275,y=195)

    UserIDLabel = Label(LoginFrame,text="UserID",bg=COLOR_WHITE,font=ARIALBOLD10)
    UserIDLabel.place(x=40,y=40)
    PasswordLabel = Label(LoginFrame,text="Password",bg=COLOR_WHITE,font=ARIALBOLD10)
    PasswordLabel.place(x=40,y=80)

    UserIDEntry = Entry(LoginFrame,width=22,bd=2,relief=GROOVE)
    UserIDEntry.place(x=115,y=40)
    PasswordEntry = Entry(LoginFrame,width=22,show='*',bd=2,relief=GROOVE)
    PasswordEntry.place(x=115,y=80)

    PasswordEntry.bind("<Return>",lambda event: CheckLogin(frame,UserIDEntry.get(),PasswordEntry.get()))
    LogInButton = Button(LoginFrame,text='LOG IN',width=25,fg=COLOR_WHITE,bg=COLOR_SKYBLUE,
        font=ARIALBOLD10,relief=FLAT,command=lambda:CheckLogin(frame,UserIDEntry.get(),PasswordEntry.get()))
    LogInButton.place(x=40,y=130)

def CheckLogin(frame,userid,password):
    if(userid != '' and password != ''):
        cursor = DATABASECONNECTION.cursor()
        cursor.execute("SELECT * FROM {} WHERE {}='{}' and {}='{}'".format(ADMIN_DATABASE['tablename'],
            ADMIN_DATABASE['ColUserID'],userid,ADMIN_DATABASE['ColPassword'],password))
        result = cursor.fetchone()
        if(result!=None):
            DashboardScreen(frame,result)
        else:
            tkinter.messagebox.showerror(APPLICATIONNAME,"Invalid Username or Password")
    else:
        tkinter.messagebox.showerror(APPLICATIONNAME,"Invalid Username or Password")