from gpiozero import Button
from signal import pause
<<<<<<< HEAD
from gpiozero import LED


pins = [22, 27, 23, 24]

pins_led = [26, 16, 5, 6]

for i, pin in enumerate(pins):
	but = Button(pin)
	led = LED(pins_led[i])

	
	def make_pressed(led_ref, name):
		def pressed(led_ref, name):
			print(f"button {name} pressed")
			led_ref.on()
		return pressed

	def make_released(led_ref, name):
		def released(led_ref, name):
			print(f"button {name} released")
			led_ref.off()
		return released

	but.when_pressed = make_pressed(led_ref, str(i+1))
	but.when_released = make_released(led_ref, str(i+1))
	print(f"button @ pin {pin} finished initialized")

=======
import sys

pins = [22, 27, 23, 24]

for i, pin in enumerate(pins):
	but = Button(pin)
	but.when_pressed = lambda b: print(f"button {b.pin.number} pressed")
	but.when_released = lambda b: print(f"button {b.pin.number} released")
	print(f"button {pin} initialized")
>>>>>>> 2bbade4 (uh oh)

try:
	pause()
except KeyboardInterrupt:
	sys.exit(0)
