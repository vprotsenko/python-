rooms = {'1':{'name':'room1', 'description':'this is room one    ', 'exit':{'east': '2', 'south': '4'}, 'invent':[]},
        '2':{'name':'room2', 'description':'this is room two    ', 'exit':{'west': '1','east': '3','south': '5'}, 'invent':[]},
        '3':{'name':'room3', 'description':'this is room three  ', 'exit':{'west': '2','south': '6'}, 'invent':[]},
        '4':{'name':'room4', 'description':'this is room four   ', 'exit':{'north': '1','south': '7','east': '5'}, 'invent':['macbook']},
        '5':{'name':'room5', 'description':'this is room five   ', 'exit':{'north': '2','south': '8','east': '6','west': '4'}, 'invent':['food']},
        '6':{'name':'room6', 'description':'this is room six    ', 'exit':{'west': '5','south': '9','north': '3'}, 'invent':['botle']},
        '7':{'name':'room7', 'description':'this is room seven  ', 'exit':{'north': '4','east': '8'}, 'invent':[]},
        '8':{'name':'room8', 'description':'this is room eight  ', 'exit':{'north': '5','east': '9','west': '7'}, 'invent':['book']},
        '9':{'name':'room9', 'description':'this is room nine   ', 'exit':{'north': '6', 'west': '8'}, 'invent':[]},
        }



char = {'position':'1', 'invent':['apple']}

#1 2 3
#4 5 6
#7 8 9


def move(direction):
    global char
    position=char['position']
    room_id=rooms[position]['exit']
    if room_id.get(direction):
        char['position']=str(room_id.get(direction))
        describe_room()
    else:
        print("No such exit")


def describe_room(arg=None):
    id=char['position']
    print("___________\n|{0} \n|Description: {1}\n|Invents: {2}\n___________".format(rooms[id]['name'], rooms[id]['description'], rooms[id]['invent']))


def describe_pocket(arg=None):
    print("Your pocket has: {0}".format(char['invent']))


def describe_handlers(arg=None):
    print("Handler list:")
    for i in handlers.keys():
        print("- " + i)


def describe_room_directions(arg=None):
    id = char['position']
    exits = rooms[id]['exit']
    for i in exits:
        room_id = exits[i]
        print(i, rooms[room_id]['name'])


def move_invent(move_from, move_to):
    if len(move_from) > 0:
        thing = str(input("What to take hare? "))
        if thing in move_from:
            move_from.remove(thing)
            move_to.append(thing)
            return thing
        else:
            return False
    else:
        return False


def put(arg=None):
    movement=move_invent(char['invent'], rooms[char['position']]['invent'])
    if movement:
        print("You lef " + movement + " in this room")
    else:
        print("You don't have it")


def take(arg=None):
    movement=move_invent(rooms[char['position']]['invent'], char['invent'])
    if movement:
        print("You took "+ movement + " in this room")
    else:
        print("No such thing in this room")


handlers = {'list': describe_handlers,
            'look_room': describe_room,
            'look_pocket': describe_pocket,
          'directions': describe_room_directions,
          'put': put,
          'take': take,
          'west':move,
          'east':move,
          'north':move,
          'south':move}


def main():
    describe_handlers()

    while True:
        command = input("Do your choice ")

        if len(command) != 0 and handlers.get(command.split()[0]):
            handlers[command.split()[0]](command)
        else:
            print("No such choice, please try something from list")

main()
