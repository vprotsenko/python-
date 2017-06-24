import socket

from threading import Thread, Lock
import time


class Client:
    def __init__(self, client):
        self.client = client

    def receive(self, message_list):
        while True:
            message=self.client[0].recv(65000)
            message_list(message)
            print(message)

    def send(self,  message):
        self.client[0].send(message)

class MyServer(Thread):

    def __init__(self):
        self.lock_mess=Lock()
        self.user = []
        self.message_list = []
        super().__init__()
        self.server = self.get_socket()

    def get_socket(self):
        server = socket.socket()
        server.bind(('localhost', 8000))
        server.listen(5)
        return server

    def run(self):
        while True:
            client = Client(self.server.accept())
            self.user.append(client)
            Thread(target=client.receive, args=[self.add_message]).start()
            print(client)

    def send_message(self, num):
        print(self.user)
        self.user[num][0].send('Hello world'.encode('cp1251'))

    def add_message(self, message):
        self.lock_mess.acquire()
        self.message_list.append(message)
        print(self.message_list)
        self.send_message()
        self.lock_mess.release()

    def send_message(self):
        for i in self.user:
            i.send(self.message_list[-1])



chat = MyServer()
chat.start()

time.sleep(1)
# chat.send_message(0)
# chat.send_message(1)
