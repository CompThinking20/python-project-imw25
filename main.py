import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import Text
import random
import os
import os.path


LARGE_FONT= ("Helvetica", 12)

class DigitalRepository(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        self.geometry("600x750")
        self.title("Local Repository") #figured out how to assign a new title to the window via the self atribute
        container.place(x=0,y=0)

        self.frames = {}
        #to be defined

        for F in (HomePage, FrameRecord, FrameListen):
            #Lists the frames for use

            frame = F(container, self)

            self.frames[F] = frame
            #Defines frames use to swap the page to another (hardest part with this entire section)

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(HomePage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()


class HomePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Welcome to the Repository!",font=LARGE_FONT, height=10,bd=1, relief="solid" )
        label.pack(pady=10,padx=10)

        button = tk.Button(self, text="Record",command=lambda: controller.show_frame(FrameRecord), width = "30",height ="2", bg = "brown2" )
        button.pack(pady=15)

        button2 = tk.Button(self, text="Listen",command=lambda: controller.show_frame(FrameListen), width = "30",height ="2", bg = "seagreen1" )
        button2.pack(pady=15)


class FrameRecord(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        #f1 = tk.Frame(width = 500, height = 500)
        label = tk.Label(self, text="Record", font=LARGE_FONT, bd=1, relief="solid")
        label.pack(anchor = CENTER)
        label2 = tk.Label(self, text="Please list your information in the programropriate boxes",height = 2)
        label2.pack(pady=0, anchor = CENTER)
        spacerlabel = tk.Label(self, text="_______________________________________________________________________________________________________________________")
        spacerlabel.pack(pady=1,anchor = CENTER)
        #Manually created a line for GUI display

        fullname_text = tk.Label(self, text = "FullName :")
        age_text = tk.Label(self,text = "Age :")
        date_text = tk.Label(self,text = "Date :")
        quote_text = tk.Label(self,text = "Quote :")

        fullname_text.place(x=15,y=80)
        age_text.place(x=15,y=160)
        date_text.place(x=15,y=240)
        quote_text.place(x=15,y=320)

        global fullname
        global age
        global date
        global quote

        #Allows them to be called outside of their function and utilized

        fullname = tk.StringVar()
        age = tk.IntVar()
        date = tk.StringVar()
        quote = tk.StringVar()
        #String Managers

        fullname_entry = tk.Entry(self, textvariable = fullname, width = "30")
        age_entry = tk.Entry(self, textvariable = age, width = "30")
        date_entry = tk.Entry(self,textvariable = date, width = "30")
        quote_entry = tk.Entry(self,textvariable = quote)
        #Entry boxes for submission of data

        fullname_entry.pack(padx=17,pady=30, anchor = "w")
        age_entry.pack(padx=17,pady=30, anchor = "w")
        date_entry.pack(padx=17,pady=30, anchor = "w")
        quote_entry.pack(padx=17,pady=30,ipadx=100,ipady=60, anchor = "w")

        def save_info():
            #Function Designed to save any user inputted data for the record function (though not yet connected)

            fullname_info = fullname.get()
            age_info = age.get()
            date_info = date.get()
            quote_info = quote.get()
            #Grabs data from entry to be used in the function
            print(fullname_info, age_info, date_info, quote_info)
            #Prints to consol
            save_path = (r'E:\Users\Ian\Documents\GitHub\python-project-imw25\sepository')

            #WARNING - This directory may need to be modified to be run on another users computer
            #Issue arrose in nameing the folder as \r kept being referenced when using the directory "repository"
            file_name = fullname_info
            #obtains file name from users "name" to be referenced as an individual file

            name = os.path.join(save_path, file_name)
            #Joins the new file save path with the file name

            file = open(name, "w")
            #Opens non-existant file and creates it using the previous strings
            #Originally was programending all information to one file but it was too costly to figure out a sorting method
            file.write("Name :" + fullname_info+"\n")
            file.write("Age :" + str(age_info)+ "\n")
            file.write("Date :" + date_info+"\n")
            file.write("Quote :" + quote_info+"\n")
            file.close
            #Writes and closes the file

            fullname_entry.delete(0, END)
            age_entry.delete(0, END)
            date_entry.delete(0, END)
            quote_entry.delete(0, END)
            #Clears Entry boxes

            messagebox.showinfo('Yes!', 'The Data has been sucessfully recorded!')
            #Confirmation Message
            button['state'] = DISABLED
            #Button disabled upon submission of data as to only allow one entry per person


        button = tk.Button(self,text="Submit Data",command=save_info, width = "30",height ="2", bg = "light green" )
        button.pack(padx=17,pady=20, anchor = "w")


        button1 = tk.Button(self, text="Back to Home",command=lambda: controller.show_frame(HomePage))
        button1.pack()


class FrameListen(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Listen", font=LARGE_FONT)
        label.pack(pady=10,padx=10)


        def selection():

            path = r"E:\Users\Ian\Documents\GitHub\python-project-imw25\sepository"

            global mylabel
            global mylabel1
            global mylabel2
            #Allows them to be called outside of their function and be destroyed upon refresh

            a = random.choice(os.listdir(path))
            with open(os.path.join(path, a), 'r') as f:
                mylabel=Label(self, text=f.read())
                mylabel.pack()
                print (f.readlines())
                f.close
                #Finds random file located in the designated custom directory "sepository" under path
                #opens the file reads and distributes it to a label to be displayed
                #prints to console for test before closing file

            b = random.choice(os.listdir(path))
            with open(os.path.join(path, b), 'r') as f:
                mylabel1=Label(self, text=f.read())
                mylabel1.pack()
                print (f.readlines())
                f.close

            c = random.choice(os.listdir(path))
            with open(os.path.join(path, c), 'r') as f:
                mylabel2=Label(self, text=f.read())
                mylabel2.pack(pady=10)
                print (f.readlines())
                f.close

            #Currently there is no code to prevent duplicate files from being selected

        def refresh():

            mylabel.destroy()
            mylabel1.destroy()
            mylabel2.destroy()
            #Destroys the labels indepedently (rather than from a label list as i wanted, but this was easier)
            selection()
            #Calls selection function


        selection()
        #[selection() for s in range(3)]
        #Unfortunately had to remove this code as I was unable to find a work around for the refresh button

        button1 = tk.Button(self, text="Back to Home", command=lambda: controller.show_frame(HomePage))
        button1.place(relx=0.5, rely=0.65, anchor = CENTER )
        #Used relx & y for these two buttons to properly position them
        #issue was upon refresh the buttons would scatter withhout reason and ignore anchors, I was lucky relx and rely worked

        button2 = tk.Button(self, text="Refresh", command = refresh)
        button2.place(relx=0.5, rely=0.7, anchor = CENTER )
        #Calls refresh function

program = DigitalRepository()
program.mainloop()
