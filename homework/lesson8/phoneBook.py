def search_peaple():
    book=open('bookDB', 'r')

    f_name=input('f_name')
    s_name=input('s_name')
    phone=input('phone')
    email=input('email')


    l=[]
    for i in book:
        i_splited=i.split(',')
        if len(f_name)>1 and f_name in i_splited[0] and i not in l:
            l.append(i)
        if  len(s_name)>1 and s_name in i_splited[1] and i not in l:
            l.append(i)
        if  len(phone)>1 and phone in i_splited[2] and i not in l:
            l.append(i)
        if  len(email)>1 and email in i_splited[3] and i not in l:
            l.append(i)

    book.close()
    return l


def remove(people):
    cleaned_book=""
    book=open('bookDB', 'r+')
    for i in book:
        if i not in people:
            cleaned_book=cleaned_book+i
    book.close()

    book=open('bookDB', 'w')
    book.write(cleaned_book)
    print("Removed")


def save(people):
    output_file=input('Put filename: ')
    cleaned_book=""
    file=open(output_file, 'w')
    for i in people:
        file.write(i)

    file.close()
    print('File created')


def add_person():
    f=open('bookDB', 'a')
    f_name=input('f_name')
    s_name=input('s_name')
    phone=input('phone')
    email=input('email')
    f.write('\n{},{},{},{}'.format(f_name, s_name, phone, email))
    f.flush()

def find_person():
    selected_people=search_peaple()
    print(selected_people)
    to_do=input('what to do: R - Remove, S - Save to file, E - exit ')
    for i in selected_people:
        print(i)
    if to_do == 'R':
        remove(selected_people)
    elif to_do == 'S':
        save(selected_people)
    elif to_do == 'E':
        print("See you next time")
    else:
        print('We have no other options')


step1=input('Put F - to find preson, Put A - to add')
if step1 == 'F':
    find_person()
elif step1 == 'A':
    add_person()







'''
Разработать программу - справочник;
Программа должна уметь сохранять в себе: Имя, Фамилию, Номер телефона, email, ввиде одной записи про человека. Подобных записей может быть много;
Приложение должно предоставлять возможность вносить подобные записи, искать записи по одному/нескольким критериям, удалять записи по одному/нескольким критериям, показывать список всех записей;
Приложение должно иметь независимую бд в виде файла любого удобного формата;
Приложение должно предоставлять возможность сохранить найденные результаты в файл любого удобного формата;
Интерфейс приложения содержит в себе на стартовом экране: Предложение искать запись, создать запись, удалить запись, просмотреть все записи.

При добавлении записи, пользователю предоставляется возможность вносить необходимые данные;
При поиске, пользователю предоставляется возможность задать данные по необходимым критериям, после выдачи результата, выдать запрос о желании сохранить результаты в файл;
При удалении, вместо запроса о сохранении в файл, запрос про удаление, после подтверждения, удалить все записи;

Результаты выдаются в виде пронумерованного списка строк;

'''