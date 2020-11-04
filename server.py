
import socket 
import select 
import sys 

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
  

# takes the first argument from command prompt as IP address 
hostName = ''
  
# takes second argument from command prompt as port number 
Port = int(sys.argv[1]) 
server.bind((hostName, Port)) 
  
#listens for 100 active connections.

server.listen(100) 

current_users=[]
while True:
    clientsocket, address = server.accept()
    current_users.append(clientsocket)
    for user in current_users:
        #replace this with username
        user.send(bytes(f"New user from  {address} connected","utf-8"))
    print(f"Connection from {address} has been established")
    clientsocket.send(bytes("Welcome to the server","utf-8"))
    message = clientsocket.recv(2048) 
    if message:
        for user in current_users:
            user.send(bytes(f"New message: {message} "))

conn.close() 
server.close() 