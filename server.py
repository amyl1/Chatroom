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
        msg = client.recv(buffer_size).decode()
        if msg != "quit":
            broadcast(msg)
        else:
            client.send("quit".encode())
            client.close()
            print("{} has left.".format(clients[client]))
            user=clients[client]
            del clients[client]
            broadcast(user+" has left the chat.")
            break


def broadcast(msg):
     for sock in clients:
        sock.send("{}".format(msg).encode())


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

buffer_size=1024
server=socket(AF_INET, SOCK_STREAM)
port = int(sys.argv[1])
server.bind(('',port))

if __name__ == "__main__":
   server.listen(100)  # Listens for 100 connections at max.
   print("Waiting for connection...")
   ACCEPT_THREAD = Thread(target=accept_incoming_connections)
   ACCEPT_THREAD.start()
   ACCEPT_THREAD.join()
   server.close()