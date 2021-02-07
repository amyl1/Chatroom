#check server message if user leaves
import socket
import sys 
import time
import tkinter as tk
from threading import Thread
from tkinter import messagebox
from tkinter import simpledialog
    

def showAllUsers():
    msg="DISPLAY"
    client_socket.send(msg.encode())

def helpFunc():
    messagebox.showinfo("Title", "a Tk MessageBox")

def changeName():
    name = simpledialog.askstring("Change Username", "Please enter your new name")
    msg="USER"+name
    client_socket.send(msg.encode())


def leaveFunc():
    messagebox.showinfo("Leave Chat", "You have left the chat")
    msg="quit"
    client_socket.send(msg.encode())

def receive():
    while True:
        try:
            msg = client_socket.recv(1024).decode()
            if msg=="quit":
                print("You have left the server")
                client_socket.close()
                window.quit()
                break
            else:                
                print(msg+"\n")
            msg_list.insert(tk.END, msg)
            #msg_list.insert(msg)
        except:
            print("Error!")
            break
   
def send():
    msg=username+": "+msgForm.get()
    msgForm.set("")
    client_socket.send(msg.encode())



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
"""
Radiobutton(window, text = "Send to All", value = 1).grid(column=0, row=1)
Radiobutton(window, text = "Whisper", value = 2).grid(column=1, columnspan = 2, row=1)
"""
messages_frame=tk.Frame(window)
msgForm=tk.StringVar()
msgForm.set("Enter message: ")
scrollbar = tk.Scrollbar(messages_frame)
msg_list = tk.Listbox(messages_frame, height=15, width=50, yscrollcommand=scrollbar.set)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y, expand=False)
msg_list.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
msg_list.pack()
messages_frame.grid(row=4)

entry_field = tk.Entry(window, textvariable=msgForm)
#entry_field.bind("<Return>", send)
entry_field.grid(column=0, row=5)
send_button = tk.Button(window, text="Send", command=send)
send_button.grid(column=1, row=5)

window.columnconfigure(0, weight=2)
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
try:
   client_socket.connect((hostName,port))
except socket.error:
   sys.exit("Error connecting: please check the port and hostname")
print('Welcome! If you want to quit, type quit to exit.')
receive_thread = Thread(target=receive)
receive_thread.start()
client_socket.send(username.encode())

window.mainloop()