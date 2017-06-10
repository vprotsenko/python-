f=open('info.txt', 'r', encoding='utf-8')

fulltext=f.readlines()




first_text={}
def first():


    for i in fulltext:
        if ':' in i and '|' in i:
            line=i.split('|')[0]
            key=line.split(':')[0].split('\t')[1]
            value=line.split(':')[1]
            first_text.update({key:value})
    print(first_text)

def second():
    aliases=fulltext[fulltext.index("zone_aliases:\n"):][1:]
    rez={}

    for i in aliases:
        if ":" in i:
            key=i.split(": ")[0]
            value=i.split(": ")[1].split("\n")[0]
            rez.update({key:value})

    print(rez)

def third(num):
    aliases=fulltext[fulltext.index(num+":\n"):][1:]
    rez={}

    for i in aliases:
        if ": " in i and i.startswith('\t'):
            key=i.split(": ")[0].split('\t')[1]
            value=i.split(": ")[1].split('\n')[0]
            rez.update({key:value})

    print(rez)


print("1 ===========================================")
first()
print("2 ===========================================")
second()
print("3 ===========================================")
third('851')




'''
Написать 3 функции, которые возвращают из данных файла следующие структуры:
Для всех данных типа global, вернуть словарь, где ключем будет название до символа ':',
значением будет список из двух значений, интовое перед символом '|', и второе интовое после '|';

вторая функция, для всех данных типа zone_aliases, возвращает словарь, где ключем будет название до ':',
значением - интовое значение числа после ':'.

третья функция, для всех данных, которые описаны после конкретного номера, должна возвращать словарь,
где ключем будет интовое значение типа данных, значением будет словарь, где ключем будет название до ':'
в конкретном типе данных, значением - интовое значение после ':'


'''