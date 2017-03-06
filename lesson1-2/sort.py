a=[4,24,54,46,1,879,98,5]

small=a[0]
for i in range(len(a)):
    if i > len(a)-2:
        break
    if a[i+1] < a[i]:
        small=a[i+1]

print(small)