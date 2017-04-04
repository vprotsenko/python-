import pickle
import hashlib
db={}

def sync_var():
    global db
    try:
        db=pickle.load(open('user_db', 'rb'))
    except FileNotFoundError:
        pickle.dump({}, open('user_db', 'wb'))
        db=pickle.load(open('user_db', 'rb'))


def dump_var_to_db():
    pickle.dump(db, open('user_db', 'wb'))


def check_user(login):
    user_list=db.keys()
    if login in user_list:
        return True
    else:
        return False

def add_user(login, password, email):
    if check_user(login):
        return False
    else:
        p=str(hashlib.sha1(password.encode('utf-8')).hexdigest())
        db.update({login:{'password':p, 'email':email}})
        dump_var_to_db()
        return True


def registration():
    username=input("Put Username")
    password=input("Put password")
    email=input("Put email")
    if add_user(username, password, email) is True:
        print("User added")
    else:
        print("User already exist")


def login():
    username=input("Put Username")
    password=input("Put password")
    if username in db.keys():

        p=str(hashlib.sha1(password.encode('utf-8')).hexdigest())
        if db[username]['password'] == p:
            print('welcome')
            return username
        else:
            print('wrong login or password')
            return None
    else:
        print('wrong login or password')


def start_screen():
    sync_var()

    a = True
    while a:
        print(db)
        choice = input("Press \"l\" to login or \"r\" for registration")
        if choice == 'r':
            registration()
            a = False
        elif choice == 'l':
            login()
            a = True
        else:
            a = False

    dump_var_to_db()


start_screen()