import os
import pandas as pd
import tkinter.messagebox
from mailmerge import MailMerge
from docx2pdf import convert
from res import *

def PDFReportCard(window,data):
    PDFPath = '.\output\ReportCard-{}.pdf'.format(data[0])
    DOCXPath = '.\output\ReportCard-{}.docx'.format(data[0])
    document = MailMerge(WORDTEMPLATE)
    document.merge(
        AdmissionNo = data[0],
        StudentName = data[1],
        Class = data[2],
        GuardianName = data[3],
        ClassRollNo = str(data[4]),
        MarksInEnglish = str(data[5]),
        MarksInMaths = str(data[6]),
        MarksInScience = str(data[7]),
        MarksInSSt = str(data[8]),
        MarksInOptional = str(data[9]),
        MarksInHindi = str(data[10]),
        TeacherRemarks = data[11],
        ClassTeacherInitials = data[12],
        TotalMarks = str(data[13]),
        Percentage = str(data[14]),
        PassOrFail = data[15]
    )
    document.write(DOCXPath)
    convert(DOCXPath,PDFPath)
    if(not tkinter.messagebox.askyesnocancel(APPLICATIONNAME,"Do you wish to keep a .docx copy of the Report Card?")):
        os.remove(DOCXPath)
        tkinter.messagebox.showinfo(APPLICATIONNAME,"PDF File saved at Path:\t\n\""+PDFPath+"\"")
    else:
        tkinter.messagebox.showinfo(APPLICATIONNAME,"Files saved at Path:\t\n\""+DOCXPath+"\"\n\""+PDFPath+"\"")
    window.destroy()