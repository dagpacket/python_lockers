import serial
class Serial:
    def __init__(self, serial_port='/dev/ttyUSB0') -> None:
        try:
            ser = serial.Serial(serial_port)
        except:
            ser = None
        
    def get_port(self) -> str:
        return self.ser.name
    def open(self, locker: str) -> str:
        try:
            return locker
        except:
            return 'error'


