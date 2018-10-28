import time
from socket import socket
from threading import Thread
import sys
import msvcrt

"""
gets a connected socket and send keep alive message
"""

keep_alive_msg = "keep-alive"
server_ip = '127.0.0.1'
server_port = 2212
name_msg = "name: barhen"
false_cracked_md5 = '7e56f7'
right_cracked_md5 = 'abcdef'
cracked_md5 = false_cracked_md5


def keep_alive(soc):
    while True:
        soc.send(keep_alive_msg)
        time.sleep(1)


def communicate(soc):
    msg = soc.recv(1024)
    print msg
    if msg.startswith("start"):
        time.sleep(30)
        if cracked_md5 == false_cracked_md5:
            print 'sending not found'
            soc.send('not found')
        else:
            soc.send("found: "+cracked_md5)
            print 'sending found'
    if msg == 'bye':
        soc.close()
        sys.exit()


def input_thread():
    msg = raw_input()
    if msg == 'true':
        global cracked_md5
        cracked_md5 = right_cracked_md5



def main():
    client = socket()
    client.connect((server_ip, server_port))
    client.send(name_msg)
    Thread(target=keep_alive, args=(client,)).start()
    Thread(target=input_thread).start()
    while True:
        communicate(client)


if __name__ == "__main__":
    main()
