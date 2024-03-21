from get_joke import get_chuck_norris_joke
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

window = tk.Tk()
window.title('Chuck Norris')
window.geometry('600x400+50+50')

window.iconbitmap("chuck_norris_icon.ico")

def show_joke():
    chuck_norris_data = get_chuck_norris_joke()
    value = chuck_norris_data["value"]
    
    label.config(text = value)
    
    # messagebox.showinfo("Message",value)
    
chuck_norris_data = get_chuck_norris_joke()
value = chuck_norris_data["value"]

image1 = Image.open("chuck_norris_icon.png")
chuck_image = ImageTk.PhotoImage(image1)
picture = Label(image=chuck_image)
# picture.image = test
picture.pack()

tk.Button(text= "New Joke", command=show_joke).pack(pady= 20)

label = tk.Label(text=value, wraplength=500, justify="center")
label.pack()

window.mainloop()
