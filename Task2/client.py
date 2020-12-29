import tkinter as tk
from tkinter.ttk import *

def changeName():
    res="Change Name"
    lbl1.configure(text=res,font=("Arial Bold", 10))

def showAllUsers():
    res="All users"
    lbl1.configure(text=res,font=("Arial Bold", 10))

def helpFunc():
    res="Help"
    lbl1.configure(text=res,font=("Arial Bold", 10))

def leaveFunc():
    res="Leave"
    lbl1.configure(text=res,font=("Arial Bold", 10))

def send():
    res="Send"
    lbl1.configure(text=res,font=("Arial Bold", 10))


window=tk.Tk()
window.title("Instant Messenger")
width  = window.winfo_screenwidth()
height = window.winfo_screenheight()
window.geometry(f'{width//2}x{height//2}')

menubar=tk.Menu(window)

nameMenu=tk.Menu(menubar, tearoff=0)
nameMenu.add_command(label="Change Username", command=changeName)
menubar.add_cascade(label="Username", menu=nameMenu)

userMenu=tk.Menu(menubar, tearoff=0)
userMenu.add_command(label="Show List of Users",command=showAllUsers)
menubar.add_cascade(label="Show Users", menu=userMenu)

helpMenu=tk.Menu(menubar, tearoff=0)
helpMenu.add_command(label="Help",command=helpFunc)
menubar.add_cascade(label="Help", menu=helpMenu)

leaveMenu=tk.Menu(menubar, tearoff=0)
leaveMenu.add_command(label="Leave the chat",command=leaveFunc)
menubar.add_cascade(label="Leave", menu=leaveMenu)

window.config(menu=menubar)

Radiobutton(window, text = "Send to All", value = 1).grid(column=0, row=1)
Radiobutton(window, text = "Whisper", value = 2).grid(column=1, columnspan = 2, row=1)

frm_messages = tk.Frame(master=window)
scrollbar = tk.Scrollbar(master=frm_messages)
messages = tk.Listbox(
    master=frm_messages, 
    yscrollcommand=scrollbar.set
)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y, expand=False)
messages.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
frm_messages.grid(row=2, column=0, columnspan=2, sticky="nsew")

lbl1 = Label(window, text="Enter a message:", font=("Arial Bold", 10))
lbl1.grid(column=0, row=4)

msg = Entry(window,width=80)
msg.grid(column=0, row=3, columnspan = 1)
btn = Button(window, text="Send",command=send)
btn.grid(column=1, row=3)
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)

window.mainloop()