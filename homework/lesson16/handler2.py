def f1(arg):
    if len(arg.split()) > 1:
        print('f1 {0}'.format(arg.split(" ", 1)[1]))
    else:
        print('f1')

def f2(arg):
    arg=arg.split()
    if len(arg) > 1 and arg[1] == 'start':
        print('f2')
    elif len(arg) > 1:
        print('Error')

def f3(arg=None):
    print("f3")

handlers = {'1': f1, '2': f2, '3': f3}

while True:
    command = input()
    if handlers.get(command.split()[0]):
        handlers[command.split()[0]](command)