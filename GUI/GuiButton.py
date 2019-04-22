'''
from tkinter import *

root =Tk()
b1=Button(text="This is my Button One")
b2=Button(text='This is my Button Two', bg='SkyBlue')
b3=Button(text="This is my Button Three", bg="Yellow",fg='Red')
b4=Button(text="Tjhis is my Button Four",bg="green",fg="Blue")
b5=Button(text="This is my Button Five",bg="skyblue",fg="Blue")

b2.pack()
b1.pack(fill=X)

b3.pack(side=LEFT,fill=Y)
b4.pack(side=LEFT,fill=Y)
b5.pack(fill=X)
root.mainloop()


from tkinter import *
from tkinter import messagebox as ms

root=Tk()
def fun1():
    ms.showinfo("Button1","Hello World")
    root1=Tk()
    root1.mainloop()
def fun2():
    ms.showinfo("Button2","Python is a great Language")
def fun3():
    ms.showinfo("Button3","Pyhton is developed by Guido Van Rossum")

b1=Button(text="This is my Button one", command=fun1)
b2=Button(text="This is my Button One", bg="skyBlue",command=fun2)
b3=Button(text="This is my Button Three",bg="Yellow",fg='Red',command=fun3)
b1.grid()
b2.grid()
b3.grid()
root.mainloop()


'''

from tkinter import *
root = Tk()
lb=Label(root,text="Login Form")
lb.grid(row=0,column=10)
l=Label(root,text="Mail")
l2=Label(root,text="Password")
txt1=Entry()
txt2=Entry()
l.grid(row=1,column=9,stick="E")
txt1.grid(row=1,column=10)
l2.grid(row=2,column=9)
txt2.grid(row=2,column=10)
check=Checkbutton(root,text="Remember Password")
check.grid()
root.mainloop()






    






