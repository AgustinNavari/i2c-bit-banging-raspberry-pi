from I2C_bus import SoftI2C


DATA = 10   # pin SDA
CLK  = 11   # pin SCL


i2c = SoftI2C(DATA, CLK)


i2c.init()
i2c.start()
print(i2c.write_byte(0b10100001))

i2c.stop()