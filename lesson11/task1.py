a={'a':1,'b':2, 'c':3}
b={'a':1,'b':2, 'c':3, 'd':4}


def compare_dict(a,b):
    alist=set(list(a.items()))
    blist=set(list(b.items()))

    dict_diff=list(alist-blist)

    print(dict_diff)

    if len(dict_diff) == 0:
        print("works")
        return True
    else:
        return False

compare_dict(a,b)

g="hello worl"

print(g.index("o"))