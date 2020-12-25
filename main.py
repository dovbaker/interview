from tkinter import *
from _tkinter import *

from time import strftime

root = Tk()
root.title("Clock")

def time ():
    str = "every second\n has a purpose"
    string = strftime('%H:%M:%S \n'+  str)
    label.config(text=string)
    label.after(1000,time)

label = Label (root , font= ("ds_digital",30),background="black",foreground ="blue")
label.pack(anchor='center')
time()

mainloop()
