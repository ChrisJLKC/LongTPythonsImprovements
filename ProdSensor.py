import spidev
from gpiozero import Button


class Sensor_Control:

    def __init__(self):
        self.spi = spidev.SpiDev()
        self.spi.open(0, 0)
        self.spi.max_speed_hz = 5000
        self.spi.mode = 0b01

        self.button = Button(16)
        self.manual_button = Button(25)

    def moisture_check(self):
        moisture_level_p = self.spi.xfer([0b01100000, 0b00000000])
        moisture_level = (moisture_level_p[0] * 256) + moisture_level_p[1]
        return moisture_level

    def light_check(self):
        light_level_p = self.spi.xfer([0b01110000, 0b00000000])
        light_level = (light_level_p[0] * 256) + light_level_p[1]
        return light_level

    def float_switch(self):
        if not self.button.value:
            return True
        else:
            return False

    def manual_override(self):
        if self.manual_button.value:
            return False
        else:
            return True
