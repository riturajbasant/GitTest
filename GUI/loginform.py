from tkinter import *
from tkinter import messagebox as ms 
root=tk()
def fun1():
    ms.showinfo("Button1", "Record Inserted")
    lb1=Label(text="Login Form")
    lb2=Label(text="FirstName")
    lb3=Label(text="Last Name")
    lb4=Label(text="Mobile Number")
    lb5=Label(text="Email ID")
    lb6=Label(text="Password")
    tx1=Entry()
    tx2=Entry()
    Tx3=Entry()
    tx4=Entry()
    tx5=Entry()
    b1=Button(text="Submit",command=fun)