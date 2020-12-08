import tkinter
import random
from tkinter import messagebox
from tkinter import Text
#from backforth import temp_frame

def save_info():
    #Function Designed to save any user inputted data for the record function (though not yet connected)
    fullname_info = fullname.get()
    age_info = age.get()
    date_info = date.get()
    quote_info = quote.get()
    #Grabs data from entry to be used in the function
    print(fullname_info, age_info, date_info, quote_info)
    #Prints to consol
    file = open("recordings.txt", "a")
    #Appends data to file as to not overwrite existing data
    file.write("\n")
    file.write("Name :" + fullname_info)
    file.write("\n")
    file.write("Age :" + str(age_info))
    file.write("\n")
    file.write("Date :" + date_info)
    file.write("\n")
    file.write("Quote :" + quote_info)
    file.close
    #Saves and writes to file

window = tkinter.Tk() # Initializes tkinter
window.title("Local Repository") # Name of the window
window.geometry("600x750") # Size of the window
header = tkinter.Label(text = "Ephemeral Voices - Your Digital Timecapsule", bg= 'white', fg= 'black')
# Header at top of the page

fullname_text = tkinter.Label(text = "FullName :")
age_text = tkinter.Label(text = "Age :")
date_text = tkinter.Label(text = "Date :")
quote_text = tkinter.Label(text = "Quote :")

fullname_text.place(x=15,y=70)
age_text.place(x=15,y=140)
date_text.place(x=15,y=210)
quote_text.place(x=15,y=280)

fullname = tkinter.StringVar()
age = tkinter.IntVar()
date = tkinter.StringVar()
quote = tkinter.StringVar()

fullname_entry = tkinter.Entry(textvariable = fullname, width = "30")
age_entry = tkinter.Entry(textvariable = age, width = "30")
date_entry = tkinter.Entry(textvariable = date, width = "30")
quote_entry = tkinter.Entry(textvariable = quote, width = "30")
#Encountered error when opening program this time. It appears to not recognize any height values and all internet work-arounds
#thus far have proven insuficient

fullname_entry.place(x=15,y=100)
age_entry.place(x=15,y=180)
date_entry.place(x=15,y=260)
quote_entry.place(x=15,y=340)

button = tkinter.Button(window,text="Submit Data",command=save_info,width = "30",height ="2", bg = "grey" )
button.place(x=15,y=390)

def record():
    messagebox.showinfo('Notice', 'These features are currently a work in progress')
#Test function which is called by a lambda command on the press of the following Button(s)
def listen():
    messagebox.showinfo('Notice', 'These features are currently a work in progress')
#Test function which is called by a lambda command on the press of the following Button(s)
def relate():
    messagebox.showinfo('Notice', 'These features are currently a work in progress')
#Test function which is called by a lambda command on the press of the following Button(s)

e = tkinter.Button(window, text="Record", fg="red", command=lambda: record())
e.place(x=120,y=100)

c = tkinter.Button(window, text="Listen", fg="blue", command=lambda: listen())
c.place(x=240,y=100)

d = tkinter.Button(window, text="Relate", fg="green", command=lambda: relate())
d.place(x=345,y=100)
#Button Experimentation to call a function, from research online I found lambda as a work around






header.pack() # Packs code into frame
window.mainloop() # keep window open



#Test Code I was working with to write to file so I can create a repository of people/images/quotes
#with open('test.txt', 'r+') as f:
    #f_contents = f.read()
    #print(f_contents)

#print(f.name)
