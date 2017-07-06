import socket

from threading import Thread, Lock
import time

class Client:
    def __init__(self, connect):
        self.connect = connect
        self.name=None

    def receive(self, message_list, calback):
        while True:
            message=self.connect[0].recv(65000)
            calback(message)
            message_list(message)
            print(message)

    def send(self,  message):
        self.connect[0].send(message)

    def ask_name(self):
        name = self.connect[0].recv(65000)
        return name

    def add_user(self, name):
        self.name=name.decode('utf-8')

    def push_message(self, m):
        self.send(m.encode('utf-8'))

    def close(self):
        self.connect[0].close()


class MyServer(Thread):

    def __init__(self):
        self.lock_mess=Lock()
        self.lock_userlist = Lock()
        self.users = []
        self.message_list = []
        super().__init__()
        self.server = self.get_socket()

    def get_socket(self):
        server = socket.socket()
        server.bind(('localhost', 8000))
        server.listen(5)
        return server

    def register_new_user(self, c):
        c.push_message('What is your name')
        name = c.ask_name()

        user_uniq = True

        for i in self.users:
            if i.name == name:
                c.push_message('User already exists')
                user_uniq = False
                c.close()

        if user_uniq:
            print('===========')
            #self.lock_userlist.acquire()
            self.users.append(c)
            #self.lock_userlist.release()
            c.add_user(name)
            self.send_message('User {0} registered'.format(name).encode('utf-8'))


    def start_chat(self, c):
        self.register_new_user(c)

    def run(self):
        while True:
            client = Client(self.server.accept())
            Thread(target=self.start_chat, args=[client]).start()
            Thread(target=client.receive, args=[self.add_message, self.check_message]).start()
            print(client)

    def add_message(self, message):
        self.lock_mess.acquire()
        self.message_list.append(message)
        self.lock_mess.release()

    def send_message(self, s, name=None):
        self.lock_userlist.acquire()
        if not name:
            for i in self.users:
                i.send(s)
        else:
            for i in self.users:
                if i.name.replace('\n', '') == name:
                    i.send(s)
                    break

        self.lock_userlist.release()

    def check_message(self, m):
        u_list = []

        list_users = '/users\n'.encode('utf-8')
        privat_mess = '/send'
        print('====', m.decode('utf-8').split(' ')[0])

        if list_users == m:
            print('looking for users', m)
            for i in self.users:
                u_list.append(i.name)
            self.send_message(str(u_list).encode('utf-8'))
        elif privat_mess == m.decode('utf-8').split(' ')[0]:
            user = m.decode('utf-8').split(' ')[1]
            print('sending to ', user)
            self.send_message((''.join(m.decode('utf-8').split(' ')[1:])).encode('utf-8'), user)
        else:
            self.send_message(m)

chat = MyServer()
chat.start()


