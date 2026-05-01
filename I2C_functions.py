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

def stop(SDA_pin, SCL_pin): #la transición de SDA de LOW a HIGH con SCL en HIGH es la condición de STOP

    _SCL_low(SCL_pin)
    _SDA_low(SDA_pin)
    time.sleep(sleep_time)

    _SCL_high(SCL_pin)
    time.sleep(sleep_time)

    _SDA_high(SDA_pin)  		#STOP
    time.sleep(sleep_time)

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

def read_byte(SDA_pin, SCL_pin):

    byte = 0

    _SDA_high(SDA_pin)  #soltamos SDA

    for i in range(8):

        _SCL_low(SCL_pin)
        time.sleep(sleep_time)

        _SCL_high(SCL_pin)
        time.sleep(sleep_time)

        bit = GPIO.input(SDA_pin) #lee el bit del pin SDA

        byte = (byte << 1) | bit #arma el byte

    _SCL_low(SCL_pin)

    return byte

def send_ack_bit(SDA_pin, SCL_pin, ack=True):
    
    #ack=True -> manda ACK (0)
    #ack=False -> manda NACK (1)

    _SCL_low(SCL_pin)
    time.sleep(sleep_time)

    if ack:
        _SDA_low(SDA_pin)   #ACK
    else:
        _SDA_high(SDA_pin)  #NACK

    time.sleep(sleep_time)

    _SCL_high(SCL_pin)
    time.sleep(sleep_time)

    _SCL_low(SCL_pin)
    time.sleep(sleep_time)

    _SDA_high(SDA_pin)  #soltamos SDA