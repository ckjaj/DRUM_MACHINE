from gpiozero import Button
from signal import pause

# Define the button connected to GPIO 17
button = Button(17)

def button_pressed():
    print("Button was pressed!")

def button_released():
    print("Button was released!")

# Assign functions to events
button.when_pressed = button_pressed
button.when_released = button_released

pause() # Keeps the program running