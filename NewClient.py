# An example script to connect to Google using socket
# programming in Python
import socket  # for socket
import sys
import time
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket successfully created")
except socket.error as err:
    print("socket creation failed with error %s" % (err))

# default port for socket
port = 12345

try:
    host_ip = socket.gethostbyname("localhost")
except socket.gaierror:
    # this means could not resolve the host
    print("there was an error resolving the host")
    sys.exit()

# connecting to the server
s.connect((host_ip, port))
print("the socket has successfully connected to %s on port == %s \n \n" % (socket.gethostname(),port))
server_response = ""
request = ""
msg = ""
server_response = s.recv(1024).decode("UTF-8")

if server_response.lower().startswith("thank"):
    while True:
        print("Server answer: %s" % server_response)
        request = ""
        request = input("What to send?\n")
        request = request.encode("UTF-8")
        s.send(request)
        server_response = s.recv(1024).decode("UTF-8")

        if request.decode("UTF-8") == "exit":
            s.close()