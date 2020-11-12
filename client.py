from socket import AF_INET, socket, SOCK_STREAM 
import sys 
import time
from threading import Thread
msg_list=[]

def receive():
   while True:
      try:
         msg = client_socket.recv(1024).decode()
         print(msg+"\n")
         print("Enter a message:")
      except:
         print("Error!")
         break
def send(msg):
    client_socket.send(msg.encode())
    if msg == "quit":
        client_socket.close()


client_socket = socket(AF_INET,SOCK_STREAM)
username = str(sys.argv[1])
hostName = str(sys.argv[2]) 
port = int(sys.argv[3])

client_socket.connect((hostName,port))
print('Welcome! If you ever want to quit, type quit to exit.')
receive_thread = Thread(target=receive)
receive_thread.start()
send(username)

while True:
   message=input("")
   if message:
      send(username+": " + message)