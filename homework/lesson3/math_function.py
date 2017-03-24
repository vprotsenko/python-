my_input = "2 plus 3 multiply 5 multiply 2 divide 2 minus 200 multiply 5 plus 100000"

transformed_input = ""

my_input=my_input.split(" ")
print(my_input)
while 'multiply' in my_input:
    index=my_input.index('multiply')
    n1=int(index)-1
    n2=int(index)+1
    rezult=int(my_input[n1]) * int(my_input[n2])

    my_input[n1]=rezult
    my_input.pop(n2)
    my_input.pop(index)
    print("=======")
    print(my_input)
while 'divide' in my_input:
    index=my_input.index('divide')
    n1=int(index)-1
    n2=int(index)+1
    rezult=int(my_input[n1]) / int(my_input[n2])

    my_input[n1]=rezult
    my_input.pop(n2)
    my_input.pop(index)
    print("=======")
    print(my_input)

while 'plus' in my_input:
    index=my_input.index('plus')
    n1=int(index)-1
    n2=int(index)+1
    rezult=int(my_input[n1]) + int(my_input[n2])

    my_input[n1]=rezult
    my_input.pop(n2)
    my_input.pop(index)
    print("=======")
    print(my_input)
while 'minus' in my_input:
    index=my_input.index('minus')
    n1=int(index)-1
    n2=int(index)+1
    rezult=int(my_input[n1]) - int(my_input[n2])

    my_input[n1]=rezult
    my_input.pop(n2)
    my_input.pop(index)
    print("=======")
    print(my_input)



'''
for i in my_input.split(" "):
    if i == "plus":
        i = "+"
    elif i == "minus":
        i = "-"
    elif i=="multiply":
        i = "*"
    elif i == "divide":
        i = "/"
    else:
        None
    transformed_input += i
print(eval(transformed_input))
'''




'''
Написать функцию:
Функция принимает в виде строки следующее:
'2 plus 3 multiply 5 minus 2 divide 2' И тому подобное.
plus : +
minus : -
multiply : *
divide : /
Это простейшие математические записи, в которых, вместо математических операторов, стоят слова.
Задача функции, обработать строку и решить записанное в ней уравнение. Функция должна вернуть результат уравнения в виде числа.
Помним о том, что операции умножения и деления выполняются до операций сложения и вычитания.
Если задание черезчур сложное для комплексного выполнения, напишите, для начала, функцию, которая будет выполнять только одно действие,
скажем уметь принимать строку только с 'plus' и выполнять только сложение.
Можно написать не функцией, а просто структурным кодом

'''