from tkinter import *
# import requests
import time
import yfinance as yf
import threading

root = Tk()
root.geometry("500x600")

current_price = 1
list = []

# global rounded_price
# l = rounded_price
# print(l)

def getting_data():
    stock = yf.Ticker("AAPL")
    a = stock.info
    stock_name = a["longName"]
    stock_display.config(text=f"stock : {stock_name}")

    data = stock.history(period="1d", interval="1m")
    price = data["Close"].iloc[-1]
    
    rounded_price = round(price,2)
    price_display.config(text=f"price : {rounded_price} USD")
    
    l = price
    time.sleep(1)
    
    print("l = ",l)
    print("rounded = ",price)
 

def get_data_loop():
    while True:
        getting_data()
        time.sleep(1)


#threading
thread = threading.Thread(target=get_data_loop)
thread.daemon = True
thread.start()

stock_display = Label(text=f"stock : ",font=("Arial",20,"bold"))
stock_display.pack(side="top",pady=(50,30))

price_display = Label(text=f"Price : ",font=("Arial",15,"bold"))
price_display.pack(side="top")

canvas = Canvas(root,bd=1,relief="solid")
canvas.pack()


root.mainloop()



