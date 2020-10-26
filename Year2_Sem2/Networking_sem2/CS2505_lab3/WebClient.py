from socket import *
import sys

Socket = socket(AF_INET, SOCK_STREAM)

IP = input("Please enter an IP >>")
#connect the client to server
server_address = (IP, 6789)
Socket.connect(server_address)

#Terminal commands
'''IP = sys.argv[1]
port = sys.argv[2]
server_address = (IP,int(port))
Socket.connect(server_address)'''

path = input("Please enter the path of requested site: ")
#path = sys.argv[3]

#client should be connected to server
#put get requst into variable then change hardcoded to user input
#send get req to server (socket.sendall.encode)
#print out response to terminal

get_request = "GET /"+path+ " HTTP/1.1"

#send get request to the server
Socket.sendall(get_request.encode())

#gets response as a large string
server_response = Socket.recv(1024).decode()
check_status = server_response.split()[1]
if check_status == '200':                       #check if the status is ok
    page = ""                                   #a string to append the file to
    while True:
        data = Socket.recv(4).decode()
        if data == "":
            break                               #break when the file is finished
        page += data

    print(page)

Socket.close()