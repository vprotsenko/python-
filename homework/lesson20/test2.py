import datetime

#decorators
def log(f):
    def write(text):
        open('chat.log', 'w').write(str(f(text)))
        return f(text)
    return write


def time(f):
    def add_time(text):
        return str(f(text)) + ' ' + str(datetime.datetime.now())

    return add_time

def beep(f):
    def add_time(text):
        new_text=''
        for i in text.split():
            if i == 'fuck':
                new_text+='BEEP '
            else:
                new_text+=i + ' '

        print(new_text)
        return f(text)

    return add_time

@log
@time
@beep
def send_text(any):
    return any

print(send_text('fuck off '))