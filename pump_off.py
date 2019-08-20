from gpiozero import Motor

pump = Motor(17, 18)
pump.stop()