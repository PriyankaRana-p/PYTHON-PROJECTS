from tkinter import*
from tkinter.ttk import*
from time import strftime

root=Tk()
root.title("Clock")
 
def time():
    string=strftime('%H:%H:%S %p')
    Label.config(text=string)
    Label.after(1000,time) 

Label=Label(root,font=("ds=digital",80),background="black",foreground="white")
Label.pack(anchor="center")
time()

mainloop()