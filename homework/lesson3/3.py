def check_prefix(number, mask):
    if mask in number:
        return True

def check_len(number,number_len):
    if len(number) == number_len:
        return True


def find_number(numbers, prefix, number_len):
    number_len=number_len+1
    for number in numbers:

        if check_prefix(number, prefix) and check_len(number,number_len):
            print(number)



find_number(['+380632272477','+380632272473','+38063227245','+40632272477'], '+380', 12)