import threading
import serial


class Arduino:

    def __init__(self, port: int, baudrate: int = 9600):
        self.connected = False
        self.port = f'COM{port}'
        self.baudrate = baudrate

        try:
            self.ser = serial.Serial(self.port, self.baudrate, timeout=15)
            self.connected = True
        except Exception as e:
            self.connected = False
            raise ConnectionError(f'Невозможно открыть serial-соединение (PORT: {self.port}; BR: {self.baudrate})')

