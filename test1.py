from gpiozero import Button
from signal import pause

button1 = Button(0)
button2 = Button(1)
button3 = Button(2)
button4 = Button(3)

button1.when_pressed = lambda: print(f"Button1 was pressed")
button1.when_released = lambda: print(f"Button1 was released")

button2.when_pressed = lambda: print(f"Button2 was pressed")
button2.when_released = lambda: print(f"Button2 was released")

button3.when_pressed = lambda: print(f"Button3 was pressed")
button3.when_released = lambda: print(f"Button3 was released")

button4.when_pressed = lambda: print(f"Button4 was pressed")
button4.when_released = lambda: print(f"Button4 was released")


pause()