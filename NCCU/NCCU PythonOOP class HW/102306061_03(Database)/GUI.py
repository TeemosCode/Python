#GUI
import MainFunction_HW3_102306061何秉哲_with_all_required_sql_methods as M
import tkinter
from tkinter import *

top = tkinter.Tk()

def callM():
    tkinter.messagebox.showinfo(M.functionrun())

a = tkinter.Button(top, activebackground = "purple" , bg = 'gray' , text = 'startin datbase!' , command = callM )
a.pack()
b = tkinter.Button(top , activebackground = 'blue' , bg = 'gray' , text = "yolo!!")
b.pack()







top.mainloop()
