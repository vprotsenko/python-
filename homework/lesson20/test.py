class Person():
    _name="Chack"

    def get_name(self):
        return self._name

    def set_name(self, n):
        if len(n) > 2:
            self._name=n.capitalize()



#p=Person()
#p.set_name('vasia')


class Demo:
    count_objects = 0
    def  __init__(self):
        self.count()

    def count(cls):
        cls.count_objects+=1

    count = classmethod(count)



