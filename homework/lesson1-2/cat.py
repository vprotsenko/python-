
cat=[1,2,3,4]

color=""
size=""
character=""
hair=""

if 0 >= cat[0] or cat[0] <=2:
    color="white"
elif 3 == cat[0] or cat[0] == 4:
    color="orange"
elif 5 >= cat[0] or cat[0] <=7:
    color="grey"
elif 8 == cat[0] or cat[0] == 9:
    color="black"

if 0 >= cat[1] or cat[1] <= 2:
    size = "small"
elif 3 >= cat[1] or cat[1] <= 5:
    size = "not big"
elif 6 == cat[1] or cat[1] == 7:
    size = "big"
elif 8 == cat[1] or cat[1] == 9:
    size = "very big"

if 0 == cat[2] or cat[2] == 1:
    character = "lazy"
elif 2 >= cat[2] or cat[2] <= 4:
    character = "calm"
elif 5 >= cat[2] or cat[2] <= 7:
    character = "active"
elif 8 == cat[2] or cat[2] == 9:
    character = "hyper active"

if 0 >= cat[3] or cat[3] <= 2:
    hair = "short wool"
elif 3 >= cat[3] or cat[3] <= 5:
    hair = "smooth wool"
elif 6 == cat[3] or cat[3] == 7:
    hair = "fluffy"
elif 8 == cat[3] or cat[3] == 9:
    hair = "hyper fluffy"

print("This is",hair, color, "cat, he is", character, "and", size)


'''
Создадим кота, но дадим возможность пользователю определить некоторые его параметры следующим образом:
Предлогаем пользователю ввести четырехзначное число;
Затем разбираем пользовательский ввод следующим образом:
Первая цифра отвечает за цвет кота. От 0 до 2 - белый. От 3 до 4 - рыжий. От 5 до 7 - серый. От 8 до 9 - черный.
Вторая цифра отвечает за размер кота. От 0 до 2 - маленький. От 3 до 5 - небольшой. от 6 до 7 - большой. От 8 до 9 - очень большой.
Третья цифра отвечает за характер кота. От 0 до 1 - ленивый. От 2 до 4 - спокойный. от 5 до 7 - подвижный. от 8 до 9 - гиперактивный.
Четвертая цифра отвечает за "пушистость". От 0 до 2 - короткошерстный. От 3 до 5 - гладкошерстный. От 6 до 7 - пушистый. От 8 до 9 - очень пушистый.

После того, как пользователь ввел число, кнему должна вернуться информация примерно следующего вида:
'''