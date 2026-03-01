from gpiozero import Button
from signal import pause

pins = [22, 27, 23, 24]

names = {}

for i, pin in enumerate(pins):
	but = Button(pin)
	names[pin] = str(i+1)
	but.when_pressed = lambda b: print(f"button {names[b.pin.number]} pressed")
	but.when_released = lambda b: print(f"button {names[b.pin.number]} released")
	print(f"button @ pin {pin} finished initialized")


pause()