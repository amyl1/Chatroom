from socket import AF_INET, socket, SOCK_STREAM 
import sys 
import time
from threading import Thread

def receive():
   try:
      msg = client_socket.recv(1024).decode("utf8")
   except:
      print("Error")
def send(msg):
    client_socket.send(bytes(msg, "utf8"))
    if msg == "quit":
        client_socket.close()


client_socket = socket(AF_INET,SOCK_STREAM)
username = str(sys.argv[1])
hostName = str(sys.argv[2]) 
port = int(sys.argv[3])

client_socket.connect((hostName,port))
receive_thread = Thread(target=receive)
receive_thread.start()

while True:
   message=input("Enter a message: ")
   if message:
      send(message)
   receive()

