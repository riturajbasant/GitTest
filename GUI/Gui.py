from tkinter import *
root = Tk()
lb1=Label (text="This is my lebel 1")
lb2=Label(text="This is my Label 2", bg="Sky Blue")
lb3=Label(text="This is my Laber 3", bg="Green",fg='Red',font='Arial')
lb1.pack(side=TOP)
lb2.pack(side=RIGHT)
lb3.pack(side=LEFT)


root.mainloop() #create new GUI window
