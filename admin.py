import socket
from cracker import Cracker
import threading
import time
import md5


class Admin(object):
    def __init__(self):
        self.crackers = []
        self.md5_string = "abcdef"
        self.chunks = self.__divide()

        self.server = socket.socket()
        self.server.bind(('127.0.0.1', 2212))
        self.server.listen(5)

    def __divide(self):
        lst = []
        start = 'aaaaaa'
        while ord(start[0]) <= ord('z'):
            stop = start[0] + 'zzzzz'
            lst.append((start, stop))
            start = chr(ord(start[0]) + 1) + start[1:]
        return lst

    def __update_name(self, cracker, name):
        cracker.name = name
        self.__find(cracker)

    def __format_string(self, cracker):
        start, stop = cracker.chunk
        st = "start:" + start + ",stop:" + stop + ",md5:" + self.md5_string
        return st

    def __give_chunk(self, cracker):
        if len(self.chunks) > 0:
            cracker.chunk = self.chunks[0]
            del self.chunks[0]

    def __find(self, cracker):
        self.__give_chunk(cracker)
        if cracker.chunk != None:
            print cracker.chunk
            st = self.__format_string(cracker)
            print st
            print cracker.send(st)

    def __check(self,cracker,what_found):
        if what_found==self.md5_string:
            cracker.send("ya melech")
            for i in self.crackers:
                i.send("bye")
                self.crackers.remove(i)
                del i



    def keep_thread(self):
        while True:
            for c in self.crackers:
                if (time.time() - c.alive > 3):
                    sht = 1
                    for k in self.crackers:
                        if k.chunk == None:
                            k.chunk = c.chunk
                            k.send(self.__format_string(k))
                            sht = 0
                            break
                    if sht:
                        self.chunks.append(c.chunk)
                    self.crackers.remove(c)
                    del c

    def communicate(self, cracker):
        while True:
            msg = cracker.recv()
            print msg
            if msg.startswith("name:"):

                index = msg.find(':') + 1
                name = msg[index:]
                self.__update_name(cracker, name)

            elif msg == 'not found':
                self.__find(cracker)

            elif msg.startswith("found:"):
                index = msg.find(':') + 2
                what_found = msg[index:]
                self.__check(cracker,what_found)

            elif msg == 'keep-alive':
                cracker.alive = time.time()

            else:
                cracker.send('follow the protocol idiot')

    def run(self):
        while True:
            (cracker_socket, cracker_ip) = self.server.accept()
            c = Cracker(cracker_socket)
            self.crackers.append(c)
            t = threading.Thread(target=self.communicate, args=(c,))
            t.start()

