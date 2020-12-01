import tkinter
import random
from tkinter import messagebox



window = tkinter.Tk() # Initializes tkinter
window.title("Local Repository") # Name of the window
window.geometry("600x750") # Size of the window
header = tkinter.Label(text = "Ephemeral Voices - Your Digital Timecapsule", bg= 'white', fg= 'black')
# Header at top of the page

def record():
    messagebox.showinfo('Notice', 'These features are currently a work in progress')
#Test function which is called by a lambda command on the press of the following Button(s)

e = tkinter.Button(window, text="Record Your Voice", fg="red", command=lambda: record())
e.place(x=120,y=100)

c = tkinter.Button(window, text="Listen to Others", fg="blue", command=lambda: record())
c.place(x=240,y=100)

d = tkinter.Button(window, text="Relate to Others", fg="green", command=lambda: record())
d.place(x=345,y=100)

#Button Experimentation to call a function, from research online I found lambda as a work around

header.pack() # Packs code into frame
window.mainloop() # keep window open



#Test Code I was working with to write to file so I can create a repository of people/images/quotes 
#with open('test.txt', 'r+') as f:
    #f_contents = f.read()
    #print(f_contents)

#print(f.name)
