from gpiozero import Motor


class Pump_Control:

    def __init__(self):
        self.pump = Motor(17, 18)
        self.State = False

    def start_pump(self):
        self.State = True
        self.pump.forward()

    def stop_pump(self):
        self.State = False
        self.pump.stop()
