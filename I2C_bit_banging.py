import RPi.GPIO as GPIO
import time
from I2C_functions import send_msg, start

CLK = 11
DATA = 10
sleep_time = 0.00001

GPIO.setmode(GPIO.BCM) #define como se nombran los pines
GPIO.setwarnings(False) #para que no grite por setear los pines muchas veces


start(DATA,CLK)

msg = 0b01010101

print(send_msg(msg,8,DATA,CLK))