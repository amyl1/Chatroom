#check server message if user leaves
import socket
import sys 

import tkinter as tk

from threading import Thread
from tkinter import messagebox
from tkinter import simpledialog
from tkinter import Radiobutton    

def showAllUsers():
    msg="DISPLAY"
    msgList.insert(tk.END, "Current Users:")
    client_socket.send(msg.encode())
    

def helpFunc():
    #Generate a pop-up window to display commands.
    popUp = tk.Tk()
    popUp.title("Help")
    popUp.geometry(f'{500}x{300}')
    m = """ 
        Welcome to the server!\n
        There is a menu containing the options to change your username,\n
        list all users, leave the chat or ask for help.\n
        Radio buttons are used to select whom you wish to send the message.\n
        If you select 'whisper', there will then be an input prompt\n
        where you type the name of the user you will send the message to.\n
        To leave the chat, you can either send the message'quit' or use the menubar.\n
        Messages cannot contain the '*' character as this is reserved by the server.
        """
    w = tk.Label(popUp, text=m, width=300, height=17)
    w.pack()
    b = tk.Button(popUp, text="OK", command=popUp.destroy, width=10)
    b.pack()
    tk.mainloop()

def changeName():
    name=""
    while not name:
        name = simpledialog.askstring("Change Username", "Please enter your new username")
    #send new username to server
    msg="USER"+name
    client_socket.send(msg.encode())
    global username
    username=name

def leaveFunc():
    messagebox.showinfo("Leave Chat", "You have left the chat")
    #disconnect the user
    msg="quit"
    client_socket.send(msg.encode())

def receive():
    while True:
        try:
            msg = client_socket.recv(1024).decode()
            #if user is leaving the server
            if msg=="quit":
                msgList.insert(tk.END, "You have left the server. You can now close the window")
                window.quit()
                client_socket.close()
                break
            #add recieved message to message list
            else:                
                msgList.insert(tk.END, msg)
        except:
            msgList.insert(tk.END, "Error. Please restart.")
            window.quit()
            break
   
def send():
    #get value from radio buttons and send to requested recipient
    msg=msgForm.get()
    msgForm.set("")
    if '*' in msg:
        msg="Messages cannot contain '*', please resend the message."
        msgList.insert(tk.END, msg)
    else:
        if radioValue.get () == 1:
            recp="ALL"
        else:
            recp=""
            while not recp:
                recp = simpledialog.askstring("Choose User", "Enter a username")
        msg=username+": "+msg +"*"+recp
        client_socket.send(msg.encode())

#set up tkinter window
window=tk.Tk()
window.title("Instant Messenger")
width  = window.winfo_screenwidth()
height = window.winfo_screenheight()
window.geometry(f'{width//2}x{height//2}')

#set up menu
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

#radio buttons, to select recipient
radioValue = tk.IntVar ()
radioValue.set(1)
Radiobutton(window, text = "Send to All", variable = radioValue, value = 1).grid(column=0, row=1)
Radiobutton(window, text = "Whisper", variable = radioValue,value = 2).grid(column=1, row=1)

#to display recieved messages
messages_frame=tk.Frame(window)
msgForm=tk.StringVar()
msgForm.set("Enter message: ")
scrollbar = tk.Scrollbar(messages_frame)
msgList = tk.Listbox(messages_frame, height=15, width=50, yscrollcommand=scrollbar.set)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y, expand=False)
msgList.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
msgList.pack()
messages_frame.grid(row=4)

#form to enter message to send
entryField = tk.Entry(window, textvariable=msgForm)
entryField.grid(column=0, row=5)
sendButton = tk.Button(window, text="Send", command=send)
sendButton.grid(column=1, row=5)

window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)

#check sys arguments
if len(sys.argv) != 4 :
   print ('Incorrect command line arguments given')
   sys.exit(1) 
try:
    port = int(sys.argv[3])
except ValueError:
    print ('Type error: Incorrect command line arguments given')
    sys.exit(1)

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
username = str(sys.argv[1])
hostName = str(sys.argv[2]) 
port = int(sys.argv[3])

while not username:
   username=input("Please enter a non-empty username")
#connect client to server
try:
   client_socket.connect((hostName,port))
except socket.error:
   sys.exit("Error connecting: please check the port and hostname")

msgList.insert(tk.END, 'Welcome! If you want to quit, type quit to exit.')

receive_thread = Thread(target=receive)
receive_thread.start()
client_socket.send(username.encode())
helpFunc()
window.mainloop()
