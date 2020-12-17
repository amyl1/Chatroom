#check server message if user leaves
import socket
import sys 
import time
from threading import Thread
msg_list=[]
run=True
def receive():
   while True:
      try:
         msg = client_socket.recv(1024).decode()
         if msg!="quit":
            print(msg+"\n")
            print("Enter a message:")
         else:
            print("You have left the server")
            client_socket.close()
            run=False
            break
      except:
         print("Error!")
         run=False
         break
         
def send(msg):
    client_socket.send(msg.encode())

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
send(username)

while True:
   message=input("")
   if message:
      if message!="quit":
         send(username+": " + message)
      else:
         send(message)
         break
