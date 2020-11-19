#fix error if client crashes out
#add error handling if argumnets not correct
from socket import AF_INET, socket, SOCK_STREAM 
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
            #print(msg[1:]+"\n")
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


client_socket = socket(AF_INET,SOCK_STREAM)
username = str(sys.argv[1])
hostName = str(sys.argv[2]) 
port = int(sys.argv[3])

client_socket.connect((hostName,port))
print('Welcome! If you want to quit, type quit to exit.')
receive_thread = Thread(target=receive)
receive_thread.start()
send(username)

while run==True:
   message=input("")
   if message:
      if message!="quit":
         send(username+": " + message)
      else:
         send(message)
         break
