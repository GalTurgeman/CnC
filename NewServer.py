# first of all import the socket library
import socket
import sys
# next create a socket object
try:
    s = socket.socket()
    print
    "Socket successfully created"

    # reserve a port on your computer in our
    # case it is 12345 but it can be anything
    port = 12345

    # Next bind to the port
    # we have not typed any ip in the ip field
    # instead we have inputted an empty string
    # this makes the server listen to requests
    # coming from other computers on the network
    s.bind(('', port))
    print("socket binded to %s" % (port))

    # put the socket into listening mode
    s.listen(5)
    print("socket is listening")
except (OSError,socket.error) as e:
    print("Fail to create socket!\n")
    print(e)
    sys.exit()
# a forever loop until we interrupt it or
# an error occurs
while True:
    # Establish connection with client.
    c, addr = s.accept()
    print('Got connection from', addr)
    client_request = ""
    # send a thank you message to the client.
    hello = "Thank you for connecting\n"
    hello = hello.encode("UTF-8")
    c.send(hello)

    client_request = c.recv(1024).decode("UTF-8")
    print(client_request)
    server_response = server_response.encode("UTF-8")

    c.send(server_response)
    # Close the connection with the client
    if client_request == "exit":
        break