import socket
from cracker import Cracker
import threading


class Admin(object):
    def __init__(self):
        crackers = []
        md5_string = ""
        chunks = []

        self._divide()
        server = socket.socket()
        server.bind(('127.0.0.1', 2212))
        server.listen(5)

    def __divide(self):
        pass

    def __update_name(self, c, name):
        c.name = name
        self._find()

    def __format_string(self, cracker):
        start, stop = cracker.chunck
        st = "start:" + start + ",stop:" + stop + ",md5:" + self.md5_string
        return st

    def __give_chunk(self, cracker):
        if len(self.cracker) > 0:
            cracker.chunk = self.chunks[0]
            del self.chunk[0]

    def __find(self, cracker):
        self.__give_chunk()
        st = self.__format_string(cracker)
        cracker.send(st)

    def communicate(self, cracker):
        msg = cracker.recv()
        if msg.startswith("name:"):
            index = msg.find(':') + 1
            name = msg[index:]
            self.__update_name(cracker, name)

        elif msg == 'not found':
            self.__find(cracker)

    def run(self):
        while True:
            (cracker_socket, cracker_ip) = self.server.accept()
            c = Cracker(cracker_socket)
            self.crackers.append(c)
            t = threading.Thread(target=self.communicate, args=(c,))
            t.start()
