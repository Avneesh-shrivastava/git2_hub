import shutil
from tkinter import *
import webbrowser
import threading
import http.server
import socketserver
from tkinter import filedialog

src = ()
root = Tk()
root.title("File sharing app")

def choose_file():
    global src
    src = filedialog.askopenfilenames()
    print(src)
    d.insert(END,src)
    button1.destroy()

def start_server():
    port = 8080
    handler = http.server.SimpleHTTPRequestHandler
    httpd = socketserver.TCPServer(("",port),handler)
    print(f"Serving at port {port}")
    httpd.serve_forever()

def open_site(event):
   #this will open the link
   url = "http://192.168.29.99:8080"
   webbrowser.open_new(url)

def file_upload():
    recieve.destroy()
    global src
    thread = threading.Thread(target=start_server)
    thread.daemon = True
    thread.start()

    d.config(text="Now open this link on your Phone Browser ")

    e = Label(text="http://(your computer ipv4 address):8080",fg="blue",cursor="hand2")
    e.grid(row=5,column=0)
    e.bind("<Button-1>",open_site) #this will make the e widget clickable

    #this will move the file from source to destination
    source_path = src[0]
    destination_path = r"D:\\server"

    try:
        shutil.copy2(source_path,destination_path)
        print("File successfully uploaded")
    except shutil.Error as e:
        print(f"Error moving file {e}")
    except FileNotFoundError:
        print(f"File not found : {source_path}")

a = Label(root,height=5,width=70)
a.grid(row=0,column=0,columnspan=1)

b = Label(text="Share files",font=("Arial",15))
b.grid(row=1,column=0)

button1 = Button(text="Select file",command=choose_file)
button1.grid(row=2,column=0,pady=10)

button = Button(text="Upload file",command=file_upload)
button.grid(row=3,column=0,pady=10)

d = Entry(root,width=50)
d.grid(row=4,column=0,columnspan=1)

recieve = Button(text="Recieve file",command=file_upload)
recieve.grid(row=5,column=0,pady=10)

root.mainloop()