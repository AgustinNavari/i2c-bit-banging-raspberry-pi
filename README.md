# i2c-bit-banging-raspberry-pi

Bit-banged I2C implementation in Python for Raspberry Pi using GPIO.

## Estructura

```text
i2c_bitbang/
  lowlevel.py          # Manejo crudo de SDA/SCL con GPIO open-drain
  bus.py               # API generica de bus I2C: read, write, scan
  devices/
    eeprom24xx.py      # Driver de ejemplo para memorias EEPROM 24xx
examples/
  eeprom_read.py       # Ejemplo de uso
```

La idea es que `lowlevel.py` no sepa nada de direcciones ni dispositivos.
`bus.py` conoce el protocolo I2C generico. Los archivos dentro de `devices/`
conocen detalles de cada integrado.

## Uso basico

```python
from i2c_bitbang import SoftI2C

bus = SoftI2C(sda_pin=10, scl_pin=11)

devices = bus.scan()
print([f"0x{address:02X}" for address in devices])
```

## EEPROM 24xx

```python
from i2c_bitbang import SoftI2C
from i2c_bitbang.devices import EEPROM24xx

bus = SoftI2C(sda_pin=10, scl_pin=11)
eeprom = EEPROM24xx(bus, address=0x50, address_size=2, page_size=64)

eeprom.write(0x0000, b"hola")
print(eeprom.read(0x0000, 4))
```

## Notas electricas

I2C necesita resistencias pull-up en SDA y SCL. Esta libreria simula salidas
open-drain: para escribir un `0` configura el pin como salida baja, y para
escribir un `1` lo libera configurandolo como entrada.
