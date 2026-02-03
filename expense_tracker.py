from tkinter import *
import datetime
from tkinter import ttk

root = Tk()
root.geometry("602x400")
root.title("Expense tracker")

list = []

def data():
    date = datetime.datetime.now()
    formatted_date = date.strftime("%B %d, %Y at %I:%M %p")
    entry = formatted_date
    entry1 = e1.get()
    e1.delete(0,END)
    entry2 = e2.get()
    e2.delete(0,END)
    tree.insert("",END, values=(entry,entry1,entry2))

    #storing data
    global list
    c = int(e.get())
    e.delete(0,END)
    list.append(c)
    
    total.config(text=f"Total Expense = ₹{sum(list)}",font=("Arial",15))


a = Label(text="Amount : ")
a.grid(row=0,column=0)
e = Entry(root)
e.grid(row=0,column=1)

a1 = Label(text="Category : ")
a1.grid(row=1,column=0)
e1 = Entry(root)
e1.grid(row=1,column=1)

a2 = Label(text="Description : ")
a2.grid(row=2,column=0)
e2 = Entry(root)
e2.grid(row=2,column=1)

button = Button(text="Add Expense",command=data)
button.grid(row=3,column=1,pady=10)

#table
tree  = ttk.Treeview(root,columns=("Date","Category","Description"),show="headings")
tree.grid(row=4,column=0,columnspan=5)

for col in ("Date","Category","Description"):
    tree.heading(col,text=col)
#table

total = Label(text="Total Expense = ₹0" ,font=("Arial",15))
total.grid(row=5,column=1,pady=10)

root.mainloop()
