from tkinter import *
from tkinter.ttk import *

def clicked():
    res="Messge was "+txt.get()
    lbl.configure(text=res,font=("Arial Bold", 10))
def showAllUsers():
    res="All users"
    lbl.configure(text=res,font=("Arial Bold", 10))

window=Tk()
window.title("Instant Messenger")
window.geometry('800x400')

lbl = Label(window, text="Hello", font=("Arial Bold", 10))
lbl.grid(column=0, row=0)

combo = Combobox(window)

combo['values']= ("Send to everyone","Send to one user")

combo.current(1) #set the selected item

combo.grid(column=1, row=1)

btn = Button(window, text="Show all users",command=showAllUsers)
btn.grid(column=1, row=2)

lbl1 = Label(window, text="Enter a message:", font=("Arial Bold", 10))
lbl1.grid(column=0, row=3)
txt = Entry(window,width=80)
txt.grid(column=1, row=3)
btn = Button(window, text="Send",command=clicked)
btn.grid(column=2, row=3)
window.mainloop()