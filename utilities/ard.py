class Arduino:
    def __init__(self, port: int, baudrate:int=9600):
        self.ser = serial.Serial(f"COM{port}", baudrate=baudrate,
                                 timeout=2.5,
                                 parity=serial.PARITY_NONE,
                                 bytesize=serial.EIGHTBITS,
                                 stopbits=serial.STOPBITS_ONE
                                 )
import threading
import serial

connected = False
port = 'COM4'
baud = 9600

#serial_port = serial.Serial(port, baud, timeout=0)


def handle_data(data):
    print(data)


