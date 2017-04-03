import csv

data=list(csv.reader(open('cells_en.csv', 'r')))

def get_not_rent():
    not_rent=[]
    for i in data:
        if i[1]=='no':
            i.pop(2)
            not_rent.append(i)
    return not_rent

def get_empty():
    empty=[]
    for i in data:
        if i[3]=='no':
            i.pop(3)
            empty.append(i)
    return empty

def get_rent_empty():
    rent_empty=[]
    for i in data:
        if i[1]=='yes' and i[3]=='no':
            i.pop(3)
            i.pop(1)
            rent_empty.append(i)
    return rent_empty


#get_not_rent()

#get_empty()

#get_rent_empty()
out_file=open('rezult', 'w', newline='')

writer=csv.writer(out_file).writerows(get_not_rent())




