import socket 
import select 
import sys 
  
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
username = str(sys.argv[1])
hostName = str(sys.argv[2]) 
Port = int(sys.argv[3]) 
server.connect((hostName, Port)) 
  
while True: 
    #buffer, how large chuncks of data do we want to receive at once. 
    msg = server.recv(1024)
    print(msg.decode("utf-8"))
    usermessage=str(input("Enter your message:"))
    server.send(usermessage.encode())
server.close() 