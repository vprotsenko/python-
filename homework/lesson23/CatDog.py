from threading import Thread
from random import randint
import time

class Cat(Thread):
    cat_list=[]
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.here = False
        self.add_cat(self)
        self.health=True

    @classmethod
    def add_cat(cls, s):
        cls.cat_list.append(s)


    def run(self):
        while self.health:
            if self.here:
                if randint(0,10) <= 3:
                    print('{0} убежал за тучку'.format(self.name))
                    self.here = False
            else:
                if randint(0,10) <= 3:
                    print('{0} прибежал из за тучки'.format(self.name))
                    self.here = True
            time.sleep(randint(2,4))

class Dog(Thread):
    dog_list=[]
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.here = True
        self.add_dog(self)

    @classmethod
    def add_dog(cls, s):
        cls.dog_list.append(s)


    def run(self):
        while len(Cat.cat_list) > 0:
            if self.here:
                if randint(0,10) <= 3:
                    print('{0} выпрыгнул из за забора'.format(self.name))
                    for i in Cat.cat_list:
                        if i.here == True:
                            print('И сожрал {0}a'.format( i.name))
                            Cat.cat_list.remove(i)
                            i.health=False

                    self.here = False
                else:
                    for i in Cat.cat_list:
                        if i.here == True:
                            print('{0} выпрыгнул и потрепал '.format(self.name)+ i.name+'a')
            else:
                if randint(0,10) <= 3:
                    print('{0} прыгнул за забор'.format(self.name))
                    self.here = True
            time.sleep(randint(2,4))

c1=Cat("Барсик")
c2=Cat("Мурзик")
c3=Cat("Рыжик")
d=Dog("Бобик")

c1.start()
c2.start()
c3.start()
d.start()
#print(c.cat_list)