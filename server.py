from socket import AF_INET, socket, SOCK_STREAM  
import sys
import time
from threading import Thread

def accept_incoming_connections():
    #Sets up handling for incoming clients.
    while True:
        client, client_address = server.accept()
        #replace with user name
        print("%s:%s has connected." % client_address)
        client.send(bytes("New user connected", "utf8")) #add username
        addresses[client] = client_address
        Thread(target=handle_client, args=(client,)).start()

def handle_client(client):
   #Handles a single client connection.
   #name = client.recv(buffer_size).decode("utf8")
   welcome = 'Welcome! If you ever want to quit, type quit to exit.'
   client.send(bytes(welcome, "utf8"))
   #add username
   msg = "A new user has joined the chat!"
   broadcast(bytes(msg, "utf8"))
   #clients[client] = name
   while True:
        msg = client.recv(buffer_size)
        if msg != bytes("{quit}", "utf8"):
           #add user name
            broadcast(msg)
        else:
            client.send(bytes("{quit}", "utf8"))
            client.close()
            del clients[client]
            #add user name
            broadcast(bytes("A username has left the chat." ,"utf8"))
            break

def broadcast(msg):  # add username.
     for sock in clients:
        sock.send(bytes("username", "utf8")+msg)


#sets up dictionaries to store clients and their addresses
clients = {}
addresses = {}

buffer_size=1024
server=socket(AF_INET, SOCK_STREAM)
port = int(sys.argv[1])
server.bind(('',port))

if __name__ == "__main__":
   server.listen(5)  # Listens for 5 connections at max.
   print("Waiting for connection...")
   ACCEPT_THREAD = Thread(target=accept_incoming_connections)
   ACCEPT_THREAD.start()  # Starts the infinite loop.
   ACCEPT_THREAD.join()
   server.close()