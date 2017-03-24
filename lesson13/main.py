import my_libs as m

def welcome_msg():
    print("What do you want to do?\n"
          "1 - Check nmber of columns\n"
          "2 - Check nmber of lines\n"
          "3 - Check Headers\n"
          "4 - Check one column (by name or number)\n"
          "5 - Check one column (by number)\n"
          "6 - Get cells by indexes\n"
          "7 - Add header\n"
          "8 - Change cell\n"
          "9 - Add line\n"
          "10 - Write all changest to file\n"
          "11 - EXIT\n"
          )

def my_app():

    g=int(input("Your Choice = "))

    if g == 1:
        print("Nmber of columns " + str(m.len_column()))
        return True
    elif g == 2:
        print("Nmber of lines " + str(m.len_lines()))
        return True
    elif g == 3:
        print("Headers ( " + str(m.get_headers()) + ")")
        return True
    elif g == 4:
        i=input('Put column name or index')
        print('List of column ' + str(m.get_column(i)))
        return True
    elif g == 5:
        i=input('Put line number')
        print('Your line: ' + str(m.get_line(i)))
        return True
    elif g == 6:
        i=input('Put row')
        j=input('Put line ')
        print(m.get_cells([i,j]))
        return True
    elif g == 7:
        i=input('Put header name')
        j=input('Put header position index ')
        print(m.add_header(i,j))
        return True
    elif g == 8:
        i=input('Put row')
        j=input('Put line ')
        k=input('Put value of cel ')
        print(m.set_cell([i,j], k))
        return True
    elif g == 9:
        i=input('Put line index')
        j=input('Put line value ')
        print(m.add_line(j,i))
        return True
    elif g == 10:
        i=input('Put file name')
        print(m.write_to_file(i))
        return True
    elif g == 11:
        return False
    else:
        print('No such choice')
        return False

status=True
while status:
    l='fdsf,sdf'
    l=list(l.split(','))
    print(l)
    welcome_msg()
    print("===================================")
    status=my_app()
    print("===================================")



'''
print(m.len_column())
print(m.len_lines())
print(m.get_headers())

print(m.get_column('dsf'))
print(m.get_line(1))
print(m.get_cells([2,0]))
print(m.add_header('xz',-3))
print(m.set_cell([1,"FathegrName"], 'xzxz'))
print(m.add_line(['hello',]))


Организовать следующие функции взаимодействия (Все функции принимают в себя первым аргументом table - список списков):
len_column - возвращает количество столбиков таблицы.
len_lines - возвращает количество строк таблицы.
get_headers - вернуть список заголовков колонок.
get_column - принимает аргумент в виде номера или заголовка колонки, возвращает список записей в данножй колонке,
начиная с заголовка колонки.
get_line - принимает аргумент, в виде номера строки таблицы, возвращает список записей в указанной строке.
get_cells - принимает номер колонки и строки в виде списка из двух элементов, где первое значение - номер колонки,
второе - номер строки. Может принимать *args подобных запросов и возвращать список значений, по указанным координатам.
add_header - принимает аргумент в виде имени заголовка для новой колонки, вторым, необязательным, аргументом,
принимает номер для новой колонки. По умолчанию, колонка создается в последней Т.Е. правой. Все значения для новой колонки,
забиваются типом пустой строки.
set_cell - принимает аргумент, в виде списка из двух значений для колонки и строчки или в виде списка из двух значений,
где первое значение - имя колонки, второе - номер строки; вторым аргументом принимает значение для ячейки и
устанавливает его. Не разрешает изменять первую строку, где находятся заголовки.

add_line - принимает список значений для строки и номер строки, где нужно вставить новую строку.
Если какую-то ячейку нужно пропустить, в списке будет стоять значение пустой строки. По умолчанию добавляет строку в конец.
'''