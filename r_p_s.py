from tkinter import *
import random

root = Tk()
root.title("ROCK - PAPER - SCISSORS")
root.geometry("400x300")

global p_list 
c_list = ["r","p","s"]

def rock_clicked():
    global p_list
    p_list = "r"
    color()
def paper_clicked():
    global p_list
    p_list = "p"
    color()
def scissor_clicked():
    global p_list
    p_list = "s"
    color()

count = 0
player = 0
computer = 0

global rock
global paper
global button

def color():
    if p_list == "r":
        rock.config(bg="yellow")
    elif p_list == "p" :
        paper.config(bg="yellow")
    elif p_list == "s" :
        button.config(bg="yellow")
    
    if p_list != "r":
        rock.config(bg="white",fg="black")
    if p_list != "p":
        paper.config(bg="white",fg="black")
    if p_list != "s":
        button.config(bg="white",fg="black")

def comp():
    global computer
    global player
    global count
    a5 = Entry(root,width=40,font=("Arial",13,"bold"))
    a5.grid(row=6,column=0,columnspan=5)

    c_choice = random.choice(c_list) 
  #rock
    if c_choice == "r" and p_list == "r":
        a5.insert("end","You both chose rock TIE!")
    elif c_choice == "r" and p_list == "p":
        a5.insert("end","YOU WON THE ROUND ")
        player = player + 1 
    elif c_choice == "r" and p_list == "s":
        a5.insert("end","COMPUTER WON THE ROUND")
        computer = computer + 1  
  #scissor
    elif c_choice == "s" and p_list == "s":
        a5.insert("end","You both chose scissor TIE!")
    elif c_choice == "s" and p_list == "p":
        a5.insert("end","COMPUTER WON THE ROUND")                 
        computer = computer + 1
    elif c_choice == "s" and p_list == "r":
        a5.insert("end","YOU WON THE ROUND")
        player = player + 1
  #paper
    elif c_choice == "p" and p_list == "p":
        a5.insert("end","you both chose paper TIE!")
    elif c_choice == "p" and p_list == "s":
        a5.insert("end","YOU WON THE ROUND")
        player = player + 1
    elif c_choice == "p" and p_list == "r":
        a5.insert("end","COMPUTER WON THE ROUND")
        computer = computer + 1    

    else : 
        a5.insert("end","nobody wins") 

#final result
    def reset():
        global player,computer
        computer = 0
        player = 0
    if player > 2:
        a5.delete(0,END)
        a5.insert("end","PLAYER WINS !")
        if player > 2 or computer > 2 :
            reset()
    elif computer > 2:
        a5.delete(0,END)
        a5.insert("end","COMPUTER WINS !")
        if computer > 3 or computer > 2 :
            reset()

    count = count + 1

    a6 = Label(text="player : " + str(player) + "  " "computer : " + str(computer),font=("Arial",11,"bold"))
    a6.grid(row=7,column=1,pady=10)

def st():
    global rock
    global paper
    global button
    a1.destroy()
    a2 = Label(text='CHOOSE ANY ONE',font = ("Arial",10,"bold"))
    a2.grid(row=2,column=0,padx=100,columnspan=5)
    rock = Button(text="✊",font=("Arial",15,"bold"),command=rock_clicked)
    rock.grid(row=4,column=0,pady=40,padx=40)
    paper = Button(text="✋",font=("Arial",15,"bold"),command=paper_clicked)
    paper.grid(row=4,column=1,pady=40,padx=40)
    button = Button(text="✌️",font=("Arial",15,"bold"),command=scissor_clicked)
    button.grid(row=4,column=2,pady=40,padx=40)
    a4 = Button(text='OK', command=comp)
    a4.grid(row=5,column=1,pady=10)
    
a = Label(text='')
a.grid(row=0,column=0)

a1 = Button(text='START',command=st)
a1.grid(row=1,column=2,padx=175)

a3 = Label(text='')
a3.grid(row=3,column=0)

root.mainloop()





