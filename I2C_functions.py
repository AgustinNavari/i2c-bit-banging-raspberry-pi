import RPi.GPIO as GPIO
import time

sleep_time = 0.00001

def _SDA_high(pin):
    GPIO.setup(pin, GPIO.IN)

def _SDA_low(pin):
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, 0)

def _SCL_high(pin):
    GPIO.setup(pin, GPIO.IN)
    while GPIO.input(pin) == 0:  # podría darse el caso que el slave este sosteniendo SCL en low por que necesita más tiempo. Lo esperamos
    	pass

def _SCL_low(pin):
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, 0)

def start(SDA_pin,SCL_pin): #la transicion de SDA de HIGH a LOW con SCL en HIGH es la condición de START

	_SDA_high(SDA_pin)
	_SCL_high(SCL_pin)
	time.sleep(sleep_time)

	_SDA_low(SDA_pin)		#START
	time.sleep(sleep_time)

	_SCL_low(SCL_pin)


def send_msg(msg_to_send, msg_size, SDA_pin, SCL_pin):

	_SCL_low(SCL_pin)
	time.sleep(sleep_time)

	for i in range(msg_size):

		bit_to_send = msg_to_send >> (msg_size - 1 - i) & 1

		if(bit_to_send):
			
			_SDA_high(SDA_pin)

		else:

			_SDA_low(SDA_pin)

		time.sleep(sleep_time)
		_SCL_high(SCL_pin)		#esclavo lee 
		time.sleep(sleep_time)
		_SCL_low(SCL_pin)

	# Acknowledge: despues de enviar el mensaje el slave responde con un ACK

	_SCL_low(SCL_pin)
	time.sleep(sleep_time)

	_SDA_high(SDA_pin) #soltamos SDA
	time.sleep(sleep_time)

	_SCL_high(SCL_pin) #clockeamos
	time.sleep(sleep_time)

	ack = GPIO.input(SDA_pin)	#leemos SDA: 0 -> ACK  1 -> NACK. El slave mantiene la linea mientras SCL este en high.

	_SCL_low	(SCL_pin)
	time.sleep(sleep_time)

	return ack

