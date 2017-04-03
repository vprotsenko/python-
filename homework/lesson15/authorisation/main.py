import pickle

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


def add_user(login, password):
    if check_user(login):
        return False
    else:
        db.update({login:{'password':password, 'notes':""}})
        return True



sync_var()

a = True
while a:

    if input("Press \"a\" if you want to add user else press enter") == "A":
        username=input("Put Username")
        password=input("Put password")
        notes=input("Put notes")
        if add_user(username, password) is True:
            print("User added")
        else:
            print("User already exist")
        a=True
    else:
        a=False

#add_user('vasia', 'test', ['my notes'])


dump_var_to_db()


