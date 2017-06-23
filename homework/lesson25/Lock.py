from threading import Lock

class MyLock:
    lock = Lock()

l=MyLock()


print(l.lock.acquire())
print(l.lock.acquire())

'''
wait - блокирует поток если флаг не установлен
clear - сбрасывает флажок set
set - ставит флаг не блокировать или освобождает от wait
'''

