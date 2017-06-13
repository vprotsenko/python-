import random
from msvcrt import getch
import time


class Field():
    field = [[], [], [], []]

    cur_position=[0,0]

    def __init__(self):
        self.set_field()

    def set_field(self):
        digits = []
        for i in range(1, 16):
            digits.append(int(i))

        digits.append(None)
        random.shuffle(digits)

        digit_position = 0
        for i in range(4):
            for g in range(0, 4):
                self.field[i].append(digits[digit_position])
                digit_position += 1

    def get_cursor(self):
        return self.cur_position

    def set_cursor(self, x, y):
        try:
            x=x-1
            y=y-1
            if self.field[x][y]:
                self.cur_position=[x,y]
                return True
        except IndexError:
            print('No such ')
            return False


    def check_move_digit(self, x, y):
        try:
            x=x-1
            y=y-1
            if self.field[x][y] is None:
                return True
        except IndexError:
            return False

    def move_digit(self, arg=None):
        pos=self.get_cursor()
        x=pos[0]
        y=pos[1]

        if self.check_move_digit(x+1, y):
            self.set_cursor(x+1, y)
            return True
        elif self.check_move_digit(x-1, y):
            self.set_cursor(x-1, y)
            return True
        elif self.check_move_digit(x, y+1):
            self.set_cursor(x, y+1)
            return True
        elif self.check_move_digit(x, y-1):
            self.set_cursor(x, y-1)
            return True
        else:
            return False


    def display_field(self):
        cursor=self.get_cursor()
        splitter = '---------------------'
        print(splitter)
        x = 0
        for i in self.field:
            line = []
            y=0
            for c in range(0, 4):
                if cursor != [x,y] and i[c] is None:
                    line.append('|    |')
                elif cursor == [x,y] and i[c] is None:
                    line.append('| * *|')
                elif cursor == [x,y] and i[c] < 10:
                    line.append('|*{0}* |'.format(i[c]))
                elif cursor == [x,y] and i[c] >= 10:
                    line.append('|*{0}*|'.format(i[c]))
                elif cursor != [x,y] and i[c] < 10:
                    line.append('| {0}  |'.format(i[c]))
                elif cursor != [x,y] and i[c] >= 10:
                    line.append('| {0} |'.format(i[c]))
                y+=1
            x += 1
            print(''.join(line).replace('||', '|'))
        print(splitter)


def main():

    f=Field()
    f.display_field()

    handlers={'up':f.set_cursor(f.get_cursor()[0]+1, f.get_cursor()[1]),
              'down':f.set_cursor(f.get_cursor()[0]-1, f.get_cursor()[1]),
              'left':f.set_cursor(f.get_cursor()[0], f.get_cursor()[1]-1),
              'right':f.set_cursor(f.get_cursor()[0], f.get_cursor()[1]+1),
              'space':f.move_digit()
    }

    while True:

        print(ord(getch()))
        time.sleep(0.2)

main()