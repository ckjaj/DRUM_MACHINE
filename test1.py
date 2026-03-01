from gpiozero import Button
from signal import pause

button1 = Button(22)
button2 = Button(27)
button3 = Button(23)
button4 = Button(24)

def but_pres():
	print(f"Button was pressed")

def but_rele():
	print(f"Button was pressed")

button1.when_pressed = but_pres
button1.when_released = but_rele

button2.when_pressed = but_pres
button2.when_released = but_rele

button3.when_pressed = but_pres
button3.when_released = but_rele

button4.when_pressed = but_pres
button4.when_released = but_rele


pause()