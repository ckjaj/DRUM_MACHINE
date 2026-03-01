from gpiozero import Button
from signal import pause
from gpiozero import LED
import sys

pins = [27, 24, 22, 23]

pins_led = [5, 6, 16, 26]

for i, pin in enumerate(pins):
	but = Button(pin)
	led = LED(pins_led[i])

<<<<<<< HEAD
=======
	


	led.blink()

>>>>>>> 31ada37 (toggle function)
	def make_pressed(led_ref, n):
		def pressed(b):
			print(f"button {n} pressed")
			if(led.value == 0):
				led.value = 1
			else:
				led.value = 0
		return pressed

	def make_released(led_ref, n):
		def released(b):
			print(f"button {n} released")
		return released

	but.when_pressed = make_pressed(led, str(i+1))
	but.when_released = make_released(led, str(i+1))

	print(f"button @ pin {pin} finished initialized")


try:
	pause()
except KeyboardInterrupt:
	print("\n")
	sys.exit(0)
