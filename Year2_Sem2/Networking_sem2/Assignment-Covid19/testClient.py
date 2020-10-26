#- take in domain name of server
#- do DNS Lookup and use returned IP Address as servers address
#- create Datagram Socket
#- Send message to server (Remember,UDP sends a message but DOESNT create a connection)
''''- recieve the response
- print answer to screen'''

#(remember to close sockets)

import socket
print(socket.gethostname())

domain_name = input("Please enter your Domain name of the Server... ")
UDP_IP = socket.gethostbyname(domain_name)
UDP_PORT = 6789

print("Target IP: ",UDP_IP)
print("Target Port: ",UDP_PORT)

while True:
#get user input for message tob
    message = input("Please enter message to be sent(X/x to exit) >>> ")
    if message == 'X' or message == 'x':
        sock.close()
        break
    print("Message: ", message)

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(message.encode(), (UDP_IP, UDP_PORT))

#recieve from server
    newdata,addr = sock.recvfrom(1024)
    newdata = newdata.decode()
    print("\n\t***New message: {} ***".format(newdata))
