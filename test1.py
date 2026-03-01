from gpiozero import Button
from signal import pause
from gpiozero import LED
import sys


pins = [22, 27, 23, 24]

pins_led = [26, 16, 5, 6]

for i, pin in enumerate(pins):
	but = Button(pin)
	led = LED(pins_led[i])

	def make_pressed(led_ref, n):
		def pressed(n):
			print(f"button {n} pressed")
			led_ref.on()
		return pressed

	def make_released(led_ref, n):
		def released(n):
			print(f"button {n} released")
			led_ref.off()
		return released

	but.when_pressed = make_pressed(led, str(i+1))
	but.when_released = make_released(led, str(i+1))

	print(f"button @ pin {pin} finished initialized")


try:
	pause()
except KeyboardInterrupt:
	sys.exit(0)
