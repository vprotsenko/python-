def string(word):
    word=list(word)
    word_dict={}
    for i in range(len(word)):
        if word[i] not in word_dict:
            word_dict[word[i]]=1
        else:
            word_sum=word_dict[word[i]]
            word_dict[word[i]]=word_sum+1


    for i in word_dict:
        print(i, word_dict[i])

string('dsfffdgggyyyyyy66655')
print(u'a')
string('dsfffdgggyyyyyy66655'.encode('koi8-r').decode('utf8'))

'''
Описать функцию, которая принимает один аргумент - строку.
Вернуть В виде словаря буквы и частоту их использования - где ключ - буква, где значение - частота этой буквы в строке.
'''