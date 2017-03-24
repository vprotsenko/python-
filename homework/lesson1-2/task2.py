d = "abcdef"

d1=d[::-2][::-1]
d2=d[::2]

rez=[]
for i in range(len(d1)):
    rez.append(d1[i])
    rez.append(d2[i])

print rez