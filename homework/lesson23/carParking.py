class Level:
    def __init__(self, box_size, number):
        self.box_size = box_size
        self.number = number
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)

    def del_car(self, id):
        for c in self.cars:
            if c.id == id:
                self.cars.remove(c)


class Car:
    def __init__(self, name, size):
        self.name = name
        self.id = 0
        self.size = size


class Parking:
    levels = []
    id = 10

    def addLevel(self, box_size, number):
        self.levels.append(Level(box_size, number))

    def get_freeSpace(self, car_size):
        for i in self.levels:
            if i.box_size > car_size:
                if i.number > 0:
                    return i
                else:
                    return None

    def gen_id(self):
        self.id += 1
        return self.id

    def park_vehicle(self, car):
        free_box = self.get_freeSpace(car.size)
        if free_box:
            free_box.number -= 1
            car.id = self.gen_id()
            free_box.add_car(car)

            print('Your {0} parked with ID-{1} in box size {2}'.format(car.name, car.id, free_box.box_size))
        else:
            print('No free parking')

    def find_car(self, your_id):
        find_car = False
        for level in self.levels:
            if your_id in level.cars:
                print(your_id)
                print(level)
                level.cars.remove[your_id]
                find_car = True

        if find_car:
            print("Take your car")
        else:
            print("No car in parking")


p = Parking()
p.addLevel(10, 5)
p.addLevel(20, 10)
p.park_vehicle(Car('Honda', 5))
p.park_vehicle(Car('Kia', 5))
p.park_vehicle(Car('VW', 5))
p.park_vehicle(Car('Audi', 5))
p.park_vehicle(Car('Bentley', 15))
p.find_car(11)
