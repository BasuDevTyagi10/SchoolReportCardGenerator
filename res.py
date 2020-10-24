#--------------DATA--------------
import sqlite3
DATABASE_DB = r".\database.db"
DATABASECONNECTION = sqlite3.connect(DATABASE_DB)

ADMIN_DATABASE = {'tablename':'adminInfo','ColUserID':'UserID','ColPassword':'Password','ColUserName':'UserName'}
STUDENT_DATABASE = {'tablename':'studInfo','ColStudAdm':'StudAdmNo','ColStudName':'StudName','ColStudClass':'StudClass',
    'ColStudGuardian':'StudGuardian','ColStudRno':'StudRno','ColMarksEng':'MarksEng','ColMarksMaths':'MarksMaths',
    'ColMarksSci':'MarksSci','ColMarksSst':'MarksSst','ColMarksOpt':'MarksOpt','ColMarksHindi':'MarksHindi',
    'ColRemarks':'Remarks','ColCT':'CTInitials','ColTotal':'Total','ColPer':'Percent','ColPorF':'PF'}
TEACHER_DATABASE = {'tablename':'teacherInfo','ColTeacherName':'TeacherName','ColTeacherInitials':'TeacherInitials'}

cursor = DATABASECONNECTION.cursor()
cursor.execute('SELECT {} FROM {}'.format(TEACHER_DATABASE['ColTeacherInitials'],TEACHER_DATABASE['tablename']))
TEACHER_INITIALS = cursor.fetchall()
TEACHER_INITIALS.insert(0,'')

DATABASE_CSV = r'.\datasourcecsv.csv'
WORDTEMPLATE = r'template.docx'

#--------------APP-DATA--------------
WINDOWX = 900
WINDOWY = 500
APPLICATIONNAME = 'STUDENT REPORT-CARD MANAGER'
APPLICATIONICON = r'.\icon.ico'

#--------------IMAGES--------------
USERIMAGE = r'.\res\img_user.png'
BACKBUTTON = r'.\res\back_arrow.png'
SEARCHBUTTON = r'.\res\search.png'
DECORATIONIMAGE = r'.\res\reportcard.png'
REFRESHBUTTON = r'.\res\refresh.png'

#--------------COLORS--------------
COLOR_BLACK = '#000000'
COLOR_WHITE = '#FFFFFF'
COLOR_ALICEBLUE = '#F0F8FF'
COLOR_STEELBLUE = '#236B8E'
COLOR_SKYBLUE = '#3299CC'
COLOR_NEONBLUE = '#67C8FF'
COLOR_FIREBRICKRED = '#B22222'

#--------------FONTS--------------
ARIALBOLD40 = ('Arial',40,'bold')
ARIALBOLD30 = ('Arial',30,'bold')
ARIALBOLD20 = ('Arial',20,'bold')
ARIALBOLD15 = ('Arial',15,'bold')
ARIALBOLD12 = ('Arial',12,'bold')
ARIALBOLD11 = ('Arial',11,'bold')
ARIALBOLD10 = ('Arial',10,'bold')
ARIAL10 = ('Arial',10)
ARIALBOLD9 = ('Arial',9,'bold')
TIMESNEWROMANBOLD20 = ('Times New Roman',20,'bold')
TIMESNEWROMANBOLD17 = ('Times New Roman',17,'bold')