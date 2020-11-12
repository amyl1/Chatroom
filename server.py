from socket import AF_INET, socket, SOCK_STREAM  
import sys
import time
from threading import Thread

def accept_incoming_connections():
    #Sets up handling for incoming clients.
    while True:
        client, client_address = server.accept()
        print("%s:%s has connected." % client_address)
        addresses[client] = client_address
        Thread(target=handle_client, args=(client,)).start()

def handle_client(client):
   #Handles a single client connection.
   name = client.recv(buffer_size).decode()
   clients[client] = name
   broadcast("{} has joined".format(name))
   while True:
        msg = client.recv(buffer_size)
        if msg != "quit".encode():
            broadcast(msg)
        else:
            client.send("quit".encode())
            client.close()
            print("{} has left.".format(clients[client]))
            del clients[client]
            #add user name
            broadcast("A user has left the chat.")
            break

def broadcast(msg):
     for sock in clients:
        sock.send("{}".format(msg).encode())


#sets up dictionaries to store clients and their addresses
clients = {}
addresses = {}

buffer_size=1024
server=socket(AF_INET, SOCK_STREAM)
port = int(sys.argv[1])
server.bind(('',port))

if __name__ == "__main__":
   server.listen(20)  # Listens for 5 connections at max.
   print("Waiting for connection...")
   ACCEPT_THREAD = Thread(target=accept_incoming_connections)
   ACCEPT_THREAD.start()
   ACCEPT_THREAD.join()
   server.close()