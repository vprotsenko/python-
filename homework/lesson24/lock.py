from threading import Thread
import time


class One(Thread):
    def __init__(self):
        super().__init__()

    def run(self):
        while True:
            print('1')
            time.sleep(1)


class Two(Thread):
    def __init__(self):
        super().__init__()

    def run(self):
        while True:
            print('2')
            time.sleep(1)


o=One()
t=Two()

o.start()
t.start()