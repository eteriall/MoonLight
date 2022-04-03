import sys

from PyQt5.QtWidgets import QApplication, QWidget

from utilities import *
import time

if __name__ == "__main__":
    app = QApplication(sys.argv)

    log('Все модули загружены успешно!')

    main_window = MainWindow(None)
    main_window.show()
    app.exec()

    for i in range(1, 15 + 1):
        log(f'Поиск установки, порт COM{i}..', cls=True)
        time.sleep(.5)
    else:
        log('Ошибка подключения к установке. ', t='err')
