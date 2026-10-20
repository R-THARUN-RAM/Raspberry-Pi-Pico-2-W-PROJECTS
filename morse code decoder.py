import machine
import time

# Configured for GP15 and the internal green LED indicator
telegraph_pin = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_UP)
led = machine.Pin("LED", machine.Pin.OUT)

MORSE_CODE_DICT = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E',
    '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
    '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O',
    '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
    '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
    '--..': 'Z', '.----': '1', '..---': '2', '...--': '3', '....-': '4',
    '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9',
    '-----': '0'
}

DOT_MAX_MS = 250       
LETTER_GAP_MS = 1500   

current_letter_buffer = ""
last_state_change = time.ticks_ms()
wires_are_touching = False

print("🚀 THE TELEGRAPH IS LIVE!")
print("Tap your loose metal wire tips together to type Morse code...")

while True:
    pin_value = telegraph_pin.value()
    now = time.ticks_ms()
    
    # Onboard LED indicator lights up when wires make contact
    if pin_value == 0:
        led.value(1)
    else:
        led.value(0)
    
    # CASE 1: Wires touch
    if pin_value == 0 and not wires_are_touching:
        time.sleep_ms(30) # Solid anti-glitch filter
        if telegraph_pin.value() == 0:
            wires_are_touching = True
            press_start_time = now
        
    # CASE 2: Wires separate
    elif pin_value == 1 and wires_are_touching:
        time.sleep_ms(30) 
        if telegraph_pin.value() == 1:
            wires_are_touching = False
            duration = time.ticks_diff(now, press_start_time)
            
            if duration <= DOT_MAX_MS:
                current_letter_buffer += "."
                print(".", end="")
            else:
                current_letter_buffer += "-"
                print("-", end="")
            last_state_change = now

    # CASE 3: Decode letter after silence
    elif pin_value == 1 and not wires_are_touching and current_letter_buffer != "":
        silence_duration = time.ticks_diff(now, last_state_change)
        if silence_duration >= LETTER_GAP_MS:
            if current_letter_buffer in MORSE_CODE_DICT:
                print(f" -> [{MORSE_CODE_DICT[current_letter_buffer]}]")
            else:
                print(" -> [? Try Again]")
            current_letter_buffer = "" 
            last_state_change = now

    time.sleep_ms(5)