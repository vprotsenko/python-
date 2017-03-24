def get_pair(l):
    pair=[]
    for i in l:
        if i%2 == 0:
            pair.append(i)
    return pair


def get_range(a, b, l):
    pair=get_pair(l)

    print(pair[a:b])

get_range(3,40,[1,2,4,5,6,4,4,4,4,7,8,87,89,79,7])

