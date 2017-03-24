f1 = open('file1', 'r').readlines()[1]
f2 = open('file2', 'r').readlines()



f2.insert(1, f1)
open('file2', 'w').writelines(f2)