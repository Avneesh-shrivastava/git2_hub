from tkinter import *
from tkinter import filedialog
import tkinter as tk
import tkinter.scrolledtext as st
import subprocess
import tempfile
from tkinter import simpledialog,messagebox
import http.server
import socketserver
import threading
import webbrowser

root = Tk()
root.title("Collaborative code generator app")
root.geometry("900x600")
root.configure(background="black")

def generate_code():
    global prompt
    prompt = type_prompt.get()
    dict = {
        "hello world" : "print(\"hello world\")",

        "loop" : '''for i in range(1, 11):
    print(i) ''',

        "add two numbers" : """a = 5
b = 7
sum = a + b
    
print("Sum is:", sum)""",

    }
   
    if prompt == "hello world":
        a = dict["hello world"]
        code_box.insert(END,a)
    if prompt == "loop":
        a = dict["loop"]
        code_box.insert(END,a)
    if prompt == "add two numbers":
        a = dict["add two numbers"]
        code_box.insert(END,a)

def run_code():
    global process
    code = code_box.get("1.0",END)
    temp_file = tempfile.NamedTemporaryFile(delete=False,suffix=".py")
    temp_file.write(code.encode())
    temp_file.close()

    process = subprocess.run(
        ["python",temp_file.name],
        capture_output = True,
        text=True)
    
    terminal.insert(END,process.stdout) 
     
def start_server():
    port = 8080
    handler = http.server.SimpleHTTPRequestHandler
    httpd = socketserver.TCPServer(("",port),handler)
    print(f"serving at port : {port}")
    httpd.serve_forever()

    #this will open the web browser

i = 0
file_list = []
t = 0
def dropdown_functions(event):
    global i
    global file_path
    global file_list
    # if i == "push" print(i)or i == "save" or i == "save as" or i == "open":
    #     i = i + 1
    opt = variable.get()
    if i % 2 == 0 and opt == "save as":
        content = code_box.get("1.0",END)
        file_path = filedialog.asksaveasfilename()
        file_list.append(file_path)
        if file_path:
            with open(file_path,"w") as file:
                file.write(content)                      

    if i % 2 == 0 and opt == "save":
        try:
            save_content = code_box.get("1.0",END)
            with open(file_list[0],"a") as file_save:
                file_save.write(save_content)
                messagebox.showinfo("Done","File saved succesfully!")
        except IndexError:
            messagebox.showinfo("Not done","File not found, go to save_as to create a new file")
            pass
 
    if i % 2 == 0 and opt == "push":
        thread = threading.Thread(target=start_server) # This will make a thread for the server
        thread.daemon = True
        thread.start()

        try:
            file_name = simpledialog.askstring("File","Enter file name with its extention")
            pushed_code = code_box.get('1.0',END) # This code will make a new ".py" file  
            with open(file_name,"w") as file:  
                file.write(pushed_code)
            messagebox.showinfo("DOne","Code uploaded successfully")
        except TypeError:
            pass

        url = "http://localhost:8080" # this code will open "http://ipv4:8080"
        webbrowser.open(url)

    if i % 2 == 0 and opt == "open":
        try: 
            global t
            open_file = filedialog.askopenfilenames()
            print(len(open_file))
            with open(open_file[0],"r",encoding="utf-8") as file:
                content = file.read()
            code_box.delete("1.0",END)
            code_box.insert(END,content)
            
            t = t + 1
        except IndexError:
            pass

    if opt == "push" or opt == "save" or opt == "save as" or opt == "open":
        i = i + 1

top_bar = Frame(width=150,bg="darkgrey")
top_bar.pack()
top_bar.grid_propagate(False)

variable = tk.StringVar()
variable.set("File")

options = ["push","save","save as","open"]

file = tk.OptionMenu(top_bar,variable, *options)
file.pack(side="left")
file.bind("<Button-1>",dropdown_functions)
file.config(background="grey", padx=20)

run = Button(top_bar,text="▶",width=3,bg="darkgrey",command=run_code)
run.pack(padx=(750,10),side="right")

label = Label(root,text="Type prompt",fg="white",bg="black")
label.pack(pady=(10,0))

frame_prompt = Frame(root,bg="black")
frame_prompt.pack(pady=(5,15))
type_prompt = Entry(frame_prompt,width=40)
type_prompt.pack(side="left",padx=(50,0))
search_prompt = Button(frame_prompt,text="Generate code",command=generate_code) 
search_prompt.pack(side="right", padx=10)

code_box =st.ScrolledText(root,bg="darkgrey",height=22,width=120,font=("Arial",10,"bold"))
code_box.pack(pady=10)

terminal = st.ScrolledText(root,bg="black",height=10,width=100,fg="white")
terminal.pack()

root.mainloop()
