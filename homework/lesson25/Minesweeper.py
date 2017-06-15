from random import randint
from msvcrt import getch
import time, subprocess

class Game():

    game=True
    field=[]
    cursor=[0,0]

    looser_counter=0

    def __init__(self, field_size=8, mine_num=15):
        self.field_size=field_size
        self.mine_num=mine_num
        self.mine_list=[]
        self.create_field()
        self.add_mine()

    def create_field(self):
        for lineX in range(self.field_size):
            y=[]
            for lineY in range(self.field_size):
                y.append(None)
            self.field.append(y)

    def creat_mine(self):
        mine=[randint(0, self.field_size), randint(0, self.field_size)]
        if mine != [0, 0]:
            return mine

    def add_mine(self):
        for i in range(self.mine_num):
            self.mine_list.append(self.creat_mine())

    def check_mine(self, x,y):
        for i in self.mine_list:
            if i == [x, y]:
                return True

    def look_around(self):
        x,y=self.cursor
        count=0
        #up
        if self.check_mine(x+1, y):
            count+=1
        if self.check_mine(x+1, y-1):
            count+=1
        if self.check_mine(x+1, y+1):
            count+=1
        #down
        if self.check_mine(x-1, y):
            count+=1
        if self.check_mine(x-1, y-1):
            count+=1
        if self.check_mine(x-1, y+1):
            count+=1
        #midle
        if self.check_mine(x, y+1):
            count+=1
        if self.check_mine(x, y-1):
            count+=1
        return count

    def move_cursor(self, x, y):
        if self.field_size > x >= 0 and self.field_size > y >= 0:
            self.cursor=[x,y]
            return True
        else:
            return False

    def left(self, arg=None):
        x,y=self.cursor
        self.move_cursor(x,y-1)

    def right(self, arg=None):
        x,y=self.cursor
        self.move_cursor(x,y+1)

    def up(self, arg=None):
        x,y=self.cursor
        self.move_cursor(x-1,y)

    def down(self, arg=None):
        x,y=self.cursor
        self.move_cursor(x+1,y)

    def open(self, arg=None):
        x,y=self.cursor
        if [x,y] in self.mine_list and self.field[x][y] != 'X':
            self.field[x][y]='M'
            self.game=False
        else:
            self.field[x][y]=self.look_around()

    def mark(self, arg=None):
        x,y=self.cursor
        if self.field[x][y] == None:
            self.field[x][y] = 'X'
            if not self.check_mine(x,y):
                self.looser_counter+=1

        elif self.field[x][y] == 'X':
            self.field[x][y] = None
            if not self.check_mine(x,y):
                self.looser_counter-=1


    def display_field(self):
        splitter = '---------------------'
        print(splitter)
        x = 0
        for i in self.field:
            line = []
            y=0
            for c in range(0, self.field_size):
                if self.field[x][y] == None:
                    if self.cursor != [x,y]:
                        line.append('|    |')
                    elif self.cursor == [x,y]:
                        line.append('| * *|')
                else:
                    if self.cursor != [x,y]:
                        line.append('| {}  |'.format(self.field[x][y]))
                    elif self.cursor == [x,y]:
                        line.append('|*{}* |'.format(self.field[x][y]))
                y+=1
            x += 1
            print(''.join(line).replace('||', '|'))
        print(splitter)



def main():

    g=Game()
    g.display_field()
    handlers={'72':g.up,
              '80':g.down,
              '75':g.left,
              '77':g.right,
              '32':g.open,
              '13':g.mark
              }

    while g.game:
        time.sleep(0.2)
        command=str(ord(getch()))
        print(command)
        if len(command) > 0 and command in handlers.keys():
            subprocess.call("cls", shell=True)
            handlers[command]('ok')
            g.display_field()

        print(g.looser_counter)
        if g.looser_counter >3:
            g.game=False
    print('Game over')
    time.sleep(500)
main()

