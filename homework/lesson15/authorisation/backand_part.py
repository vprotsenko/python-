import datetime
import pickle
import hashlib

db = {}


def sync_var():
    global db
    try:
        db = pickle.load(open('user_db', 'rb'))
    except FileNotFoundError:
        pickle.dump({}, open('user_db', 'wb'))
        db = pickle.load(open('user_db', 'rb'))


def dump_var_to_db():
    pickle.dump(db, open('user_db', 'wb'))


def check_user(login):
    user_list = db.keys()
    if login in user_list:
        return True
    else:
        return False


def add_user(login, password, email):
    if check_user(login):
        return False
    else:
        p = str(hashlib.sha1(password.encode('utf-8')).hexdigest())
        db.update({login:{'password':p, 'email':email, 'notes':[]}})
        dump_var_to_db()
        return True


def login(username, password):
    if username in db.keys():

        p = str(hashlib.sha1(password.encode('utf-8')).hexdigest())
        if db[username]['password'] == p:
            print('welcome')
            return username
        else:
            return False
    else:
        return False


def create_note(user, title, text):
    db[user]['notes'].append([title, text, datetime.datetime.now()])
    dump_var_to_db()


def get_notes(user):
    return db[user]['notes']


def get_note_id(user, id):
    return db[user]['notes'][id]


def remove_id(user, id):
    try:
        id = int(id)
        db[user]['notes'].pop(id)
        dump_var_to_db()
        return True
    except:
        return False

