from gpiozero import LED


class LED_Control:

    def __init__(self):
        self.green_led = LED(6)
        self.red_led = LED(26)
        self.State = "Off"

    def green_LED(self):
        if self.State == "Green":
            self.green_led.off()
            self.State = "Off"

        elif self.State == "Red":
            self.red_led.off()
            self.green_led.on()
            self.State = "Green"

        else:
            self.green_led.on()
            self.State = "Green"

    def red_LED(self):
        if self.State == "Red":
            self.red_led.off()
            self.State = "Off"

        elif self.State == "Green":
            self.green_led.off()
            self.red_led.on()
            self.State = "Red"

        else:
            self.red_led.on()
            self.State = "Red"
