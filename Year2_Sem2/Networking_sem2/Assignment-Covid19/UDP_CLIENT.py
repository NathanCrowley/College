from socket import *

host = gethostname()
UDP_IP = gethostbyname(host)
UDP_PORT = 6789
message = input("Please enter message to be sent >>> ")

print("UDP target IP: ", UDP_IP)
print("UDP target Port: ", UDP_PORT)
print("Message: ", message)

address = (UDP_IP, 6789)
message = message.encode()

sock = socket(AF_INET, SOCK_DGRAM)
sock.sendto(message, address)
