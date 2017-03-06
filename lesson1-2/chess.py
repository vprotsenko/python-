my_input = input("enter value: ")
numeric_side = ['1', '2', '3', '4', '5', '6', '7', '8']
alphabet_side = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']



black = []

for h in range(4):
    for w in range(4):
        black.append(numeric_side[::2][h] + alphabet_side[::2][w])
for h in range(4):
    for w in range(4):
        black.append(numeric_side[1::2][h] + alphabet_side[1::2][w])


if my_input in black:
    print("black")
else:
    print("white")
