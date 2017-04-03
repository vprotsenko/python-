import pickle
my_list=[1,2,3,45,3,467,4,8,9,9,]

f=open('test','wb')
pickle.dump(my_list, f)
f.close()

login pass note(body title)
f2=open('test', 'rb')
my_new_list=pickle.load(f2)
print(my_new_list)