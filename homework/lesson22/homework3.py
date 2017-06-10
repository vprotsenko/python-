import os
from threading import Thread
class Parser(Thread):
    storage=[]

    def __init__(self, fname):
        super().__init__()
        self.fname=fname

    def run(self):
        data=open(self.fname, 'r', encoding='koi8-r').readlines()
        l=0
        while l < len(data):
            i=data[l]
            if i.startswith('#'):
                index=data.index(i)
                key=data[index+1].split('~')[0]
                value=data[index+8].split('~')[0].split('\n')[0]
                self.storage.append({key:value})
            l+=1

class Runner(Parser):


    def __init__(self):
        self.createListOfParsers()

    def createListOfParsers(self):
        for f in os.listdir('./mob/mob/'):
            Parser('./mob/mob/'+f).start()

    def prinOutput(self):
        line_counter=0
        for line in self.storage:
            line_counter+=1
            print(line)
        print(line_counter)

#r=Runner()
#r.prinOutput()


import os.path, time
print(time.ctime(os.path.getctime('./mob/mob/0.mob')))
