from reportcard import *
from res import *
from tkinter import *
import tkinter.messagebox
from tkinter import ttk


cursor = DATABASECONNECTION.cursor()

def ClearEntries(entry1,entry2,combobox1,entry3,entry4,entry5,entry6,entry7,entry8,entry9,enrty10,text1,combobox2):
    entry1.delete(0,END)
    entry2.delete(0,END)
    combobox1.current(0)
    entry3.delete(0,END)
    entry4.delete(0,END)
    entry5.delete(0,END)
    entry6.delete(0,END)
    entry7.delete(0,END)
    entry8.delete(0,END)
    entry9.delete(0,END)
    enrty10.delete(0,END)
    text1.delete(1.0,END)
    combobox2.current(0)

def AddStudentToDB(studadmno,studname,studclass,gname,studrno,markseng,marksmath,markssci,markssst,marksopt,markshin,rems,ctini,
    entrya,entryn,cbcls,entrygn,entryrno,entryeng,entrymat,entrysci,entrysst,entryopt,entryhin,textrem,cbct):
    
    if '' in (studadmno,studname,studclass,gname,studrno,markseng,marksmath,markssci,markssst,marksopt,markshin,ctini):
        tkinter.messagebox.showerror(APPLICATIONNAME,"Missing Data Field(s)")
    else:
        cursor.execute('SELECT * FROM '+STUDENT_DATABASE['tablename']+' WHERE '+STUDENT_DATABASE['ColStudAdm']+'='+studadmno+'')
        if(cursor.fetchone()!=None):
            tkinter.messagebox.showerror(APPLICATIONNAME,"Student Data Already Registered")
        else:
            markserror = 0
            if(int(markseng)>100 or int(markseng)<0):
                markserror+=1
            if(int(marksmath)>100 or int(marksmath)<0):
                markserror+=1
            if(int(markssci)>100 or int(markssci)<0):
                markserror+=1
            if(int(markssst)>100 or int(markssst)<0):
                markserror+=1
            if(int(marksopt)>100 or int(marksopt)<0):
                markserror+=1
            if(int(markshin)>100 or int(markshin)<0):
                markserror+=1
            
            if(markserror>0):
                tkinter.messagebox.showerror(APPLICATIONNAME,"Invalid Marks in {} subjects\nValue must be within 0 and 100".format(markserror))
            if(int(studrno)<0):
                tkinter.messagebox.showerror(APPLICATIONNAME,"Invalid Class Roll Number.")
            if(markserror == 0 and int(studrno)>0):
                total = int(markseng)+int(marksmath)+int(markssci)+int(markssst)+int(marksopt)+int(markshin)
                per = float("{:.2f}".format(total/6))
                cursor.execute('INSERT INTO '+STUDENT_DATABASE['tablename']+'('+STUDENT_DATABASE['ColStudAdm']+','+STUDENT_DATABASE['ColStudName']+',\
                    '+STUDENT_DATABASE['ColStudClass']+','+STUDENT_DATABASE['ColStudGuardian']+','+STUDENT_DATABASE['ColStudRno']+','+STUDENT_DATABASE['ColMarksEng']+',\
                    '+STUDENT_DATABASE['ColMarksMaths']+','+STUDENT_DATABASE['ColMarksSci']+','+STUDENT_DATABASE['ColMarksSst']+','+STUDENT_DATABASE['ColMarksOpt']+',\
                    '+STUDENT_DATABASE['ColMarksHindi']+','+STUDENT_DATABASE['ColRemarks']+','+STUDENT_DATABASE['ColCT']+','+STUDENT_DATABASE['ColTotal']+','+STUDENT_DATABASE['ColPer']+',\
                    '+STUDENT_DATABASE['ColPorF']+') VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',(
                    studadmno,studname,studclass,gname,studrno,
                    markseng,marksmath,markssci,markssst,marksopt,markshin,
                    rems.rstrip(),ctini,total,per,'Pass' if per>=40 else 'Fail')
                )
                DATABASECONNECTION.commit()
                tkinter.messagebox.showinfo(APPLICATIONNAME,"Date Recorded!")
                ClearEntries(entrya,entryn,cbcls,entrygn,entryrno,entryeng,entrymat,entrysci,entrysst,entryopt,entryhin,textrem,cbct)

def SortDataList(datalist):
    datalist.sort(key=lambda x: x[0])
    return datalist

def ShowStudentData(table):
    cursor.execute("SELECT * FROM "+STUDENT_DATABASE['tablename']+"")
    datalist = SortDataList(cursor.fetchall())
    if len(datalist)!=0:
        for data in datalist:
            table.insert('',END,values=data)

def ClearTable(table):
    for record in table.get_children():
        table.delete(record)

def Reload(table):
    ClearTable(table)
    ShowStudentData(table)

def SearchStudentData(admno,table):
    if(admno!=''):
        cursor.execute("SELECT * FROM "+STUDENT_DATABASE['tablename']+" WHERE "+STUDENT_DATABASE['ColStudAdm']+"="+admno+"")
        searchresult = cursor.fetchone()
        if(searchresult!=None):
            ClearTable(table)
            table.insert('',END,values=searchresult)

def UpdateDB(window,searchadmno,table,studadmno,studname,studclass,gname,studrno,markseng,marksmath,markssci,markssst,marksopt,markshin,rems,ctini,
    entrya,entryn,cbcls,entrygn,entryrno,entryeng,entrymat,entrysci,entrysst,entryopt,entryhin,textrem,cbct):
    
    if '' in (studadmno,studname,studclass,gname,studrno,markseng,marksmath,markssci,markssst,marksopt,markshin,ctini):
        tkinter.messagebox.showerror(APPLICATIONNAME,"Missing Data Field(s)")
    else:
        cursor.execute('SELECT * FROM '+STUDENT_DATABASE['tablename']+' WHERE '+STUDENT_DATABASE['ColStudAdm']+'='+studadmno+'')
        if(studadmno != searchadmno and cursor.fetchone()!=None):
            tkinter.messagebox.showerror(APPLICATIONNAME,"Student Data Already Registered")
            window.focus_force()
        else:
            markserror = 0
            if(int(markseng)>100 or int(markseng)<0):
                markserror+=1
            if(int(marksmath)>100 or int(marksmath)<0):
                markserror+=1
            if(int(markssci)>100 or int(markssci)<0):
                markserror+=1
            if(int(markssst)>100 or int(markssst)<0):
                markserror+=1
            if(int(marksopt)>100 or int(marksopt)<0):
                markserror+=1
            if(int(markshin)>100 or int(markshin)<0):
                markserror+=1
            
            if(markserror>0):
                tkinter.messagebox.showerror(APPLICATIONNAME,"Invalid Marks in {} subjects\nValue must be within 0 and 100".format(markserror))
            if(int(studrno)<0):
                tkinter.messagebox.showerror(APPLICATIONNAME,"Invalid Class Roll Number.")
            if(markserror == 0 and int(studrno)>0):
                total = int(markseng)+int(marksmath)+int(markssci)+int(markssst)+int(marksopt)+int(markshin)
                per = float("{:.2f}".format(total/6))
                porf = 'Pass' if per>=40 else 'Fail'
                cursor.execute('UPDATE '+STUDENT_DATABASE['tablename']+' SET '+STUDENT_DATABASE['ColStudAdm']+'="'+studadmno+'",'+STUDENT_DATABASE['ColStudName']+'="'+studname+'",\
                    '+STUDENT_DATABASE['ColStudClass']+'="'+studclass+'",'+STUDENT_DATABASE['ColStudGuardian']+'="'+gname+'",'+STUDENT_DATABASE['ColStudRno']+'='+studrno+',\
                    '+STUDENT_DATABASE['ColMarksEng']+'='+markseng+','+STUDENT_DATABASE['ColMarksMaths']+'='+marksmath+','+STUDENT_DATABASE['ColMarksSci']+'='+markssci+',\
                    '+STUDENT_DATABASE['ColMarksSst']+'='+markssst+','+STUDENT_DATABASE['ColMarksOpt']+'='+marksopt+','+STUDENT_DATABASE['ColMarksHindi']+'='+markshin+',\
                    '+STUDENT_DATABASE['ColRemarks']+'="'+rems.rstrip()+'",'+STUDENT_DATABASE['ColCT']+'="'+ctini+'",'+STUDENT_DATABASE['ColTotal']+'='+str(total)+',\
                    '+STUDENT_DATABASE['ColPer']+'='+str(per)+','+STUDENT_DATABASE['ColPorF']+'="'+porf+'"\
                    WHERE '+STUDENT_DATABASE['ColStudAdm']+'='+searchadmno+'')
                DATABASECONNECTION.commit()
                tkinter.messagebox.showinfo(APPLICATIONNAME,"Date Updated!")
                window.destroy()
                Reload(table)
            
def EditStudentData(table):
    if(table.selection()):
        admno = table.item(table.selection()[0])['values'][0]
        cursor.execute("SELECT * FROM "+STUDENT_DATABASE['tablename']+" WHERE "+STUDENT_DATABASE['ColStudAdm']+"="+str(admno)+"")
        editdata = cursor.fetchone()
    #WINDOW    
        EditStudentDataWindow = Tk()
        EditStudentDataWindow.configure(bg=COLOR_WHITE)
        EditStudentDataWindow.title(APPLICATIONNAME)
        EditStudentDataWindow.geometry("700x360+400+300")
        EditStudentDataWindow.resizable(0,0)
        EditStudentDataWindow.iconbitmap(APPLICATIONICON)

        HeadingFrame = Frame(EditStudentDataWindow,bg=COLOR_STEELBLUE,width=690,height=35)
        HeadingFrame.place(x=5,y=5)
        HeadingLabel = Label(HeadingFrame,text='EDIT STUDENT',fg='#fff',bg=COLOR_STEELBLUE,font=ARIALBOLD12)
        HeadingLabel.place(x=270,y=6)

        StudentDetailsFrame = Frame(EditStudentDataWindow,bg=COLOR_ALICEBLUE,width=690,height=75,highlightbackground=COLOR_SKYBLUE,highlightthickness=1)
        StudentDetailsFrame.place(x=5,y=45)
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

        MarksFrame1 = Frame(EditStudentDataWindow,bg=COLOR_ALICEBLUE,width=400,height=230,highlightbackground=COLOR_SKYBLUE,highlightthickness=1)
        MarksFrame1.place(x=5,y=125)
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

        MarksFrame2 = Frame(EditStudentDataWindow,bg=COLOR_ALICEBLUE,width=285,height=230,highlightbackground=COLOR_SKYBLUE,highlightthickness=1)
        MarksFrame2.place(x=410,y=125)
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

        AddStudentButton = Button(MarksFrame2,text='Save Changes',fg=COLOR_WHITE,bg=COLOR_SKYBLUE,
            font=ARIALBOLD10,width=15,relief=FLAT,command=lambda:UpdateDB(
            EditStudentDataWindow,
            str(admno),
            table,
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
        AddStudentButton.place(x=85,y=160)

        EntryAdmNo.insert(0,editdata[0])
        EntryName.insert(0,editdata[1])
        ComboBoxClass.set(editdata[2])
        EntryGuardianName.insert(0,editdata[3])
        EntryClassRNo.insert(0,editdata[4])
        EntryEng.insert(0,editdata[5])
        EntryMaths.insert(0,editdata[6])
        EntrySci.insert(0,editdata[7])
        EntrySst.insert(0,editdata[8])
        EntryOpt.insert(0,editdata[9])
        EntryHindi.insert(0,editdata[10])
        TextRemarks.insert(END,editdata[11])
        ComboBoxCT.set(editdata[12])

        EditStudentDataWindow.focus_force()
        EditStudentDataWindow.mainloop()
    #WINDOW END
    else:
        tkinter.messagebox.showerror(APPLICATIONNAME,"Please make a selection from the table!")

def DeleteAllStudentData():
    if(tkinter.messagebox.askyesnocancel(APPLICATIONNAME,"Are you sure you want to DELETE ALL the Student Data?")):
        cursor.execute("DELETE FROM "+STUDENT_DATABASE['tablename']+"")
        DATABASECONNECTION.commit()
        tkinter.messagebox.showinfo(APPLICATIONNAME,"Student Data Deleted!")

def DeleteSelectedStudentData(table):
    admnolist = []
    for records in table.selection():
        admnolist.append(table.item(records)['values'][0])
    if(len(admnolist)!=0):
        if(tkinter.messagebox.askyesnocancel(APPLICATIONNAME,"Are you sure you want to DELETE the SELECTED Student Data of {} student(s)?".format(len(admnolist)))):
            for admno in admnolist:
                cursor.execute("DELETE FROM "+STUDENT_DATABASE['tablename']+" WHERE "+STUDENT_DATABASE['ColStudAdm']+"="+str(admno)+"")
                DATABASECONNECTION.commit()
            tkinter.messagebox.showinfo(APPLICATIONNAME,"{} Student(s) Data Deleted!".format(len(admnolist)))
            Reload(table)
    else:
        tkinter.messagebox.showerror(APPLICATIONNAME,"Please make a selection from the table!")

def GenerateReportCard(table):
    if(table.selection()):
        admno = table.item(table.selection()[0])['values'][0]
        cursor.execute("SELECT * FROM "+STUDENT_DATABASE['tablename']+" WHERE "+STUDENT_DATABASE['ColStudAdm']+"="+str(admno)+"")
        data = cursor.fetchone()
    #WINDOW
        GenerateReportCardWindow = Tk()
        GenerateReportCardWindow.configure(bg=COLOR_WHITE)
        GenerateReportCardWindow.title(APPLICATIONNAME)
        GenerateReportCardWindow.geometry("700x360+400+300")
        GenerateReportCardWindow.resizable(0,0)
        GenerateReportCardWindow.iconbitmap(APPLICATIONICON)

        HeadingFrame = Frame(GenerateReportCardWindow,bg=COLOR_STEELBLUE,width=690,height=35)
        HeadingFrame.place(x=5,y=5)
        HeadingLabel = Label(HeadingFrame,text='GENERATE REPORT CARD',fg='#fff',bg=COLOR_STEELBLUE,font=ARIALBOLD12)
        HeadingLabel.place(x=240,y=6)

        StudentDetailsFrame = Frame(GenerateReportCardWindow,bg=COLOR_ALICEBLUE,width=690,height=310,highlightbackground=COLOR_SKYBLUE,highlightthickness=1)
        StudentDetailsFrame.place(x=5,y=45)
        LabelPersonalDetailsHeading = Label(StudentDetailsFrame,text='PERSONAL DETAILS',fg=COLOR_BLACK,bg=COLOR_ALICEBLUE,font=ARIALBOLD11)
        LabelPersonalDetailsHeading.place(x=15,y=10)
        LabelName = Label(StudentDetailsFrame,text='Name :',fg=COLOR_BLACK,bg=COLOR_ALICEBLUE,font=ARIALBOLD10)
        LabelName.place(x=10,y=30)
        LabelName1 = Label(StudentDetailsFrame,text=data[1],fg=COLOR_BLACK,bg=COLOR_ALICEBLUE,font=ARIAL10)
        LabelName1.place(x=60,y=30)
        LabelGuardian = Label(StudentDetailsFrame,text='Guardian Name :',fg=COLOR_BLACK,bg=COLOR_ALICEBLUE,font=ARIALBOLD10)
        LabelGuardian.place(x=350,y=30)
        LabelGuardian1 = Label(StudentDetailsFrame,text=data[3],fg=COLOR_BLACK,bg=COLOR_ALICEBLUE,font=ARIAL10)
        LabelGuardian1.place(x=465,y=30)
        LabelAdmNo = Label(StudentDetailsFrame,text='Admission No. :',fg=COLOR_BLACK,bg=COLOR_ALICEBLUE,font=ARIALBOLD10)
        LabelAdmNo.place(x=10,y=50)
        LabelAdmNo1 = Label(StudentDetailsFrame,text=data[0],fg=COLOR_BLACK,bg=COLOR_ALICEBLUE,font=ARIAL10)
        LabelAdmNo1.place(x=115,y=50)
        LabelClass = Label(StudentDetailsFrame,text='Class :',fg=COLOR_BLACK,bg=COLOR_ALICEBLUE,font=ARIALBOLD10)
        LabelClass.place(x=270,y=50)
        LabelClass1 = Label(StudentDetailsFrame,text=data[2],fg=COLOR_BLACK,bg=COLOR_ALICEBLUE,font=ARIAL10)
        LabelClass1.place(x=320,y=50)
        LabelClassRno = Label(StudentDetailsFrame,text='Class Roll No. :',fg=COLOR_BLACK,bg=COLOR_ALICEBLUE,font=ARIALBOLD10)
        LabelClassRno.place(x=510,y=50)
        LabelClassRno1 = Label(StudentDetailsFrame,text=data[4],fg=COLOR_BLACK,bg=COLOR_ALICEBLUE,font=ARIAL10)
        LabelClassRno1.place(x=615,y=50)
        LabelMarksHeading = Label(StudentDetailsFrame,text='MARKS',fg=COLOR_BLACK,bg=COLOR_ALICEBLUE,font=ARIALBOLD11)
        LabelMarksHeading.place(x=15,y=80)
        LabelEng = Label(StudentDetailsFrame,text='English :',fg=COLOR_BLACK,bg=COLOR_ALICEBLUE,font=ARIALBOLD10)
        LabelEng.place(x=10,y=100)
        LabelEng1 = Label(StudentDetailsFrame,text=data[5],fg=COLOR_BLACK,bg=COLOR_ALICEBLUE,font=ARIAL10)
        LabelEng1.place(x=70,y=100)
        LabelHindi = Label(StudentDetailsFrame,text='Hindi :',fg=COLOR_BLACK,bg=COLOR_ALICEBLUE,font=ARIALBOLD10)
        LabelHindi.place(x=230,y=100)
        LabelHindi1 = Label(StudentDetailsFrame,text=data[10],fg=COLOR_BLACK,bg=COLOR_ALICEBLUE,font=ARIAL10)
        LabelHindi1.place(x=275,y=100)
        LabelSci = Label(StudentDetailsFrame,text='Science :',fg=COLOR_BLACK,bg=COLOR_ALICEBLUE,font=ARIALBOLD10)
        LabelSci.place(x=460,y=100)
        LabelSci1 = Label(StudentDetailsFrame,text=data[7],fg=COLOR_BLACK,bg=COLOR_ALICEBLUE,font=ARIAL10)
        LabelSci1.place(x=525,y=100)
        LabelMaths = Label(StudentDetailsFrame,text='Mathematics :',fg=COLOR_BLACK,bg=COLOR_ALICEBLUE,font=ARIALBOLD10)
        LabelMaths.place(x=10,y=120)
        LabelMaths = Label(StudentDetailsFrame,text=data[6],fg=COLOR_BLACK,bg=COLOR_ALICEBLUE,font=ARIAL10)
        LabelMaths.place(x=100,y=120)
        LabelSSt = Label(StudentDetailsFrame,text='Social Studies :',fg=COLOR_BLACK,bg=COLOR_ALICEBLUE,font=ARIALBOLD10)
        LabelSSt.place(x=230,y=120)
        LabelSSt1 = Label(StudentDetailsFrame,text=data[8],fg=COLOR_BLACK,bg=COLOR_ALICEBLUE,font=ARIAL10)
        LabelSSt1.place(x=335,y=120)
        LabelOpt = Label(StudentDetailsFrame,text='Optional Subject :',fg=COLOR_BLACK,bg=COLOR_ALICEBLUE,font=ARIALBOLD10)
        LabelOpt.place(x=460,y=120)
        LabelOpt1 = Label(StudentDetailsFrame,text=data[9],fg=COLOR_BLACK,bg=COLOR_ALICEBLUE,font=ARIAL10)
        LabelOpt1.place(x=580,y=120)
        LabelTotal = Label(StudentDetailsFrame,text='TOTAL :',fg=COLOR_BLACK,bg=COLOR_ALICEBLUE,font=ARIALBOLD10)
        LabelTotal.place(x=10,y=145)
        LabelTotal1 = Label(StudentDetailsFrame,text=data[13],fg=COLOR_BLACK,bg=COLOR_ALICEBLUE,font=ARIAL10)
        LabelTotal1.place(x=65,y=145)
        LabelPer = Label(StudentDetailsFrame,text='PERCENTAGE :',fg=COLOR_BLACK,bg=COLOR_ALICEBLUE,font=ARIALBOLD10)
        LabelPer.place(x=350,y=145)
        LabelPer1 = Label(StudentDetailsFrame,text=data[14],fg=COLOR_BLACK,bg=COLOR_ALICEBLUE,font=ARIAL10)
        LabelPer1.place(x=450,y=145)
        LabelRemarksHeading = Label(StudentDetailsFrame,text='REMARKS',fg=COLOR_BLACK,bg=COLOR_ALICEBLUE,font=ARIALBOLD11)
        LabelRemarksHeading.place(x=15,y=175)
        LabelResult = Label(StudentDetailsFrame,text='Result :',fg=COLOR_BLACK,bg=COLOR_ALICEBLUE,font=ARIALBOLD10)
        LabelResult.place(x=10,y=195)
        LabelResult1 = Label(StudentDetailsFrame,text=data[15],fg=COLOR_BLACK,bg=COLOR_ALICEBLUE,font=ARIAL10)
        LabelResult1.place(x=64,y=195)
        LabelRemarks = Label(StudentDetailsFrame,text='Teacher Remarks :',fg=COLOR_BLACK,bg=COLOR_ALICEBLUE,font=ARIALBOLD10)
        LabelRemarks.place(x=10,y=215)
        LabelRemarks1 = Label(StudentDetailsFrame,text=data[11],fg=COLOR_BLACK,bg=COLOR_ALICEBLUE,font=ARIAL10)
        LabelRemarks1.place(x=135,y=215)
        LabelCT = Label(StudentDetailsFrame,text='Class Teacher :',fg=COLOR_BLACK,bg=COLOR_ALICEBLUE,font=ARIALBOLD10)
        LabelCT.place(x=10,y=245)
        LabelCT1 = Label(StudentDetailsFrame,text=data[12],fg=COLOR_BLACK,bg=COLOR_ALICEBLUE,font=ARIAL10)
        LabelCT1.place(x=110,y=245)
        
        GenerateButton = Button(StudentDetailsFrame,text='Generate Report Card',fg=COLOR_WHITE,bg=COLOR_STEELBLUE,
            font=ARIALBOLD10,relief=FLAT,command=lambda:PDFReportCard(GenerateReportCardWindow,data))
        GenerateButton.place(x=380,y=250)
        
        GenerateReportCardWindow.focus_force()
        GenerateReportCardWindow.mainloop()
    #WINDOW-ENDS
    else:
        tkinter.messagebox.showerror(APPLICATIONNAME,"Please make a selection from the table!")