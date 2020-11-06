import socket 
import sys 

        
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
username = str(sys.argv[1])
hostName = str(sys.argv[2]) 
Port = int(sys.argv[3]) 
server.connect((hostName, Port)) 
msg = server.recv(1024)
print(msg.decode())
server.send('Server: {} has joined the chat. Say hello!'.format(username).encode())

while True: 
    #buffer, how large chuncks of data do we want to receive at once. 
    msg = server.recv(1024)
    print(msg.decode())
    usermessage=str(input("Enter your message:"))
    if usermessage != "QUIT":
        usermessage=username+": "+usermessage
        server.send(usermessage.encode())
    else:
        #quit
        server.send("QUIT".encode())
        #send message to say leaving
        server.close() 