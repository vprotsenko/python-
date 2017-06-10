'''
class Person:
    _name = ''

    def get_name(self):
        return self._name

    def set_name(self, n):
        if len(n) > 2:
            self._name = n.capitalize()

    name = property(get_name(), set_name())

#p=Person()
'''

from urllib import request
import json
from urllib.parse import quote_plus

url = 'https://api.privatbank.ua/p24api/pboffice?json&city={0}&address={1}'

def requestapi(city, address):
    city=quote_plus(city)
    address=quote_plus(address)

    return json.loads(request.urlopen(url.format(city, address)).read().decode('utf-8'))


print(requestapi('Днепропетровск', 'Титова'))

'''
data=request.urlopen(url).read().decode('utf-8')


json_data=json.loads(data)

print(json_data[0]['sale'])

'''

