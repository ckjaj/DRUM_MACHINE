from gpiozero import Button
from signal import pause

# Define the button connected to GPIO 17

pins = [19, 13, 6, 5, 10, 9, 25, 8,
		27, 22, 23, 24, 14, 15, 18, 17]

buttons = []

#buttons index + 1 = the beat

for i, pin in enumerate(pins):
	but = Button(pin)

	but.when_pressed = lambda b: print(f"Button was pressed")
	but.when_released = lambda b: print(f"Button was released")

	buttons.append(but)




pause() # Keeps the program running