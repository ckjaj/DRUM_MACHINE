from gpiozero import Button
from signal import pause

button1 = Button(22)
button1.name = "1"
button2 = Button(27)
button2.name = "2"
button3 = Button(23)
button3.name = "3"
button4 = Button(24)
button4.name = "4"

def but_pres(b):
	print(f"Button {b.name} was pressed")

def but_rele(b):
	print(f"Button {b.name} was released")

button1.when_pressed = but_pres
button1.when_released = but_rele

button2.when_pressed = but_pres
button2.when_released = but_rele

button3.when_pressed = but_pres
button3.when_released = but_rele

button4.when_pressed = but_pres
button4.when_released = but_rele


pause()