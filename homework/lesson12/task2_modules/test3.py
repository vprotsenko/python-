import json
data=['blabla', 123,2.5,True,False,None,[1,2,3], (4,5,6), {'key1': 'value1'}]


json.dump(data, open('test', 'w'), indent=4)


my_json=json.load(open('test', 'r'))
print(dir(my_json))
print(str(my_json))

