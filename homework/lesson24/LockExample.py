from threading import Lock, Thread
import time
import random

class MyList(list):
    lock = Lock()

class WriteInfo(Thread):
    counter = 1
    def __init__(self, lst):
        super().__init__()
        self.lst = lst
        self.name = self.counter
        self.counterup()

    @classmethod
    def counterup(cls):
        cls.counter += 1

    def run(self):
        while True:
            time.sleep(random.randint(4, 7))
            self.lst.lock.acquire()
            print('{0} starting'.format(self.name))
            for i in range(0, 5):
                self.lst.append(random.randint(1, 100))
                time.sleep(1)
            self.lst.lock.release()

class ReadInfo:
    def __init__(self, lst):
        self.lst = lst

    def read(self):
        while True:
            self.lst.lock.acquire()
            print(self.lst)
            self.lst.lock.release()
            time.sleep(1)

l = MyList()
w = WriteInfo(l)
w2 = WriteInfo(l)
w3 = WriteInfo(l)
r = ReadInfo(l)
w.start()
w2.start()
w3.start()
r.read()