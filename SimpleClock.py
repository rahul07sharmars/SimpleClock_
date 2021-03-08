from tkinter import *
from tkinter.ttk import *

from time import strftime

root = Tk()
root.title("Clock")
def time():
    #format of time
    string= strftime("%H:%M:%S %p")
    label.config(text=string)
    #update it every second
    label.after(1000, time)
#font of the text
label = Label(root, font=("ds-digital",80),background="black", foreground="cyan")
label.pack(anchor='center')
time()

mainloop()