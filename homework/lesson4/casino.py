from random import randint



def get_random():
    random_int=randint(1,9)
    return random_int


def get_result(user_input):
    random_int= get_random()
    if user_input == random_int:
        print("Hey you're lucky")
        return False
    else:
        print("Looser")
        print("Number was ", random_int)
        return True

game_status=True

while game_status:
    user_int=int(input("Enter you number \n"))
    if user_int < 1 or user_int > 9:
        print("Hey, we have no such field, please chouse number 1-9")
    else:
        game_status=get_result(user_int)

