from tkinter import *
from demo19_ModuleAndImport_1 import MyHome

homeBusan = MyHome("Busan S")

def paintRoof():
    strColor = txtColor.get(1.0, END)
    homeBusan.paintRoof(strColor)
    lblColor['text'] = homeBusan.colorRoof

root = Tk()
txtColor = Text(root, width=20, height=2)
lblColor = Label(root, text = homeBusan.colorRoof, width=20, height=2)
btnColor = Button(root, text = "Paint the Roof", width = 20, height = 1, \
    command=paintRoof)

txtColor.pack()
lblColor.pack()
btnColor.pack()

root.mainloop()