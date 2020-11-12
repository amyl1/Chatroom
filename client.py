from socket import AF_INET, socket, SOCK_STREAM 
import sys 
import time
from threading import Thread
msg_list=[]

def receive():
   try:
      msg = client_socket.recv(1024).decode()
      msg_list.append(msg)
   except:
      print("Error!")
def send(msg):
    client_socket.send(msg.encode())
    if msg == "quit":
        client_socket.close()


client_socket = socket(AF_INET,SOCK_STREAM)
username = str(sys.argv[1])
hostName = str(sys.argv[2]) 
port = int(sys.argv[3])

client_socket.connect((hostName,port))
receive_thread = Thread(target=receive)
receive_thread.start()
send(username)
receive()
while True:
   for i in range(len(msg_list)):
      print(msg_list.pop())
   message=input("Enter a message: ")
   if message:
      send(username+": " + message)
   receive()