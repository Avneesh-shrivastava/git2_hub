from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from PIL import Image,ImageTk
import tkinter.scrolledtext as st
import pandas as pd
import csv
import os

dict1 = {
    "username_" : [],
    "password_" : [],
    "images" : []
}
df = pd.DataFrame(dict1)



root = Tk()
root.title("SUDO")
root.geometry("400x600")

username_list = []
password_list = []

is_post = False
count = 1
post = ""
is_acc_logged_in = False
list = []
new_session = False

def choose_file():#this function opens a file selection dialog box
    global post    
    post = filedialog.askopenfilename()

def check_new_session():
    global new_session
    new_session = True
    login_page() 

def upload_page():
    upload = Frame(root,width=400,height=600,bg="white")
    upload.pack_propagate(False)
    upload.grid(row=0,column=0)

    choose = Button(upload,text="Choose file",bg="purple",fg="yellow",command=choose_file)
    choose.pack(pady=(100,30))

    back = Button(upload,text="Back",bg="purple",fg="yellow",command=home_page)
    back.pack(pady=30)

def profile():
    profile_name = username_entry.get()

    profile_frame = Frame(root,width=400,height=600,bg="white")
    profile_frame.grid(row=0,column=0)
    profile_frame.pack_propagate(False)
    name = Label(profile_frame,text=profile_name,bg="white")
    name.pack(side="top")

    back = Button(profile_frame,text="⬅",bg="purple",command=home_page)
    back.pack(side="top",anchor="w")

    logout = Button(profile_frame,text="Log out",bg="red",command=check_new_session)
    logout.pack(side="bottom")

    text_area = st.ScrolledText(profile_frame,height=30,width=20,bd=1,relief="solid")
    text_area.pack(pady=50)

    global post
    global list
    list.append(post)
    print(list)
    is_post = True

    if is_post:
        for x in list:
            if x == "":
                continue

            img = Image.open(x)
            img_resize = img.resize((50,50))
            img = ImageTk.PhotoImage(img_resize)
            # list.append(img)
            
            text_area.insert(END,"\n")

    #         image = Label(text_area,image=img)
    #         image.image = img
    #         text_area.window_create(INSERT,window=image)


def home_page():
    global count
    home_frame = Frame(root,width=400,height=600,bg="white")
    home_frame.pack_propagate(False)
    home_frame.grid(row=0,column=0)

    header = Frame(home_frame,width=400,height=40,bg="purple",color="")
    header.pack_propagate(False)
    header.pack()
    
    text_area = st.ScrolledText(home_frame,bd=1,relief="solid",height=300,width=50,wrap="none")
    text_area.pack()
    
    profile_button = Button(header,text="🧑",bg="yellow",command=profile)
    profile_button.pack(side="right",padx=10)

    upload_button = Button(header,text="⬆",bg="yellow",height=0,width=2,command=upload_page)
    upload_button.pack(side="right",padx=8)

    global post
    global list
    list.append(post)
    print(list)
    is_post = True

    global new_session
    if new_session == False:
        if is_post:
            for x in list:
                if x == "":
                    continue

                img = Image.open(x)
                img_resize = img.resize((300,350))
                img = ImageTk.PhotoImage(img_resize)
                
                text_area.insert(END,"\n")

                image = Label(text_area,image=img)
                image.image = img
                text_area.window_create(INSERT,window=image)
                text_area.config(
                    padx=20,
                    pady=20,
                )
                text_area.insert(END,"\n")
                a = Button(text="   ❤️")
                
                text_area.window_create(INSERT,window=a)


def signup_logic():
    global username_entry_signup
    _username_ = username_entry_signup.get()
    _password_ = password_entry_signup.get()

    if _username_ and _password_:
        messagebox.showinfo("Done","Account created successfully")
    else:
        messagebox.showinfo("Not Done","Account Not Created")

#creating a csv file and storing the user and password in it
    file_open = os.path.isfile("user_idnp.csv")

    with open("user_idnp.csv",mode="a",newline="") as file:
        writer = csv.writer(file)
        if not file_open:
            writer.writerow(["_username_","_password_"])

        writer.writerow([_username_,_password_])

def login_logic():
    username = str(username_entry.get())
    password = str(password_entry.get())
    print(username)
    print(password)

    data = pd.read_csv("user_idnp.csv")
    if username in data["_username_"].values and password in data["_password_"].values:
        home_page()
    else:
        messagebox.showinfo("Error","Account not created")

    
def signup_page():
    login = Frame(width=400,height=600,bd=0,relief="solid",bg="purple")
    login.pack_propagate(False)
    login.grid(row=0,column=0)

    a = Label(login,text="SUDO",font=("Helvetica",20,"bold"),fg = "yellow",bg="purple")
    a.pack()
    slogan = Label(login,text="share your thoughts and memories",font=("Helvetica",8,"bold"),fg="white",bg="purple")
    slogan.pack()
    username_ = Label(login,text="Username",fg="white",bg="purple",font=("Helvetica",10,"bold"))
    username_.pack(pady=(100,5))
    global username_entry_signup
    username_entry_signup = Entry(login,width=30)
    username_entry_signup.pack()

    password_ = Label(login,text="Password",fg="white",bg="purple",font=("Helvetica",10,"bold"))
    password_.pack(pady=(30,5))
    global password_entry_signup
    password_entry_signup = Entry(login,width=30)
    password_entry_signup.pack()

    signup = Button(login,text="Create account",command=signup_logic)
    signup.pack(pady=(50,5))

    go_back = Button(login,text="back",command=login_page)
    go_back.pack(pady=30)
    
def login_page():
    login = Frame(width=400,height=600,bd=0,relief="solid",bg="purple")
    login.pack_propagate(False)
    login.grid(row=0,column=0)

    a = Label(login,text="SUDO",font=("Helvetica",20,"bold"),fg = "yellow",bg="purple")
    a.pack()
    slogan = Label(login,text="share your thoughts and memories",font=("Helvetica",8,"bold"),fg="white",bg="purple")
    slogan.pack()
    username_ = Label(login,text="Username",fg="white",bg="purple",font=("Helvetica",10,"bold"))
    username_.pack(pady=(100,5))
    global username_entry
    username_entry = Entry(login,width=30)
    username_entry.pack()

    password_ = Label(login,text="Password",fg="white",bg="purple",font=("Helvetica",10,"bold"))
    password_.pack(pady=(30,5))
    global password_entry
    password_entry = Entry(login,width=30)
    password_entry.pack()

    login_button = Button(login,text="Login",command=login_logic)
    login_button.pack(pady=(50,5))
    
    signup = Button(login,text="Sign-up",command=signup_page)
    signup.pack(pady=30)

    
        
login_page()

root.mainloop()
