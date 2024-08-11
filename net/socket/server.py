# server.py
# Importing neccessary inbuilt modules
import socket
import random
import string

# Creating a socket instance
server_object = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

# Connecting to the localhost
ip_address = '127.0.0.1'
port = 5555
server_object.bind((ip_address, port))
server_object.listen()


print('Start SERVER.') 
#Once the client connects to the particular port, the server starts to accept the request.
connection_object, _ = server_object.accept()


if connection_object:
	# Connected to client successfully
    print("SERVER CONNECTED TO CLIENT")
    
    # sending initial message to the client
    connection_object.send(b"type the message")
    
    # receiving message from the client
    data_receive = connection_object.recv(1024)
    
    while data_receive != b'stop':
        client_input = data_receive.decode('utf-8')
        print("{}: {}".format("CLIENT MESSAGE: ", client_input))
        # server_input = random.choice(string.ascii_letters)
        server_input = 'otvet: ' + client_input
        connection_object.send(server_input.encode('utf-8'))
        data_receive = connection_object.recv(1024)

print('Done.')