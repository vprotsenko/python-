from threading import Thread, Event
import time, random

class Printer(Thread):
    printers=[]

    def __init__(self, name, event1, event2):
        super().__init__()
        self.name=name
        self.event1=event1
        self.event2=event2

    @classmethod
    def my_event(cls, name):
        cls.printers.append(cls, name)

    def run(self):
        while True:

            self.event1.wait()
            time.sleep(random.randint(0, 2))
            print(self.name)
            self.event1.clear()
            self.event2.set()


a=Event()
b=Event()

p1=Printer('a', a, b)
p2=Printer('b', b, a)

b.set()
p1.start()
p2.start()

'''
wait - блокирует поток если флаг не установлен
clear - сбрасывает флажок set
set - ставит флаг не блокировать или освобождает от wait
'''

'''
Написать два потока, задача одного писать в файл a, второго - b.
Буквы должны писаться последовательно
a
b
a
b
a
b
Никогда не должны перемешиваться или дублироваться.
Для этого понадобиться использования двух ивентов!
'''



'''
if __name__ == '__main__':
@property
@staticmethod
'''