#- create Datagram Socket
#- bind this socket to hostIP and port (port 6789)
#- stay in infinite loop and listen for messages (from client)
#- print recieved message and save to a log file with timestamp
#- take message and change to UPPERCASE
#- extract address and port from client
#- sends timestamp and UPPERCASE sentence to client

#(remember to close sockets)

import socket
from datetime import datetime

host = socket.gethostname()
UDP_IP = socket.gethostbyname(host)
UDP_PORT = 6789

#create socket
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind((UDP_IP,UDP_PORT))

while True:
#get current time for timestamp
    time = datetime.now()
    print(host,UDP_IP)
    print("**Server waiting for client**")
#recieve clients message
    data,addr = sock.recvfrom(1024)

#decode messae from bytes to string
    data = data.decode()
    print("Recieved message: ",data)

#log message + timestamp
    print("\tMessage being logged...")
    with open('file2log.txt','a') as textfile:
        textfile.write(data+" -- "+str(time)+"\n")
    print("Message: {} logged.".format(data))

#extract address from client
    client_address = addr

#send uppercase message and timestamp to client
    # change to upper case
    print("\t**Changing to UpperCase...**")
    data = data.upper()
    #send back to client
    print("Sending back to client.....")
    sock.sendto(data.encode(),client_address)

sock.close()

