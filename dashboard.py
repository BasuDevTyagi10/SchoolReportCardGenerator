from tkinter import *
from res import *
import login
from frontend import *

def DashboardScreen(frame,result):
    BackgroundFrame1 = Frame(frame,height=500,width=900,bg=COLOR_WHITE)
    BackgroundFrame1.place(x=0,y=0)
    TitleBackgroundFrame = Frame(frame,bg=COLOR_STEELBLUE,height=80,width=900)
    TitleBackgroundFrame.place(x=0,y=0)

    TitleLabelHeading = Label(TitleBackgroundFrame,text='REPORT CARD MANAGEMENT SYSTEM',fg=COLOR_WHITE,bg=COLOR_STEELBLUE,font=ARIALBOLD30)
    TitleLabelHeading.place(x=60,y=17)

    CurrentUserLabelHeading=Label(frame,text="Current User : ",bg=COLOR_WHITE,fg=COLOR_STEELBLUE,font=ARIALBOLD10)
    CurrentUserLabelHeading.place(x=5,y=83)
    CurrentUserLabel=Label(frame,text=result[2],fg=COLOR_STEELBLUE,bg=COLOR_WHITE,font=ARIALBOLD10)
    CurrentUserLabel.place(x=100,y=83)

    DashboardMainScreen(frame)

def DashboardMainScreen(frame):
    BackgroundFrame = Frame(frame,bg=COLOR_SKYBLUE,width=900,height=390)
    BackgroundFrame.place(x=0,y=110)

    DecoCanvas = Canvas(BackgroundFrame,height=390,width=450,bg=COLOR_SKYBLUE,bd=0,highlightthickness=0)
    DecoCanvas.place(x=0,y=0)
    DecoImage = PhotoImage(file=DECORATIONIMAGE)
    frame.AdjustedDecoImage = AdjustedDecoImage = DecoImage.subsample(5,5)
    DecoCanvas.create_image((40,30),image=AdjustedDecoImage,anchor=NW)


    ButtonsFrame = Frame(BackgroundFrame,height=390,width=450,bg=COLOR_SKYBLUE)
    ButtonsFrame.place(x=450,y=0)
    AddStudentButton=Button(ButtonsFrame,text='Add Student Data',fg=COLOR_STEELBLUE,bg=COLOR_WHITE,
        font=ARIALBOLD15,width=30,command=lambda:AddStudent(frame))
    AddStudentButton.place(x=0,y=40)
    
    ShowStudentButton=Button(ButtonsFrame,text='Show All Students',fg=COLOR_STEELBLUE,bg=COLOR_WHITE,
        font=ARIALBOLD15,width=30,command=lambda:AllStudents(frame))
    ShowStudentButton.place(x=0,y=110)

    LogOutButton=Button(ButtonsFrame,text='LOG OUT',fg=COLOR_WHITE,bg=COLOR_FIREBRICKRED,
        font=ARIALBOLD12,width=10,command=lambda:login.LoginScreen(frame))
    LogOutButton.place(x=0,y=200)