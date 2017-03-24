while True:
    i=input('Put digits')

    try:
        i=int(i)
        print(2/i)
    except ValueError:
        print("Digits only input")
    except ZeroDivisionError:
        print('Don\'t devide on 0')
