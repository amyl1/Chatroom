from socket import AF_INET, socket, SOCK_STREAM  
import sys
from threading import Thread
import logging

usernames=[]

def sendUser(msg,user,name):
    sent=False
    #send message to requested recipient
    for username in usernames:
        if username[0]==user:
            username[1].send("{}".format(msg).encode())
            sent=True
            logging.info(msg+" whispered to "+ user) 
    #send error message back to user
    if not sent:
        for username in usernames:
            if username[0]==name:     
                username[1].send("User could not be found, retry sending.".encode())

def accept_incoming_connections():
    #Sets up handling for incoming clients.
    while True:
        client, client_address = server.accept()
        print("%s:%s has connected." % client_address)
        logging.info("%s:%s has connected." % client_address)
        addresses[client] = client_address
        Thread(target=handle_client, args=(client,)).start()          

def handle_client(client):
    #Handles a single client connection.
    name = client.recv(buffer_size).decode()
    usernames.append([name,client])
    clients[client] = name
    broadcast("{} has joined".format(name))
    while True:
        try:
            msg = client.recv(buffer_size).decode()
            #user has requested to change username
            if msg[:4] == "USER":
                user=clients[client]
                newName=msg[4:]
                clients[client]=newName
                for u in range(len(usernames)):
                    if usernames[u][0]==user:
                        usernames[u]=[newName,usernames[1]]
                broadcast(user+" has changed their name to "+newName) 
            #user has requested to see a list of all users
            elif msg=="DISPLAY":
                for i in range(len(usernames)):
                    msg=usernames[i][0] 
                    client.send("{}".format(msg).encode())
            #user is leaving
            elif msg == "quit":
                client.send("quit".encode())
                client.close()
                print("{} has left.".format(clients[client]))
                user=clients[client]
                for u in range(len(usernames)):
                    if usernames[u][0]==user:
                        usernames.remove(usernames[u])
                del clients[client]
                #inform all users
                broadcast(user+" has left.")
                break
            #send message
            else:
                msgParts=msg.split('*')
                #send to all
                if msgParts[1]=="ALL":
                    broadcast(msgParts[0])
                #send to one user
                else:
                    sendUser(msgParts[0],msgParts[1],name)
        #disconnect user if they crash
        except:
            print("{} has left.".format(clients[client]))
            user=clients[client]
            del clients[client]
            broadcast(user+" has left the chat.")
            break

#send to all users
def broadcast(msg):
    for sock in clients:
        sock.send("{}".format(msg).encode())
    logging.info("{} ".format(msg))

#if server crasheds, disconnect all users
def closeAll():
    for sock in clients:
        sock.send("Server has crashed! Disconnecting...".encode())
        sock.close()
    logging.info("server crashed. All users disconneted")

#check sys arguments
if len(sys.argv) != 2 :
    print ('Incorrect command line arguments given')
    sys.exit(1) 
try:
    port = int(sys.argv[1])
except ValueError:
    print ('Incorrect command line arguments given')
    sys.exit(1) 
#sets up dictionaries to store clients and their addresses
clients = {}
addresses = {}
logging.basicConfig(filename="server.log",level=logging.INFO)
with open('server.log', 'w'):
    pass
buffer_size=1024
server=socket(AF_INET, SOCK_STREAM)
port = int(sys.argv[1])
server.bind(('',port))

if __name__ == "__main__":
    try:
        server.listen(100)  # Listens for 100 connections at max.
        print("Waiting for connection...")
        ACCEPT_THREAD = Thread(target=accept_incoming_connections)
        ACCEPT_THREAD.start()
        ACCEPT_THREAD.join()
    except:
        closeAll()
        server.close()