from tkinter import *
import requests
from PIL import Image,ImageTk 



root = Tk()
root.title("weather app")
root.geometry("400x600")

def space():
    space = Label(text="")
    space.grid(row=1,column=0)

def get_weather():
    city = d.get()
    api_url = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=2ad3f9acfa575c20b470b82630e5d3c0"
    json_data = requests.get(api_url).json()
    condition = json_data["weather"][0]["main"]
    temp = int(json_data["main"]["temp"] - 273.15 )
    pressure = int(json_data["main"]["pressure"])
    humidity = int(json_data["main"]["humidity"])

    temp_text = "weather :" + condition +"\n"+ "temperature : " + str(temp) + "℃"
    h_p_text = "humidity : " + str(humidity) + "\n" + "pressure : " + str(pressure)

    space = Label(text="",font=("Arial",7,"bold"),pady=40)
    space.grid(row=8,column=0)
    space = Label(text="Showing weather report of : "+city ,font=("Arial",15,"bold"))
    space.grid(row=9,column=0)

    t = Label(text=temp_text,font=("Arial",15,"bold"))
    t.grid(row=10,column=0)

    g = Label(text=h_p_text,font=("Arial",15,"bold"))
    g.grid(row=11,column=0)

a = Label(text="WEATHER APP", font =("Arial", 18, "bold"), fg = "blue", padx=110,bg="lightblue",pady=50)
a.grid(row=0, column=0)

space()

b = Label(text="Let's find out what's the weather today", font=("Arial", 14, "bold"))
b.grid(row=2,column=0)

space1 = Label(text=" ")
space1.grid(row=3,column=0)


d = Entry(width=30, font=("Ariel", 15))
d.grid(row=5,column=0)
#d.insert(0,"Enter city : ")

space2 = Label(text=" ")
space2.grid(row=6,column=0)

butt = Button(text="Check weather",relief=GROOVE, activebackground="yellow",bg="lightblue",
font=("helventica", 10,"bold"),
padx=5,
pady=5,
command=get_weather
)
butt.grid(row=7,column=0)

image = Image.open("weather-2021-12-07.webp")
image = image.resize((50, 50))
photo = ImageTk.PhotoImage(image)

img = Label(image=photo, bd=4,pady=200)
img.grid(row=6,column=0,columnspan=4)

root.mainloop()

