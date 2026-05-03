from I2C_bus import SoftI2C
import time


DATA = 10   # pin SDA
CLK  = 11   # pin SCL


i2c = SoftI2C(DATA, CLK)

i2c.init()

'''
i2c.init()
i2c.start()
print(i2c.write_byte(0b10100001))
i2c.stop()
'''

i2c.start()
i2c.write_byte(0b10100000)
i2c.write_byte(0b00000000)
i2c.write_byte(0b00000010)
i2c.write_byte(0b01010101)
i2c.stop()

time.sleep(0.01) # WRITE CYCLE TIME t_wr

i2c.start()
i2c.write_byte(0b10100000)
i2c.write_byte(0b00000000)
i2c.write_byte(0b00000010)
i2c.start()
i2c.write_byte(0b10100001)
print(i2c.read_byte(ack=False))
i2c.stop()