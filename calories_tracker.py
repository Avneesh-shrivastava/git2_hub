from tkinter import *
from tkinter import ttk
import pandas as pd
import csv
import os

root = Tk()
root.title("Calorie traker")
list = []
count = 0
limit = 0

dict = {
    "date":[],
    "food_item" : [],
    "calories" : []
}
df = pd.DataFrame(dict)

def data_to_csv():
    date = e_date.get()
    food_item = e_food.get()
    calories  = e_calories.get()
    file_open = os.path.isfile("my_data.csv")


    with open ("my_data.csv",mode="a",newline="") as file:
        writer = csv.writer(file)

        if not file_open:
            writer.writerow(["Date","Food_item","Calories"])
        writer.writerow([date,food_item,calories])

def add_data():
    
    data_to_csv()

    global count
    count = count + 1
    
    if count == 1:
        global limit
        limit = e_calorie_limit.get()
        calorie_limit.destroy()
        e_calorie_limit.destroy()
    
    limit2 = limit
    limit2 = int(limit2)

    table.insert("",END,values=(e_date.get(),e_food.get(),e_calories.get()))
    tot = int(e_calories.get())
    list.append(tot)
    c = sum(list)

    total_cal.config(text=f"Total calories : {c}")

    a = Label(text="")
    a.grid(row=8,column=1)

    if c == limit2:
        a.config(text="Calories limit over",font=("Arial",15,"bold"))

    e_date.delete(0,END)
    e_food.delete(0,END)
    e_calories.delete(0,END)

date = Label(text="Enter date : ")
date.grid(row=0,column=0)
e_date = Entry(root)
e_date.grid(row=0,column=1)

food = Label(text="Enter food type : ")
food.grid(row=2,column=0)
e_food = Entry(root)
e_food.grid(row=2,column=1)

calories = Label(text="Enter calories : ")
calories.grid(row=3,column=0)
e_calories = Entry(root)
e_calories.grid(row=3,column=1)

calorie_limit = Label(text="Enter your calorie limit : ")
calorie_limit.grid(row=4,column=0)
e_calorie_limit = Entry(root)
e_calorie_limit.grid(row=4,column=1)

button = Button(text="ADD",command=add_data)
button.grid(row=5,column=1,pady=20)

table = ttk.Treeview(root,columns=("Date","Food","Calories"),show="headings")
table.grid(row=6,column=0,columnspan=10)

table.heading("Date",text="Date")
table.heading("Food",text="Food")
table.heading("Calories",text="Calories")

total_cal = Label(text="Total calories : 0",font=("Arial",15))
total_cal.grid(row=7,column=1,pady=10)



root.mainloop()