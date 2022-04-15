import sys

from PyQt5.QtWidgets import QApplication, QWidget

from utilities import *
import time

if __name__ == "__main__":
    app = QApplication(sys.argv)

    log('Все модули загружены успешно!')

    main_window = MainWindow(Arduino(3))
    main_window.show()
    app.exec()
