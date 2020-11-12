import socket  
import sys
import time

server=socket.socket()
port = int(sys.argv[1])
server.bind(('',port))
print("server done binding to host and port successfully")
print("Waiting for connections...")
#maximum of 20 connections
server.listen(20)
connection,address= server.accept()
#replace with username

display_mess= (" {} has connected to the server and is now online...".format(address))
display_mess=display_mess.encode()
connection.send(display_mess)
print(" message has been sent...")
while True: 

   in_message=connection.recv(1024)
   in_messagge=in_message.decode()
   print(in_message)