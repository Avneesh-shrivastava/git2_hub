from tkinter import *

root = Tk()
root.title("Calculator")

pack = []
e = Entry(root,width=20,font=("Arial",15,'bold'),bg="cyan",relief=RAISED)
e.grid(row=0,column=0,columnspan=20)

def equal():
    global pack
    try:
        
        v = e.get()
        pack = v.split()
        x = int(pack[0])
        y = int(pack[2])
        e.delete(0,END)
        if pack[1] == "➕":
            e.insert("end",x + y)
        if pack[1] == "➖":
            e.insert("end",x - y)        
        if pack[1] == "✖️":
            e.insert("end",x * y)
        if pack[1] == "➗":
            e.insert("end",x // y)
    except:
        e.delete(0,END)
        e.insert("end","an err occured")

def clr():
    global pack
    e.delete(0,END)
    pack.clear()

#operators
def addition():
    e.insert("end"," ➕ ")
def subtraction():
    e.insert("end"," ➖ ")
def multiply():
    e.insert("end"," ✖️ ")
def division():
    e.insert("end"," ➗ ")

#displays button on entrybox
def nine():
    e.insert("end",9)
def eight():
    e.insert("end",8) 
def seven():
    e.insert("end",7)      
def six():
    e.insert("end",6) 
def five():
    e.insert("end",5) 
def four():
    e.insert("end",4) 
def three():
    e.insert("end",3) 
def two():
    e.insert("end",2) 
def one():
    e.insert("end",1)     
def zero():
    e.insert("end",0)

#button
b9 = Button(text="9",width=7,height=3,command=nine,bg="yellow")
b9.grid(row=1,column=0)
b8 = Button(text="8",width=7,height=3,command=eight,bg="yellow")
b8.grid(row=1,column=1)
b7 = Button(text="7",width=7,height=3,command=seven,bg="yellow")
b7.grid(row=1,column=2)
b6 = Button(text="6",width=7,height=3,command=six,bg="yellow")
b6.grid(row=2,column=0)
b5 = Button(text="5",width=7,height=3,command=five,bg="yellow")
b5.grid(row=2,column=1)
b4 = Button(text="4",width=7,height=3,command=four,bg="yellow")
b4.grid(row=2,column=2)
b3 = Button(text="3",width=7,height=3,command=three,bg="yellow")
b3.grid(row=3,column=0)
b2 = Button(text="2",width=7,height=3,command=two,bg="yellow")
b2.grid(row=3,column=1)
b1 = Button(text="1",width=7,height=3,command=one,bg="yellow")
b1.grid(row=3,column=2)
b0 = Button(text="0",width=7,height=3,command=zero,bg="yellow")
b0.grid(row=4,column=0)

#clear all button
clear = Button(text="C",width=7,height=3,command=clr,bg="red")
clear.grid(row=4,column=1)

div = Button(text="➗",width=5,height=3,command=division,bg="lightblue")
div.grid(row=1,column=3)
add = Button(text="➕",width=7,height=3,command=addition,bg="lightblue")
add.grid(row=4,column=2)
sub = Button(text="➖",width=5,height=3,command=subtraction,bg="lightblue")
sub.grid(row=2,column=3)
multi = Button(text="✖️",width=5,height=3,command=multiply,bg="lightblue")
multi.grid(row=3,column=3)
eq = Button(text="🟰",width=5,height=3,command=equal,bg="lightblue")
eq.grid(row=4,column=3)

root.mainloop()