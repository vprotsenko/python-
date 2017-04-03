import mod as m
import json

print(m.x)

m.set_x(44)
m.get_x()

print(m.x)

a=open('test1.py', 'r+')

l=[3,4,65,6,457,43,753,7]
l.reverse()
l.sort()
l.reverse()
l.extend([4,4,4,4,4,4])
print(l)
m=set(l)

def square(r):
    return r>100

print(list(filter(square, m)))

