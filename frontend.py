from tkinter import *
from tkinter import ttk
from res import *
import dashboard
from backend import *

def AddStudent(frame):
    BackgroundFrame = Frame(frame,bg=COLOR_SKYBLUE,width=WINDOWX,height=WINDOWY-110)
    BackgroundFrame.place(x=0,y=110)
    MainFrame=Frame(BackgroundFrame,bg=COLOR_WHITE,width=700,height=360,bd=5,relief=FLAT)
    MainFrame.place(x=100,y=15)
    frame.BackImg = BackImg = PhotoImage(file=BACKBUTTON)
    BackButton = Button(BackgroundFrame,image=BackImg,bg=COLOR_SKYBLUE,activebackground=COLOR_SKYBLUE,
        borderwidth=0,relief=FLAT,command=lambda:dashboard.DashboardMainScreen(frame))
    BackButton.place(x=10, y=10)

    HeadingFrame = Frame(MainFrame,bg=COLOR_STEELBLUE,width=690,height=35)
    HeadingFrame.place(x=0,y=0)
    HeadingLabel = Label(HeadingFrame,text='ADD STUDENTS',fg='#fff',bg=COLOR_STEELBLUE,font=ARIALBOLD12)
    HeadingLabel.place(x=270,y=6)

    StudentDetailsFrame = Frame(MainFrame,bg=COLOR_ALICEBLUE,width=690,height=75,highlightbackground=COLOR_SKYBLUE,highlightthickness=1)
    StudentDetailsFrame.place(x=0,y=40)
    LabelAdmNo = Label(StudentDetailsFrame,text='Admission No. :',fg=COLOR_STEELBLUE,bg=COLOR_ALICEBLUE,font=ARIALBOLD11)
    LabelAdmNo.place(x=10,y=10)
    LabelName = Label(StudentDetailsFrame,text='Name :',fg=COLOR_STEELBLUE,bg=COLOR_ALICEBLUE,font=ARIALBOLD11)
    LabelName.place(x=260,y=10)
    LabelClass = Label(StudentDetailsFrame,text='Class :',fg=COLOR_STEELBLUE,bg=COLOR_ALICEBLUE,font=ARIALBOLD11)
    LabelClass.place(x=480,y=10)
    LabelGuardianName = Label(StudentDetailsFrame,text='Guardian Name :',fg=COLOR_STEELBLUE,bg=COLOR_ALICEBLUE,font=ARIALBOLD11)
    LabelGuardianName.place(x=10,y=40)
    LabelClassRNo = Label(StudentDetailsFrame,text='Class Roll No. :',fg=COLOR_STEELBLUE,bg=COLOR_ALICEBLUE,font=ARIALBOLD11)
    LabelClassRNo.place(x=300,y=40)
    EntryAdmNo = Entry(StudentDetailsFrame,width=15,bd=2,relief=GROOVE)
    EntryAdmNo.place(x=130,y=11)
    EntryName = Entry(StudentDetailsFrame,width=20,bd=2,relief=GROOVE)
    EntryName.place(x=320,y=11)
    ComboBoxClass = ttk.Combobox(StudentDetailsFrame,width=5,state='readonly')
    ComboBoxClass['value'] = ('','I','II','III','IV','V','VI','VII','VIII','IX','X','XI','XII')
    ComboBoxClass.current(0)
    ComboBoxClass.place(x=540,y=11)
    EntryGuardianName = Entry(StudentDetailsFrame,width=20,bd=2,relief=GROOVE)
    EntryGuardianName.place(x=140,y=41)
    EntryClassRNo = Entry(StudentDetailsFrame,width=5,bd=2,relief=GROOVE)
    EntryClassRNo.place(x=420,y=41)

    MarksFrame1 = Frame(MainFrame,bg=COLOR_ALICEBLUE,width=400,height=230,highlightbackground=COLOR_SKYBLUE,highlightthickness=1)
    MarksFrame1.place(x=0,y=120)
    LabelMarksOb = Label(MarksFrame1,text="MARKS OBTAINED",fg=COLOR_STEELBLUE,bg=COLOR_ALICEBLUE,font=ARIALBOLD12)
    LabelMarksOb.place(x=10,y=20)
    LabelEng = Label(MarksFrame1,text="English:",fg=COLOR_STEELBLUE,bg=COLOR_ALICEBLUE,font=ARIALBOLD11)
    LabelEng.place(x=5,y=70)
    EntryEng = Entry(MarksFrame1,width=5,bd=2,relief=GROOVE)
    EntryEng.place(x=70,y=71)
    Label1001 = Label(MarksFrame1,text="/100",fg=COLOR_STEELBLUE,bg=COLOR_ALICEBLUE,font=ARIALBOLD10)
    Label1001.place(x=105,y=70)
    LabelSst = Label(MarksFrame1,text="Social Studies:",fg=COLOR_STEELBLUE,bg=COLOR_ALICEBLUE,font=ARIALBOLD11)
    LabelSst.place(x=175,y=70)
    EntrySst = Entry(MarksFrame1,width=5,bd=2,relief=GROOVE)
    EntrySst.place(x=290,y=71)
    Label1002 = Label(MarksFrame1,text="/100",fg=COLOR_STEELBLUE,bg=COLOR_ALICEBLUE,font=ARIALBOLD10)
    Label1002.place(x=325,y=70)
    LabelMaths = Label(MarksFrame1,text="Maths:",fg=COLOR_STEELBLUE,bg=COLOR_ALICEBLUE,font=ARIALBOLD11)
    LabelMaths.place(x=5,y=100)
    EntryMaths = Entry(MarksFrame1,width=5,bd=2,relief=GROOVE)
    EntryMaths.place(x=70,y=101)
    Label1003 = Label(MarksFrame1,text="/100",fg=COLOR_STEELBLUE,bg=COLOR_ALICEBLUE,font=ARIALBOLD10)
    Label1003.place(x=105,y=100)
    LabelOpt = Label(MarksFrame1,text="Optional:",fg=COLOR_STEELBLUE,bg=COLOR_ALICEBLUE,font=ARIALBOLD11)
    LabelOpt.place(x=175,y=100)
    EntryOpt = Entry(MarksFrame1,width=5,bd=2,relief=GROOVE)
    EntryOpt.place(x=290,y=101)
    Label1004 = Label(MarksFrame1,text="/100",fg=COLOR_STEELBLUE,bg=COLOR_ALICEBLUE,font=ARIALBOLD10)
    Label1004.place(x=325,y=100)
    LabelSci = Label(MarksFrame1,text="Science:",fg=COLOR_STEELBLUE,bg=COLOR_ALICEBLUE,font=ARIALBOLD11)
    LabelSci.place(x=5,y=130)
    EntrySci = Entry(MarksFrame1,width=5,bd=2,relief=GROOVE)
    EntrySci.place(x=70,y=131)
    Label1005 = Label(MarksFrame1,text="/100",fg=COLOR_STEELBLUE,bg=COLOR_ALICEBLUE,font=ARIALBOLD10)
    Label1005.place(x=105,y=130)
    LabelHindi = Label(MarksFrame1,text="Hindi:",fg=COLOR_STEELBLUE,bg=COLOR_ALICEBLUE,font=ARIALBOLD11)
    LabelHindi.place(x=175,y=130)
    EntryHindi = Entry(MarksFrame1,width=5,bd=2,relief=GROOVE)
    EntryHindi.place(x=290,y=131)
    Label1006 = Label(MarksFrame1,text="/100",fg=COLOR_STEELBLUE,bg=COLOR_ALICEBLUE,font=ARIALBOLD10)
    Label1006.place(x=325,y=130)

    MarksFrame2 = Frame(MainFrame,bg=COLOR_ALICEBLUE,width=285,height=230,highlightbackground=COLOR_SKYBLUE,highlightthickness=1)
    MarksFrame2.place(x=405,y=120)
    LabelRemarks = Label(MarksFrame2,text="Remarks(if any):",fg=COLOR_STEELBLUE,bg=COLOR_ALICEBLUE,font=ARIALBOLD11)
    LabelRemarks.place(x=10,y=20)
    TextRemarks = Text(MarksFrame2,height=3,width=30,bd=2,relief=GROOVE)
    TextRemarks.place(x=10,y=50)
    LabelCT = Label(MarksFrame2,text="Class Teacher Initials:",fg=COLOR_STEELBLUE,bg=COLOR_ALICEBLUE,font=ARIALBOLD11)
    LabelCT.place(x=10,y=120)
    ComboBoxCT = ttk.Combobox(MarksFrame2,width=5,state='readonly')
    ComboBoxCT['value'] = TEACHER_INITIALS
    ComboBoxCT.current(0)
    ComboBoxCT.place(x=180,y=121)

    AddStudentButton = Button(MarksFrame2,text='Add Data',fg=COLOR_WHITE,bg=COLOR_SKYBLUE,
        font=ARIALBOLD10,width=10,relief=FLAT,command=lambda:AddStudentToDB(
            EntryAdmNo.get(),
            EntryName.get(),
            ComboBoxClass.get(),
            EntryGuardianName.get(),
            EntryClassRNo.get(),
            EntryEng.get(),
            EntryMaths.get(),
            EntrySci.get(),
            EntrySst.get(),
            EntryOpt.get(),
            EntryHindi.get(),
            TextRemarks.get(1.0,END),
            ComboBoxCT.get(),
            EntryAdmNo,EntryName,ComboBoxClass,EntryGuardianName,EntryClassRNo,EntryEng,EntryMaths,EntrySci,EntrySst,EntryOpt,EntryHindi,TextRemarks,ComboBoxCT
        ))
    AddStudentButton.place(x=90,y=160)

def AllStudents(frame):
    BackgroundFrame = Frame(frame, bg=COLOR_SKYBLUE, width=900, height=390)
    BackgroundFrame.place(x=0, y=110)
    TitleBackgroundFrame = Frame(BackgroundFrame,width=900,height=30,bg=COLOR_SKYBLUE)
    TitleBackgroundFrame.place(x=0,y=0)
    HeadingLabel=Label(TitleBackgroundFrame,bg=COLOR_SKYBLUE,text='STUDENTS INFORMATION',fg='#fff',font=ARIALBOLD12)
    HeadingLabel.place(x=350,y=7)

    frame.BackImg = BackImg = PhotoImage(file=BACKBUTTON)
    BackButton = Button(BackgroundFrame,image=BackImg,bg=COLOR_SKYBLUE,activebackground=COLOR_SKYBLUE,
        borderwidth=0,relief=FLAT,command=lambda:dashboard.DashboardMainScreen(frame))
    BackButton.place(x=2,y=2)

    TableFrame = Frame(BackgroundFrame,bg=COLOR_WHITE,bd=1,relief=FLAT)
    TableFrame.place(x=0,y=90,width=900,height=300)    

    XScroll = Scrollbar(TableFrame,orient=HORIZONTAL)
    YScroll = Scrollbar(TableFrame,orient=VERTICAL)
    TableStudent =ttk.Treeview(TableFrame,
        columns=("StudentAdmNo","StudentName","StudentClass","StudentGuardian","StudentRno",
        "MarksEng","MarksMaths","MarksSci","MarksSst","MarksOpt","MarksHindi",
        "Remarks","CTInitials","Total","Per","PorF"),
        xscrollcommand=XScroll.set,yscrollcommand=YScroll.set)
    XScroll.pack(side=BOTTOM,fill=X)
    YScroll.pack(side=RIGHT, fill=Y)
    XScroll.config(command=TableStudent.xview)
    YScroll.config(command=TableStudent.yview)

    TableStudent.heading("StudentAdmNo", text="Adm. No.")
    TableStudent.heading("StudentName", text="Student Name")
    TableStudent.heading("StudentClass", text="Class")
    TableStudent.heading("StudentGuardian", text="Guardian Name")      
    TableStudent.heading("StudentRno", text="Roll No.")
    TableStudent.heading("MarksEng", text="ENG")
    TableStudent.heading("MarksMaths", text="MAT")
    TableStudent.heading("MarksSci", text="SCI")
    TableStudent.heading("MarksSst", text="SST")
    TableStudent.heading("MarksOpt", text="OPT")
    TableStudent.heading("MarksHindi", text="HIN")
    TableStudent.heading("Total", text="Total")
    TableStudent.heading("Per", text="%")
    TableStudent.heading("PorF",text="Result")
    TableStudent.heading("Remarks", text="Remarks")
    TableStudent.heading("CTInitials", text="Class Teacher")
    TableStudent['show']='headings'
    TableStudent.column("StudentAdmNo",width=60)
    TableStudent.column("StudentName",width=120)
    TableStudent.column("StudentClass",width=40)
    TableStudent.column("StudentGuardian",width=120)
    TableStudent.column("StudentRno",width=50)
    TableStudent.column("MarksEng",width=40)
    TableStudent.column("MarksMaths",width=40)
    TableStudent.column("MarksSci",width=40)
    TableStudent.column("MarksSst",width=40)
    TableStudent.column("MarksOpt",width=40)
    TableStudent.column("MarksHindi",width=40)
    TableStudent.column("Total",width=50)
    TableStudent.column("Per",width=30)
    TableStudent.column("PorF",width=40)
    TableStudent.column("CTInitials",width=80)
    
    TableStudent.pack(fill=BOTH,expand=1)

    TableStudent.bind("<Double-1>",lambda event:GenerateReportCard(TableStudent))

    ShowStudentData(TableStudent)

    frame.RefreshImage = RefreshImg = PhotoImage(file=REFRESHBUTTON)
    RefreshButton = Button(BackgroundFrame,image=RefreshImg,bg=COLOR_SKYBLUE,activebackground=COLOR_SKYBLUE,
        borderwidth=0,relief=FLAT,command=lambda:Reload(TableStudent))
    RefreshButton.place(x=44,y=3.5)

    EditOptionsFrame = Frame(BackgroundFrame,bg=COLOR_ALICEBLUE,width=900,height=50)
    EditOptionsFrame.place(x=0,y=40)
    SearchBoxLabel = Label(EditOptionsFrame,text="Admission No. :",bg=COLOR_ALICEBLUE,fg=COLOR_STEELBLUE,font=ARIALBOLD10)
    SearchBoxLabel.place(x=10,y=15)
    SearchBox = Entry(EditOptionsFrame,width=15,bd=2,relief=GROOVE)
    SearchBox.place(x=120,y=16)
    SearchBox.bind("<Return>",lambda event:SearchStudentData(SearchBox.get(),TableStudent))
    SearchImg = PhotoImage(file=SEARCHBUTTON)
    frame.SmallSearchImg = SmallSearchImg = SearchImg.subsample(2,2)
    SearchButton = Button(EditOptionsFrame,text=" Search",image=SmallSearchImg,bg=COLOR_SKYBLUE,
        fg=COLOR_WHITE,compound=LEFT,font=ARIALBOLD10,relief=FLAT,command=lambda:SearchStudentData(SearchBox.get(),TableStudent))
    SearchButton.place(x=230,y=12)
    EditStudentDataButton = Button(EditOptionsFrame,text='Edit Data',fg=COLOR_WHITE,bg=COLOR_STEELBLUE,
        font=ARIALBOLD10,width=10,relief=FLAT,command=lambda:EditStudentData(TableStudent))
    EditStudentDataButton.place(x=420,y=12)
    GenerateReportCardButton = Button(EditOptionsFrame,text='Generate Report Card',fg=COLOR_WHITE,bg=COLOR_STEELBLUE,
        font=ARIALBOLD10,relief=FLAT,command=lambda: GenerateReportCard(TableStudent))
    GenerateReportCardButton.place(x=520,y=12)
    DeleteSelectedStudentDataButton = Button(EditOptionsFrame,text='Delete Selected',fg=COLOR_WHITE,bg=COLOR_FIREBRICKRED,
        font=ARIALBOLD10,relief=FLAT,command=lambda:DeleteSelectedStudentData(TableStudent))
    DeleteSelectedStudentDataButton.place(x=680,y=12)
    DeleteAllStudentDataButton = Button(EditOptionsFrame,text='Delete All',fg=COLOR_WHITE,bg=COLOR_FIREBRICKRED,
        font=ARIALBOLD10,width=10,relief=FLAT,command=lambda:DeleteAllStudentData())
    DeleteAllStudentDataButton.place(x=800,y=12)