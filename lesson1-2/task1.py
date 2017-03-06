a = [1, 2, 3, 4, 5, 6]
b = [7, 8, 9]

a_len = len(a)
b_len = len(b)

new_list = []

for i in range(a_len):
    if i < a_len:
        new_list.append(a[i])
    if i < b_len:
        new_list.append(b[i])

print new_list