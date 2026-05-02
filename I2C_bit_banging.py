import RPi.GPIO as GPIO
import time
from I2C_functions import send_msg, start, send_ack_bit, stop, read_byte

CLK = 11
DATA = 10
sleep_time = 0.00001

GPIO.setmode(GPIO.BCM) #define como se nombran los pines
GPIO.setwarnings(False) #para que no grite por setear los pines muchas veces

msg_write = 0b10100000
msg_read  = 0b10100001

wrd_add_1 = 0b00000000
wrd_add_2 = 0b00000010

'''
start(DATA,CLK)
print(send_msg(msg_read,8,DATA,CLK))
print(read_byte(DATA,CLK))
send_ack_bit(DATA,CLK,1)
stop(DATA,CLK)
'''

start(DATA,CLK)
print(send_msg(msg_write, 8,DATA, CLK))
print(send_msg(wrd_add_1, 8, DATA, CLK))
print(send_msg(wrd_add_2, 8, DATA, CLK))
start(DATA,CLK)
print(send_msg(msg_read,8,DATA,CLK))
print(read_byte(DATA,CLK))
send_ack_bit(DATA,CLK,ack=False)
stop(DATA,CLK)