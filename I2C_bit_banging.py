import RPi.GPIO as GPIO
import time
from I2C_functions import send_msg, start, send_ack_bit, stop, read_byte

CLK = 11
DATA = 10
sleep_time = 0.00001

GPIO.setmode(GPIO.BCM) #define como se nombran los pines
GPIO.setwarnings(False) #para que no grite por setear los pines muchas veces

msg = 0b010100001

start(DATA,CLK)
print(send_msg(msg,8,DATA,CLK))
print(read_byte(DATA,CLK))
send_ack_bit(DATA,CLK,1)
stop(DATA,CLK)
