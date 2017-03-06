a=[4,24,54,46,1,879,98,5]

sorted_a=[]
small=a[0]

#while a:

def remove_num():
    for i in a:
        if small > i:
            small=i
    a.pop(i)
    sorted_a.append(small)



while a:
    remove_num()

print(small, sorted_a, a)