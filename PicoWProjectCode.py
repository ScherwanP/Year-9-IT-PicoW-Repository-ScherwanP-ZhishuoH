import machine #imports machine library, Pin and PWM library from machine and imports time
from machine import Pin, PWM
import time

potentiometer = machine.ADC(26)  # Pin 26 for potentiometer


led = Pin(16, Pin.OUT)  # Pin 16 for LED
button = Pin(15, Pin.IN)  # Pin 15 for button
buzzer = machine.Pin(11, machine.Pin.OUT) #GP11 pin for buzzer
buzzerSound = PWM(buzzer) #controls the pitch of the sound
pin = Pin("LED", Pin.OUT) #creates a variable to turn on the onboard LED

# Function to play a tone on the buzzer
def play_tone(frequency, duration):
    buzzerSound.duty_u16(32768)  # Set duty cycle (50%)
    buzzerSound.freq(frequency)  # Set frequency in Hz
    time.sleep(duration)  # Wait for the duration
    buzzerSound.duty_u16(0)  # Stop the sound
    time.sleep(0.1)  # Small delay after the tone

while True: # WIll run the code forever
    pot_value = potentiometer.read_u16() #Sets pot_value to the potentiometer reader
    print("Potentiometer value: {}".format(pot_value)) #prints the potentiometer value to the terminal
    print(button.value()) #prints the button value to the terminal
    if button.value() == 1:
        # Button and LED logic
        if pot_value < 50000: #if potentiometer value to below 50000
            pin.on() #turns on the onboard LED
            led.off() #turns off the external LED
        if 50000 < pot_value < 60000:
            pin.off() #turns off the onboard LED
            led.on() # turns on the external LED


        # Buzzer tone sequence when potentiometer is above 60000
        elif pot_value > 60000:
            led.off() #turns off the external LED
            play_tone(659, 0.1)  # E note
            play_tone(622, 0.1)  # D# note
            play_tone(659, 0.1)  # E note
            play_tone(622, 0.1)  # D# note
            play_tone(659, 0.1)  # E note
            play_tone(494, 0.1)  # B note
            play_tone(587, 0.1)  # D note
            play_tone(523, 0.1)  # C note
            play_tone(440, 0.1)  # A note
            buzzerSound.duty_u16(0)  # Ensure the buzzer is off after the sequence
            

        # If the potentiometer is below the threshold, turn off the LED
        else:
            pass #avoids error by passing the else statement
    else:
        pin.off() #turns everything off
        led.off()

    time.sleep(0.1)  # Small delay to avoid overwhelming the CPU
