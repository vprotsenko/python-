import random
import subprocess
from pynput import keyboard

class Cursor:
    cursor_position = [[False, True, False, False],
                       [False, False, False, False],
                       [False, False, False, False],
                       [False, False, False, False]]

    def get_cursor_position(self):
        cursor = [0,0]
        for i in self.cursor_position:
            try:
                cursor[1]=i.index(True)
                break
            except ValueError:
                cursor[0]+=1
        return cursor

    def set_position(self, new_position):
        curr_position=self.get_cursor_position()
        try:
            if new_position[0] >= 0 and new_position[1] >= 0:
                self.cursor_position[new_position[0]][new_position[1]]=True
                self.cursor_position[curr_position[0]][curr_position[1]]=False


                return True
            else:
                print('You are at the border')

        except IndexError:
            print('You are at the border')
            return False


    def move_down(self):
        move=self.get_cursor_position()
        move[0]=move[0]+1
        self.set_position(move)

    def move_up(self):
        move=self.get_cursor_position()
        move[0]=move[0]-1
        self.set_position(move)

    def move_left(self):
        move=self.get_cursor_position()
        move[1]=move[1]-1
        self.set_position(move)

    def move_right(self):
        move=self.get_cursor_position()
        move[1]=move[1]+1
        self.set_position(move)

class Field(Cursor):
    field = [[], [], [], []]


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

    def move_digit(self):
        c_position=self.get_cursor_position()
        print('curr'+str(c_position))
        digit=self.field[c_position[0]][c_position[1]]
        print('digit'+str(digit))
        new_position= []

        try:
            if self.field[c_position [0]+1][c_position[1]] == None:
                try:
                    new_position=[c_position[0]+1, c_position[1]]
                except IndexError:
                    print('nok')
            elif self.field[c_position[0]-1][c_position[1]] == None:
                try:
                    new_position=[c_position[0]-1, c_position[1]]
                except IndexError:
                    print('nok')
            elif self.field[c_position[0]][c_position[1]-1] == None:
                try:
                    new_position=[c_position[0], c_position[1]-1]
                except IndexError:
                    print('nok')
            elif self.field[c_position[0]][c_position[1]+1] == None:
                try:
                    new_position=[c_position[0], c_position[1]+1]
                except IndexError:
                    print('nok')
            else:
                return

            self.field[new_position[0]][new_position[1]]=digit
            self.field[c_position[0]][c_position[1]]=None

        except IndexError:
            print('bad step')

    def display_field(self):
        cursor=self.get_cursor_position()
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



f=Field()
c=Cursor()

f.set_field()

def on_press(key):
    try:
        k = key.char # single-char keys
    except:
        k = key.name # other keys

    if key == keyboard.Key.esc:
        return False # stop listener

    if k == 'left':
        subprocess.call("cls", shell=True)
        c.move_left()
        f.display_field()

    elif k == 'right':
        subprocess.call("cls", shell=True)
        c.move_right()
        f.display_field()
    elif k == 'up':
        subprocess.call("cls", shell=True)
        c.move_up()
        f.display_field()
    elif k == 'down':
        subprocess.call("cls", shell=True)
        c.move_down ()
        f.display_field()
    elif k == 'space':
        subprocess.call("cls", shell=True)
        f.move_digit()
        f.display_field()


f.display_field()
lis = keyboard.Listener(on_press=on_press)
lis.start() # start to listen on a separate thread
lis.join() # no this if main thread is polling self.keys










