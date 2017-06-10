class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, scholarship, *args):
        super().__init__(*args)
        self.scholarship = scholarship

    def get_scholarship(self):
        return self.scholarship*0.8


class Warden(Student):
    def get_scholarship(self):
        return super().get_scholarship()*3

Andy=Warden(100, 'Andy')
Bob=Student(100, 'Super Bob')

print(Andy.get_scholarship())





