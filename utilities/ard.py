import threading
import serial


class Arduino:

    def __init__(self, port: int, baudrate: int = 9600):
        self.connected = False
        self.port = f'COM{port}'
        self.baudrate = baudrate
        self.thread = threading.Thread(target=self.read_from_port, args=(self,))
        self.thread.start()

        try:
            self.ser = serial.Serial(self.port, self.baudrate, timeout=0)
            self.connected = True
        except Exception as e:
            self.connected = False
            raise ConnectionError(f'Невозможно открыть serial-соединение (PORT: {self.port}; BR: {self.baudrate})')

    def handle_data(self, data):
        print(data)

    def read_from_port(self):
        while not self.connected:
            while True:
                print("test")
                reading = self.ser.readline().decode()
                self.handle_data(reading)
