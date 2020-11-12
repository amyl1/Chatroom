import socket 
import sys 
import time
        
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
username = str(sys.argv[1])
hostName = str(sys.argv[2]) 
port = int(sys.argv[3])

server=socket.socket()
server.connect((hostName,port))
print('Connected to the chat server')

while True: 
   incoming_message=server.recv(1024)
   incoming_message=incoming_message.decode()
   print(" Server :", incoming_message)
   message= input(str("Enter a message:"))
   message =message.encode()
   server.send(message)
   print(" message has been sent...")