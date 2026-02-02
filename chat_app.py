from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Chat app")
root.geometry("300x505")



def bot_reply():
    text_area.insert(END,reply() + "\n", "bot")


def reply():
    global c
    if c == "hi":
         return "hello"
    elif c == "how are you":
        return "I am fine, what about you?"
    else : 
         return "i didnt get it"       

def message(event=None):
    global c
    c = a1.get()
    text_area.insert(END,c + "\n", "user")
    a1.delete(0,END)   
    root.after(1000,bot_reply())


a = Label(root,text="",bd=1,relief="solid",height=2,width=43,bg="green")
a.grid(row=0,column=0,columnspan=5)

frame = Frame(root)
frame.grid(row=0,column=0)

img = Image.open("weather-2021-12-07.webp")
img1 = img.resize((21,21))
img = ImageTk.PhotoImage(img1)
image = Label(frame,image=img,bd=0)
image.pack(side="left")

name = Label(frame,text="Chat bot",bg="green",fg="white",padx=15)
name.pack(side="left")

text_area = Text(root,width=37,bg="lightgrey",height=27)
text_area.grid(row=1,column=0,columnspan=9)

text_area2 = Text(root)
text_area2.grid(row=3,column=0,columnspan=10)

frame2 = Frame(text_area2,width=10)
frame2.grid(row=3,column=0,columnspan=3)

a1 = Entry(frame2,width=16,font=('Arial',20,'bold'))
a1.pack(side="left")

c = a1.get()

button = Button(frame2,text="SEND",padx=7,pady=7,command=message)
button.pack(side="left")

a1.bind("<Return>", message)
text_area.tag_config(
     "user",
    foreground="white",
    background = "green",
    justify = "right",
    font=("Arial",16)
)
text_area.tag_config(
    "bot",
    foreground="black",
    background="white",
    font=("Arial",16) 
)


root.mainloop()