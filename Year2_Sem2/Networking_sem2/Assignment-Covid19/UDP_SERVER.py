from socket import *
from datetime import datetime
host = gethostname()
UDP_IP = gethostbyname(host)
UDP_PORT = 6789
address = (UDP_IP,UDP_PORT)

sock = socket(AF_INET, SOCK_DGRAM)
sock.bind(address)

while True:
    #decode message + log to a file
    text_file = open('file2log.txt', 'a')
    sentence = ''
    time = datetime.now()
    #decode message
    while True:
        data = sock.recvfrom(1024)
        if data:
            sentence += str(data)
        else:
            print("No more data from Client.")
            break
    text_file.write(sentence + " " + str(time) + "\n")
    text_file.close()
    break
