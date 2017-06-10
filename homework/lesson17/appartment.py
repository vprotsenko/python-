class Room:
    def __init__(self, long, width, num_windows):
        self.long = long
        self.width = width
        self.num_windows = num_windows

    def get_area(self):
        return self.long * self.width

    def get_num_windows(self):
        return self.num_windows


class Appartment:
    rooms=[]

    def add_room(self, room):
        self.rooms.append(room)

    def get_area_rooms(self):
        square=0
        for i in self.rooms:
            square+=int(i.get_area())
        return square

    def get_num_windows_rooms(self):
        windows=0
        for i in self.rooms:
            windows+=int(i.get_num_windows())
        return windows


app=Appartment()

app.add_room(Room(5,4,1))
app.add_room(Room(3,3,0))
app.add_room(Room(5,3,4))

print(app.get_area_rooms())

print(app.get_num_windows_rooms())


#Homework, read blog about classes
#