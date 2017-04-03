from random import randint
word="privet"

def rand_word(w):
    new_w=[]
    w=list(w)
    while w:
        r=randint(0, len(w)-1)
        new_w.append(w.pop(r))
    return new_w


def replace(w):
    correct_w=list(w)
    incorect_w=rand_word(w)
    print(correct_w, incorect_w)

    while correct_w != incorect_w:
        my_input=input("put 2 digits")
        num1=int(my_input.split(" ")[0])-1
        num2=int(my_input.split(" ")[1])-1

        incorect_w.insert(num2, incorect_w.pop(num1))
        print("".join(incorect_w))


replace(word)