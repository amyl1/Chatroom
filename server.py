
import socket 
import select 
import sys 

def broadcast(users,new_message):
    for user in users:
        user.send(f": {new_message}".encode())

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
  

# local host
hostName = ''
  
# takes second argument from command prompt as port number 
Port = int(sys.argv[1]) 
server.bind((hostName, Port)) 
  


server.listen(100) 

current_users=[]
while True:
    clientsocket, address = server.accept()
    current_users.append(clientsocket)
    print(f"Connection from {address} has been established")
    clientsocket.send("Welcome to the server! \n To quit the server, type QUIT \n".encode())
    
    while True:
        message = clientsocket.recv(1024) 
        if message:
            if message!="QUIT":
                broadcast(current_users,message)
            else: #replace with username
                broadcast(current_users,"User has left")
                break

conn.close() 
server.close() 