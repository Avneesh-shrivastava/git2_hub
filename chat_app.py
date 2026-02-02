from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Chat app")
root.geometry("300x505")

def message():
    text_area.insert(END,a1.get() + "\n", "user")
    text_area.insert(END,reply() + "\n\n","bot")    

def reply():
    if a1.get() == "hi":
         return "hello"
    elif a1.get() == "how are you":
        return "I am fine, what about you?"
    else : 
         return "i didnt get it"       


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
button = Button(frame2,text="SEND",padx=7,pady=7,command=message)
button.pack(side="left")

text_area.tag_config(
     "user",
    foreground="white",
    background = "green",
    justify = "right",
)
text_area.tag_config(
    "bot",
    foreground="black",
    background="white" 
)

root.mainloop()