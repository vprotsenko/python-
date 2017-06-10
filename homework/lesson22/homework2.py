import os

class Data:

    def __init__(self, num, name, descr):
        self.num=num
        self.name=name
        self.descr=descr


class DB:

    raw_database={}
    storage=[]

    def __init__(self, path):
        self.path=path
        self.fill_database()


    def fill_database(self):
        count=0
        for f in os.listdir(self.path):
            new_file=open(self.path+f, "r", encoding='koi8-r').readlines()
            zeroLine=[]
            for i in new_file:

                if i.startswith("#"):
                    zeroLine.append(i)

            for z in zeroLine:
                index=new_file.index(z)
                key=new_file[index:index+2][1].split('\n')[0]
                value=new_file[index:index+9][-1]
                self.raw_database.update({key:value})
            count+=1
        start=1
        for i in self.raw_database.keys():
            self.storage.append(Data(start, i.split('~')[0], self.raw_database[i].split('~')[0]))
            start+=1
        print("------"+str(count))

    def GetObjectByNum(self, n):
        for i in self.storage:
            if n == i.num:
                print('{0} | {1} |{2}'.format(i.num, i.name, i.descr))

    def GetObjectByName(self, n):
        for i in self.storage:
            if n in i.name:
                print('{0} | {1} |{2}'.format(i.num, i.name, i.descr))

    def GetObjectByDescr(self, d):
        for i in self.storage:
            if d in i.descr:
                print('{0} | {1} |{2}'.format(i.num, i.name, i.descr))

d=DB("./mob/mob/")

print(len(d.storage))

d.GetObjectByNum(5)
d.GetObjectByName('костяк скелет')
d.GetObjectByDescr('Костоправ понуро плетется за дозорным разъездом.')


'''
В архиве находится куча файлов, консистентных данных.
В каждом файле куча данных, где каждый фрагмент начинается с #и номер фрагмента
Необходимо спарсить данные и создать объект - хранилище для всех этих данных таким образом,
чтобы мы могли по первой строке после номера, находить восьмую строку после номера.
Т.Е. фактически тебе нужно только первая строка после номера фрагмента и восьмая.
все лишние символы типа ~ и  перевода строк убираем
типа гиганского словаря.
Более идеальным вариантом будет следующий:
Создаем объекты каждой записи, которые имеют следующие свойства:
num - номер фрагмента, кпримеру 5500
name - хранит первую строку после номера фрагмента.
descr - хранит восьмую строку после номера.
создаем объект-хранилище с соответствующими методами типа GetObjectByName, GetObjectByNum, GetObjectByDescr, куда передаем нужные данные,
если такой объект в хранилище находится, он возвращается.
Т.Е. таким образом мы можем искать объект по любому из трех свойств.
'''