import backend_part as back


def registration():
    username = input("Put Username")
    password = input("Put password")
    email = input("Put email")
    if back.add_user(username, password, email) is True:
        print("User added")
    else:
        print("User already exist")


def print_notes(user):
    id = 0
    for i in back.get_notes(user):
        print("id={0} date={3}||{1}||{2}".format(id, i[0], i[1], i[2]))
        id += 1


def print_note_id(user, id):
    try:
        id = int(id)
        print(back.get_note_id(user, id))
    except (IndexError, ValueError):
        print('No such id')


def print_remove_id(user, id):
    if back.remove_id(user, id):
        print('note removed')
    else:
        print('No such id')


def login():
    print("You are about to login")
    username = input("Put Username")
    password = input("Put password")
    user = back.login(username, password)
    if user:
        while user:
            i = input('======================= \n'
                      'To create note \"c\" \n'
                      'to print all notes \"p\" \n'
                      'to find by id \"i\" \n'
                      'to delete by index \"d\" \n'
                      'press \"e\" to exit')
            if i == "c":
                title = input("Input title")
                text = input("Input text")
                back.create_note(user, title, text)
                return True
            elif i == 'p':
                print_notes(user)
                return True
            elif i == 'i':
                id = input('Put note id')
                print_note_id(user, id)
                return True
            elif i == 'd':
                id = input('Put note id')
                print_remove_id(user, id)
                return True
            elif i == 'e':
                user = False
            else:
                user = True
        else:
            return
    else:
        print("Wrong password")
        return True

