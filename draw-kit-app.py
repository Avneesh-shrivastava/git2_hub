from tkinter import *

root = Tk()
root.geometry("400x500")
root.title("Draw Kit App")

canvas = Canvas(root,bg="white", width=400, height=475)
canvas.pack()

btn_frame = Frame(root)
btn_frame.pack()

color = "black"
brush_size = 3

def color_red():
    global color
    color = "red"

def color_green():
    global color
    color = "green"

def color_blue():
    global color
    color = "blue"

def color_yellow():
    global color
    color = "yellow"

def clear():
    canvas.delete("all")    



def brush_up():
    global brush_size
    brush_size += 1
    if brush_size < 0 :
        brush_size -= 1

def brush_down():
    global brush_size
    brush_size -= 1    
    if brush_size < 0 :
        brush_size += 1

def paint(event):
    x1 = event.x - brush_size
    y1 = event.y - brush_size
    x2 = event.x + brush_size
    y2 = event.y + brush_size
    canvas.create_oval(x1,y1,x2,y2,fill=color,outline=color)

canvas.bind("<B1-Motion>",paint)

red_color = Button(btn_frame,text="RED", command=color_red)
red_color.pack(side="left")

green_color = Button(btn_frame,text="GREEN", command=color_green)
green_color.pack(side="left")

blue_color = Button(btn_frame,text="BLUE", command=color_blue)
blue_color.pack(side="left")

yellow_color = Button(btn_frame,text="YELLOW", command=color_yellow)
yellow_color.pack(side="left")

clr = Button(btn_frame,text="CLEAR", command=clear)
clr.pack(side="left")

bru = Label(btn_frame,text="Brush size :")
bru.pack(side="left")

a = Button(btn_frame,text= "🔼",relief=RAISED,command=brush_up)
a.pack(side="left")
        
b = Button(btn_frame,text= "🔽",relief=RAISED,command= brush_down)
b.pack(side="left")

root.mainloop()
