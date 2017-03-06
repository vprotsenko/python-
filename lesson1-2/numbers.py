values = "10 15 3 4 20"
#values = input("enter value")

values = values.split(" ")

if len(values) < 3:
    print("error")

first_num = int(values[0])
last_num = int(values[-1])
middle = int(len(values)/2)

if last_num/first_num != 2:
    print("error")


if len(values)%2 == 0:
    middle1_index = int(len(values)/2-1)
    middle2_index = int(len(values)/2)
    print(values[middle1_index], values[middle2_index])
else:
    print(values[middle])

'''
Программа должна принимать через пользовательский ввод несколько чисел через пробел. Соблюдаем следующие условия:
Чисел должно быть не менее трех;
Последнее число должно быть ровно в два раза больше чем первое;
Если условия не соблюдены, вывести на экран "Error".
Если условия соблюдены:
Если чисел парное количество, вывести на экран 2 средних числа, Т.Е. Если числа "10 15 3 20" - вывести на экран "15 3);
Если непарное, вывести на экран одно среднее число - "12 22 8 32 24" - вывести на экран "8";'''