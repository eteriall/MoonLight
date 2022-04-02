from utilities import *
import time

time.sleep(4)
log('Все модули загружены успешно!')
time.sleep(2)

for i in range(1, 15 + 1):
    log(f'Поиск установки, порт COM{i}..', cls=True)
    time.sleep(.5)
else:
    log('Ошибка подключения к установке. ', t='err')


