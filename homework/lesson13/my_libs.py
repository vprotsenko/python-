import csv

f = list(csv.reader(open('Book1.csv', 'r'), delimiter=','))


def len_column():
    my_json = list(f)[0]
    return len(my_json)


def len_lines():
    my_json = list(f)
    return len(my_json) - 1


def get_headers():
    my_json = list(f)[0]
    return my_json


def get_column(arg):
    error_msg = "No such column"
    output = ''
    try:
        arg = int(arg)
        if arg > 2 or arg < 0:
            print(error_msg)
        else:
            position = arg
            for i in f:
                if len(i[position]) > 0:
                    output += i[position] + "\n"
            return output
    except:
        if arg not in f[0]:
            print(error_msg)
        else:
            position = f[0].index(arg)
            for i in f:
                if i[position] != "":
                    output += i[position] + "\n"
            return output


def get_line(n):
    try:
        n = int(n)
        if 0 <= n < len(f):
            return (",".join(f[n]))
        else:
            print("You are out of range, try again")
    except:
        print('Error input, try with to put digit')


def get_cells(l):
    try:
        row = int(l[0])
        col = int(l[1])
        if col < 0 or col > len(f[0]) - 1:
            print('wrong column')
        elif row < 0 or row > len(f) - 1:
            print('wrong row')
        else:
            return f[row][col]
    except:
        print("Your input need to be with digits")


def add_header(arg, p=-1):
    try:
        p = int(p)
    except:
        p = -1
    if p == -1 or p < -1:
        p = len(f)

    for i in range(len(f)):
        if i == 0:
            f[i].insert(p, arg)
        else:
            f[i].insert(p, None)
    return f


def set_cell(l, val):
    try:
        row = int(l[0])
        col = l[1]

        try:
            col = int(col)
            if col < 0 or col > len(f[0]) - 1:
                print('wrong column')
            elif row < 0 or row > len(f) - 1:
                print('wrong row')
            else:
                f[row][col] = val
                print(f[row][col])
                return f
        except:
            if col in f[0]:
                position = f[0].index(col)
                f[row][position] = val
                print(f[row][position])
                return f
            else:
                print('No such column')
    except:
        print('Row has to be int')


def add_line(l, index=-1):
    try:
        index = int(index)
    except:
        index = len(f)

    l = list(l.split(','))
    if index < 1:
        index = len(f)
    f.insert(index, l)
    while len(l) < len(f[0]):
        l.append("")
    return f


def write_to_file(name):
    file = open(name, 'w')

    for i in f:
        line = ",".join(i)
        file.write(line + "\n")
    file.flush()
    file.close()
