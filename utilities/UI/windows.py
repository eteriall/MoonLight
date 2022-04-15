import json
import os
import time

from PyQt5.QtWidgets import QWidget, QFileDialog, QMessageBox

from ._py.experiment import Ui_MainWindow as ExperimentWindowParent
from ._py.main import Ui_MainWindow as MainWindowParent
from PyQt5 import QtWidgets, QtGui


def warning():
    pass

def write_read(ser, x):
    ser.write(bytes(x, 'utf-8'))
    time.sleep(0.05)
    data = ser.readline()
    print(data)
    return data

class ExperimentData:
    def __init__(self, configuration: dict):
        for key in configuration:
            self.__setattr__(key, configuration[key])
        self.validate()

    def validate(self):
        validators = {
            'speed': {'min': 0.1, 'max': 1},
            'distance': {'min': 0.1, 'max': 1},
            'fiber_d': {'min': 0.1, 'max': 1},
            'protect_d': {'min': 0.1, 'max': 1}
        }
        for key in validators:
            value = self.__dict__.get(key)
            _min, _max = (validators[key][k] for k in ('min', 'max'))
            if value is None:
                raise ValueError(f'Отсутствует параметр {key}')
            if value < _min or value > _max:
                raise ValueError(f'Параметр {key} не входит в поле допустимых значений [{_min};{_max}]')
        return True


class ExperimentWindow(QtWidgets.QMainWindow, ExperimentWindowParent):
    def __init__(self, arduino):
        self.ard = arduino
        self.setupUi(self)
        super().__init__()

    def set_experiment_data(self, data):
        try:
            self.data = ExperimentData(data)
        except Exception as e:
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.showMessage('Oh no!')


class MainWindow(QtWidgets.QMainWindow, MainWindowParent):
    def __init__(self, ard=None):
        self.ard = ard
        super(MainWindow, self).__init__()
        self.setupUi(self)

        # Управление конфигурациями оптоволокна
        self.load_btn.clicked.connect(self.load_of_config)
        self.save_btn.clicked.connect(self.save_of_config)
        self.calibrate_btn.clicked.connect(self.calibrate)
        self.start_btn.clicked.connect(self.start_experiment)

    def setObjectName(self, name):
        pass

    def resize(self, *s):
        pass

    def get_of_parameters(self):
        """Returns dict with data from input fields"""
        return {
            k: self.__dict__.get(f'{k}_field').value() for k in ('speed', 'distance', 'fiber_d', 'protect_d')
        }

    def set_of_parameters(self, json: dict):
        """Fills input fields with passed parameters"""
        for key in json:
            self.__dict__[f'{key}_field'].setValue(json[key])

    def load_of_config(self):
        """Opens file selection dialogue and loads optic fiber configuration"""
        fileName, _ = QFileDialog.getOpenFileName(self, "Выберите конфигурацию", "",
                                                  "Параметры Оптоволокна (*.json)")
        if fileName:
            with open(fileName, mode='r') as f:
                self.set_of_parameters(json.load(f))
        pass

    def save_of_config(self):
        """Opens file dialogue and creates new optic fiber configuration file"""
        params = self.get_of_parameters()
        fileName, _ = QFileDialog.getSaveFileName(self, "Новая конфигурация", "",
                                                  "Параметры Оптоволокна (*.json)")
        if fileName:
            with open(fileName, mode='w+') as f:
                json.dump(params, f)
        pass

    def update_experiments_table(self):
        """Reloads experiments data from json file"""
        files = os.listdir('/Experiments')
        for i, f in enumerate(files):
            f = json.load(open(f))
            for j, el in enumerate(('speed', 'distance', 'fiber_d', 'protect_d')):
                self.table.setItem(i, j, f[el])

            self.table.setItem()
    def calibrate(self):
        """Calibrates arduino"""
        try:
            write_read(self.ard.ser, "1")
        except Exception as e:
            print(e, str(e.__traceback__))
        pass

    def start_experiment(self):
        """Opens experiment window with loaded configuration"""
        try:
            d = write_read(self.ard.ser, "2").decode()
            self.msg = QMessageBox()
            self.msg.setIcon(QMessageBox.Information)
            self.msg.setText(d)
            self.msg.setInformativeText(d)
            self.msg.setWindowTitle("Result")
            self.msg.exec_()
        except Exception as e:
            print(e, str(e.__traceback__))
        pass
