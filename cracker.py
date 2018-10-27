import socket
import time


class Cracker:
    def __init__(self,socket):
        self.name = ''
        self.socket = socket
        self.chunk = None
        self.alive = time.time()

    def send(self,s):
        print 'sent to',self.name, s
        return self.socket.send(s)

    def recv(self):
        msg =  self.socket.recv(1024)
        print 'recived from', self.name, msg
        return  msg