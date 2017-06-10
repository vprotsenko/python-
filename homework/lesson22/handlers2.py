class Handler:

    handler={}

    def register_handler(self, alias, link):
        self.handler.update({alias: link})

    def unregister_handler(self, alias):
        self.handler.pop(alias)

    def get_aliases_from_command(self, user_input):
        for i in self.handler.keys():
            if i.startswith(user_input[0]):
                return i

    def get_handler(self, alias):
        return self.handler[alias]

    def run(self, user_input):
        self.get_handler(self.get_aliases_from_command(user_input))()


def printHi():
    print('--Hello')


def printBye():
    print('--Bye')

def printCiao():
    print('--Ciao')

handler=Handler()

handler.register_handler('bye',printBye)
handler.register_handler('hi',printHi)
handler.register_handler('Ciao',printCiao)

handler.run('bye')
handler.run('hi')
handler.run('Ciao')








'''
Разработать класс handlers:

Наша вариация -  handlers для обработки пользовательских команд, где первое слово пользовательского ввода,
 является алиасом команды и остальная часть строки после алиаса, является аргументами, если таковые требуются.

Организовать следующие методы:
register_handler - метод принимает два аргумента: алиас команды  и ссылку на функцию или метод обработчик.
 регистрирует(сохраняет) указанный алиас и соответствующий обработчик. Подобных алиасов и обработчиков может быть много.
unregister_handler - метод принимает один аргумент: алиас команды. Удаляет соответствующий хандлер.
get_handler_aliases - метод возвращает все алиасы команд.
get_aliases_from_command - метод принимает один аргумент: строку пользовательского ввода.
Как говорилось, первое слово в строке пользовательского ввода, должно быть алиасом команды.
Учитываем, что алиас может быть сокращенным Т.Е. вместо "copy" - "co" и Т.Д.
Ищет соответствующий алиас в зарегистрированных хандлерах и, если находит, возвращает полный алиас. Если не находит, возвращает None.
get_handler - принимает один аргумент: алиас команды и возвращает соответствующий хандлер.
run - принимает один аргумент: строку пользовательского ввода, определяет алиас, получает хандлер,
выполняет его, передавая в качестве аргумента всю строку пользовательского ввода. (используем методы, описанные выше).
'''