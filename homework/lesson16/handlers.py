def one(arg):
    print('f1' + arg)


def two(choice, arg):
    if choice == "2" and arg == "":
        return
    elif choice == "2" and arg != "":
        if arg == ' start':
            print('f2')
        else:
            print("Error")


def three():
    print('f3')


def four():
    print('f4')


status=True
while status:

    ch=input('Put number 1-4 or \'e\' for exit')

    ch.split(" ")
    choice=str(ch[0])
    comment=ch[1:]

    if choice == "1":
        one(comment)
    elif choice == "2":
        two(choice, comment)
    elif choice == "3":
        three(comment)
    elif choice == "4":
        four(comment)
    elif choice == "e":
        status = False
    else:
        print("No such option")