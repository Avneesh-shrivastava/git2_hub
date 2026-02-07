from tkinter import *
from PIL import Image,ImageTk
root = Tk()
root.title("Netflix")
root.geometry("400x655")
root["background"] = "black"
frame = Frame(root)
frame.grid(row=0,column=0)

#Movies information
def intesteller_info():
    movie_info_text.delete("1.0","end")
    movie_info_text.insert(END,"\n\n\n")
    movie_info_text.insert(END,"Interstellar (2014)\n Genre: Historical Drama, Biography, Thriller\n Runtime: 3h 00m\n Rating: U/A 16+ (PG-13)\n Audio Languages: English, Hindi, Tamil, Telugu (depending on platform)\n Subtitle Languages: English, Hindi ")
    
def oppenhiemer_info():
    movie_info_text.delete("1.0","end")
    movie_info_text.insert(END,"\n\n\n")
    movie_info_text.insert(END,"Oppenhiemer (2023)\n Genre: Biography, Drama, History\n Director: Christopher Nolan\n Language: English\n Runtime: 3h\n IMDb Rating: 8.3 / 10")
    
def avengers_info(): 
    movie_info_text.delete("1.0","end")
    movie_info_text.insert(END,"\n\n\n") 
    movie_info_text.insert(END,"Avengers End Game (2019)\n Genre: Action, Adventure, Sci-Fi\n Director: Anthony Russo, Joe Russo\n Language: English\n Runtime: 3h 2m\n IMDb Rating: 8.4 / 10")

def dhurandhar_info():
    movie_info_text.delete("1.0","end")
    movie_info_text.insert(END,"\n\n\n") 
    movie_info_text.insert(END,"Dhurandhar (2026)\n Genre: Action, Thriller\n Director: Aditya dhar\n Language: Hindi\n Runtime: 3h 32m\n IMDb Rating: 8.4 / 10")
    
text = Text(frame,height=20,bd=4,relief="solid",wrap="none",width=50,bg="black")
text.grid(row=0,column=0)

img = Image.open("HD-wallpaper-interstellar-2014-movie-poster.jpg")
resized_img = img.resize((200,300))
img = ImageTk.PhotoImage(resized_img)
text.insert(END,"   ")

text.image_create(END,image=img)

text.insert(END,"   ")

img2 = Image.open("Oppenheimer-PosterSpy-4.jpg")
resized_img2 = img2.resize((200,300))
img2 = ImageTk.PhotoImage(resized_img2)
text.image_create(END,image=img2)
text.insert(END,"   ")

img3 = Image.open("images.jpg")
resized_img3 = img3.resize((200,300))
img3 = ImageTk.PhotoImage(resized_img3)
text.image_create(END,image=img3)
text.insert(END,"   ")

img4 = Image.open("MV5BMzFiNTVkZjYtM2I3Yi00MGNjLWEyYTAtMGViNGExZmMzMGMzXkEyXkFqcGc@._V1_.jpg")
resized_img4 = img4.resize((200,300))
img4 = ImageTk.PhotoImage(resized_img4)
text.image_create(END,image=img4)
text.insert(END,"   \n")

intersteller = Button(text,text="Intesteller",command=intesteller_info)
oppenhiemer =Button(text,text="Oppenhiemer",command=oppenhiemer_info)
avengers = Button(text,text="Avenger's end game",command=avengers_info)
dhurandhar = Button(text,text="Dhurandhar",command=dhurandhar_info)

text.insert(END,"            ")
text.window_create(END,window=intersteller)
text.insert(END,"                   ")
text.window_create(END,window=oppenhiemer)
text.insert(END,"                ")
text.window_create(END,window=avengers)
text.insert(END,"               ")
text.window_create(END,window=dhurandhar)

scroll = Scrollbar(root,orient="horizontal",command=text.xview,bg="black")
scroll.grid(row=1,column=0,sticky="ew")

movie_info_text = Text(root,bg="black",fg="white",width=50,wrap="none",height=18)
movie_info_text.grid(row=2,column=0,columnspan=10)

scroll_bar2 = Scrollbar(root,orient="horizontal",command=movie_info_text.xview,bg="black")
scroll_bar2.grid(row=3,column=0,sticky="ew")

root.mainloop()
