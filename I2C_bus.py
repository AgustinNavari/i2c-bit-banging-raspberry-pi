from I2C_lowlevel import _start, _stop, _send_byte, _read_byte, _send_ack_bit, I2C_init

class SoftI2C:

    def __init__(self, SDA, SCL):
        self.SDA = SDA
        self.SCL = SCL

    def start(self):
        _start(self.SDA, self.SCL)

    def stop(self):
        _stop(self.SDA, self.SCL)

    def write_byte(self, byte):
        return _send_byte(byte, self.SDA, self.SCL) == 0 #ACK (0) devuelve True, NACK (1) devuelve False

    def read_byte(self, ack=True):
        byte = _read_byte(self.SDA, self.SCL)
        _send_ack_bit(self.SDA, self.SCL, ack)
        return byte

    def init(self):
        I2C_init()