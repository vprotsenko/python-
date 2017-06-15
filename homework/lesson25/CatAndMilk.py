import random, time
from threading import Lock, Thread

class MyLock(list):
    lock = Lock()

class PlateWithMilk:
    plates=[]

    def __init__(self, plate_color):
        self.plate_color=plate_color
        self.milk=10
        self.count_plates(self)

    @classmethod
    def count_plates(cls, p):
        cls.plates.append(p)

    def add_milk(self):
        if self.milk < 10:
            self.milk+=1
            return True
        else:
            return False

    def drink_milk(self):
        if self.milk > 0:
            self.milk-=1
            return True
        else:
            return False

    def get_milk_count(self):
        return self.milk


class Cat(Thread):
    cats=[]

    def __init__(self, name, lck):
        super().__init__()
        self.lck=lck
        self.name=name
        self.cat_position=0
        self.create_cat(self)

    @classmethod
    def create_cat(cls, name):
        cls.cats.append(name)


    def run(self):

        while True:
            self.come_to_plate()
            time.sleep(random.randint(7, 20))


    def come_to_plate(self):
        plate=PlateWithMilk.plates[0]
        self.lck.lock.acquire()
        print('{0} заметил что стоит {1} тарелка и прибежал хлебать молоко'.format(self.name, plate.plate_color))
        for i in range(1, 3):
            if plate.drink_milk():
                print('{0} хлебнул {1} раза'.format(self.name, i))
                #self.lck.append(random.randint(1, 100))
                time.sleep(1)
            else:
                print('{0} от жадности дохлебал все молоко и свалил'.format(self.name))
                return

        print('{0} больше пить не может, уходит'.format(self.name))
        self.lck.lock.release()



class GirlWithMilk(Thread):

    def __init__(self, lck):
        super().__init__()
        self.lck=lck

    def run(self):
        while True:
            self.add_milk()
            time.sleep(10)


    def add_milk(self):
        while True:
            plate= PlateWithMilk.plates[0]
            self.lck.lock.acquire()
            print('Девочка пришла подливать молоко')
            while plate.milk < 10:
                plate.add_milk()
                time.sleep(1)
                print("Кап")
            print('Девочка ушла')
            self.lck.lock.release()
            time.sleep(10)

p1=PlateWithMilk('Красная')
#p2=PlateWithMilk('Синяя')
#p3=PlateWithMilk('Зеленая')

l=MyLock()
g=GirlWithMilk(l)
c1=Cat('Жора', l)
с2=Cat('Рыжик Падло', l)
с3=Cat('Барсик', l)


c1.start()
с2.start()
с3.start()
g.add_milk()


'''
Описать класс блюдца с молоком. Реализовать необходимые атрибуты доступа,
типа количество глотков, выпить глоток, налить в блюдце.
Реализовать максимальное количество глотков, не более 10;
Реализовать класс кота. Коты переодически прибегают в комнату и пристраиваются пить молоко,
но все строго в своей очереди. Иногда коты отваливаются от блюдца,
но через какое-то время опять пристраиваются в очередь.
Реализовать необходимое поведение;
Организовать класс девочки Маши, задача которой подливать молоко, так, чтобы оно не скоро закончилось.

Реализовать все действия с таймингом, чтобы они не выполнялись мнгновенно.
Лучше медленнее. Коты могут пить по несколько глотков.

'''