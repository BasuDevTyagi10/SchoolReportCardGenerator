from tkinter import *
from res import *
from login import *

root = Tk()
root.iconbitmap(APPLICATIONICON)
root.title(APPLICATIONNAME)
positionRight = int((root.winfo_screenwidth()-WINDOWX)/2)
positionDown = int((root.winfo_screenheight()-WINDOWY)/2)
root.geometry('{}x{}+{}+{}'.format(WINDOWX,WINDOWY,positionRight,positionDown))
root.resizable(0,0)
LoginScreen(root)
root.mainloop()