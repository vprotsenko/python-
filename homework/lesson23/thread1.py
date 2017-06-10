from threading import Thread
import time

def loop_x():
    while True:
        print('x')
        time.sleep(3)

t=Thread(target=loop_x())


loop_x()