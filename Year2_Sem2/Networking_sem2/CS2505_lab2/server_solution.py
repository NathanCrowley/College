'''
Nathan Crowley - 118429092
'''

# from the socket module import all
from socket import *
from datetime import datetime
# Create a TCP server socket
# (AF_INET is used for IPv4 protocols)
# (SOCK_STREAM is used for TCP)
sock = socket(AF_INET, SOCK_STREAM)
# if we did not import everything from socket, then we would have to write the previous line as:
# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# set values for host 'localhost' - meaning this machine and port number 10000
host_name = getfqdn(gethostname())
print("*** Host IP: ",host_name)
host_ip = gethostbyname(host_name)  #gets host name of current device
print("*** IP: %s."%(host_ip))      #print the ip address
server_address = (host_name, 10000)
# output to terminal some info on the address details
print('*** Server is starting up on %s port %s ***' % server_address)
# Bind the socket to the host and port
sock.bind(server_address)

# Listen for one incoming connections to the server
sock.listen(1)

# we want the server to run all the time, so set up a forever true while loop
while True:
    #text_file = open("file_log.txt","a")    #open text file to hold users input
    sentence = ""                           #creat empty string to hold message
    #time = datetime.now()                   #get the time the message is sent
    # Now the server waits for a connection
    print('*** Waiting for a connection ***')
    # accept() returns an open connection between the server and client, along with the address of the client
    connection, client_address = sock.accept()

    try:
        print('connection from', client_address)
        # Receive the data in small chunks and retransmit it
        while True:
            # decode() function returns string object
            data = connection.recv(16).decode()
            if data:
                sentence += str(data)           #store message in a string we append to the string as the message is sent in parts not as a whole
                print('Client "%s"' % data)
                #print('sending data back to the client')
                # encode() function returns bytes object
                connection.sendall(data.encode())
            else:
               # print('no more data from', client_address)
                break

            server_message = input("Please enter a message to be sent: ")
            connection.sendall(server_message.encode())

            # Look for the response
            amount_received = 0
            amount_expected = len(server_message)

            while amount_received < amount_expected:
                data = connection.recv(16).decode()
                amount_received += len(data)
            #print(sentence)

    finally:
        #text_file.write(sentence + " " + str(time) + "\n")  # append users input to file log
        # Clean up the connection
        #text_file.close()
        connection.close()

# now close the socket
sock.close();