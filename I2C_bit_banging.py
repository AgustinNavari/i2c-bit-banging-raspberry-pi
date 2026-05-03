import RPi.GPIO as GPIO
import time
from I2C_lowlevel import _start, _stop, _send_byte, _read_byte, _send_ack_bit

CLK = 11
DATA = 10
sleep_time = 0.00001

GPIO.setmode(GPIO.BCM) #define como se nombran los pines
GPIO.setwarnings(False) #para que no grite por setear los pines muchas veces

msg_write = 0b10100000
msg_read  = 0b10100001

msg = 0b10101010

wrd_add_1 = 0b00000000
wrd_add_2 = 0b00000000

'''
start(DATA,CLK)
print(send_msg(msg_read,8,DATA,CLK))
print(read_byte(DATA,CLK))
send_ack_bit(DATA,CLK,1)
stop(DATA,CLK)
'''



_start(DATA,CLK)
print(_send_byte(msg_write, DATA, CLK))
print(_send_byte(wrd_add_1, DATA, CLK))
print(_send_byte(wrd_add_2, DATA, CLK))
_start(DATA,CLK)
print(_send_byte(msg_read, DATA, CLK))
print(_read_byte(DATA,CLK))
_send_ack_bit(DATA,CLK,ack=False)
_stop(DATA,CLK)

'''
start(DATA,CLK)
print(send_msg(msg_write, 8,DATA, CLK))
print(send_msg(wrd_add_1, 8, DATA, CLK))
print(send_msg(wrd_add_2, 8, DATA, CLK))
print(send_msg(msg, 8, DATA, CLK))
stop(DATA,CLK)
'''