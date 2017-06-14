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
        x=self.get_cursor()[0]+x
        y=self.get_cursor()[1]+y
        print(x,y)

        if x >= 0 and y >= 0 and y < 4 and x < 4:
            self.cur_position[0]=x
            self.cur_position[1]=y
            return True
        else:
            return False

    def check_move_digit(self, x, y):
        try:
            if self.field[x][y] is None:
                return True
        except IndexError:
            return False

    def move_digit(self, arg=None):
        pos=self.get_cursor()
        x=pos[0]
        y=pos[1]
        if self.check_move_digit(x+1, y):
            now=self.field[x][y]
            self.field[x][y]=None
            self.field[x+1][y]=now
            return True
        elif self.check_move_digit(x-1, y):
            now=self.field[x][y]
            self.field[x][y]=None
            self.field[x-1][y]=now
            return True
        elif self.check_move_digit(x, y+1):
            now=self.field[x][y]
            self.field[x][y]=None
            self.field[x][y+1]=now
            return True
        elif self.check_move_digit(x, y-1):
            now=self.field[x][y]
            self.field[x][y]=None
            self.field[x][y-1]=now
            return True
        else:
            return False

    def move_up(self, arg=None):
        self.set_cursor(-1, 0)

    def move_down(self, arg=None):
        self.set_cursor(1,0)

    def move_left(self, arg=None):
        self.set_cursor(0,-1)

    def move_right(self, arg=None):
        self.set_cursor(0,+1)

    def display_field(self):
        cursor=self.get_cursor()
        print(cursor)
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
    handlers={'u':f.move_up,
              'd':f.move_down,
              'l':f.move_left,
              'r':f.move_right,
              's':f.move_digit
              }

    while True:
        print('let\'s go')

        command=input('Chice = ')

        if len(command) > 0:
            handlers[command]('ok')
            f.display_field()

        time.sleep(0.2)

main()
