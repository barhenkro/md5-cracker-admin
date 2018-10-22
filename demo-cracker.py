import time
from socket import socket
from threading import Thread
import msvcrt

"""
gets a connected socket and send keep alive message
"""

keep_alive_msg = "keep alive"
server_ip = '127.0.0.1'
server_port = 4320
name_msg = "name: barhen"
false_cracked_md5 = '7e56f7'
right_cracked_md5 = '7e56f8'
cracked_md5 = false_cracked_md5


def keep_alive(soc):
    while True:
        soc.send(keep_alive_msg)
        time.sleep(1)


def communicate(soc):
    msg = soc.recv(1024)
    if msg.startswith("start"):
        soc.send(cracked_md5)
    if msg == 'bye':
        soc.close()


def main():
    client = socket()
    client.connect((server_ip, server_port))
    client.send(name_msg)
    Thread(target=keep_alive, args=(client,)).start()
    while True:
        if msvcrt.kbhit() and msvcrt.getwch() == 't':
            print 't'
            cracked_md5 = right_cracked_md5

        communicate(client)


if __name__ == "__main__":
    main()
