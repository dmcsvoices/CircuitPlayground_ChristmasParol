# Parol2020
import time
import board
import pulseio
import adafruit_irremote
import neopixel

#Set up the LED Pins
ledA = pulseio.PWMOut(board.A1, frequency=5000, duty_cycle=0)
ledB = pulseio.PWMOut(board.A2, frequency=5000, duty_cycle=0)
ledC = pulseio.PWMOut(board.A3, frequency=5000, duty_cycle=0)
ledD = pulseio.PWMOut(board.A6, frequency=5000, duty_cycle=0)

# Create a 'pulseio' input, to listen to infrared signals on the IR receiver
pulsein = pulseio.PulseIn(board.IR_RX, maxlen=120, idle_state=True)

# Create a decoder that will take pulses and turn them into numbers
decoder = adafruit_irremote.GenericDecode()

#setup neopixels
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=.05, auto_write=False)
pixels.fill((0, 0, 0))
pixels.show()

RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
LIGHTBLUE = (153, 255, 255)
LAVENDAR = (153, 51, 255)
PINK = (255, 153, 255)
PURPLE = (180, 0, 255)
WHITE = (255, 255, 255)
OFF = (0, 0, 0)

def color_chase(color, wait):
    for i in range(10):
        pixels[i] = color
        time.sleep(0.01)
        pixels.show()
        pixels[i] = OFF
        #time.sleep(wait)
        pixels.show()
    time.sleep(0.01)

def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        return (0, 0, 0)
    if pos < 85:
        return (255 - pos * 3, pos * 3, 0)
    if pos < 170:
        pos -= 85
        return (0, 255 - pos * 3, pos * 3)
    pos -= 170
    return (pos * 3, 0, 255 - pos * 3)

def rainbow_cycle(wait):
    for j in range(255):
        for i in range(10):
            rc_index = (i * 256 // 10) + j * 5
            pixels[i] = wheel(rc_index & 255)
        pixels.show()
        time.sleep(wait)


def rainbow(wait):
    for j in range(255):
        for i in range(len(pixels)):
            idx = int(i + j)
            pixels[i] = wheel(idx & 255)
        pixels.show()
        time.sleep(wait)

def ShineA(wait):
    color_chase(GREEN,0.01)
    for i in range(100):
        # PWM LED up and down
        if i < 50:
            ledA.duty_cycle = int(i * 2 * 65535 / 100)  # Up
        else:
            ledA.duty_cycle = 65535 - int((i - 50) * 2 * 65535 / 100)  # Down
        time.sleep(wait)

def ShineB(wait):
    color_chase(WHITE,0.01)
    for i in range(100):
        # PWM LED up and down
        if i < 50:
            ledB.duty_cycle = int(i * 2 * 65535 / 100)  # Up
        else:
            ledB.duty_cycle = 65535 - int((i - 50) * 2 * 65535 / 100)  # Down
        time.sleep(wait)


def ShineC(wait):
    color_chase(RED,0.01)
    for i in range(100):
        # PWM LED up and down
        if i < 50:
            ledC.duty_cycle = int(i * 2 * 65535 / 100)  # Up
        else:
            ledC.duty_cycle = 65535 - int((i - 50) * 2 * 65535 / 100)  # Down
        time.sleep(wait)

def ShineD(wait):
    color_chase(GREEN,0.01)
    for i in range(100):
        # PWM LED up and down
        if i < 50:
            ledD.duty_cycle = int(i * 2 * 65535 / 100)  # Up

        else:
            ledD.duty_cycle = 65535 - int((i - 50) * 2 * 65535 / 100)  # Down

        time.sleep(wait)



def AllFastBlink(wait):
    ledA.duty_cycle = 65535
    ledB.duty_cycle = 65535
    ledC.duty_cycle = 65535
    ledD.duty_cycle = 65535
    time.sleep(wait)
    ledA.duty_cycle = 0
    ledB.duty_cycle = 0
    ledC.duty_cycle = 0
    ledD.duty_cycle = 0
    color_chase(GREEN,0.01)
    time.sleep(wait)

def FastRotateCCW(wait):
    ledA.duty_cycle = 65535
    time.sleep(wait)
    ledA.duty_cycle = 0
    time.sleep(wait)
    ledC.duty_cycle = 65535
    time.sleep(wait)
    ledC.duty_cycle = 0
    time.sleep(wait)
    ledD.duty_cycle = 65535
    time.sleep(wait)
    ledD.duty_cycle = 0
    time.sleep(wait)
    ledB.duty_cycle = 65535
    time.sleep(wait)
    ledB.duty_cycle = 0
    time.sleep(wait)
    color_chase(GREEN,0.01)

def FastRotateCW(wait):
    ledA.duty_cycle = 65535
    time.sleep(wait)
    ledA.duty_cycle = 0
    time.sleep(wait)
    ledB.duty_cycle = 65535
    time.sleep(wait)
    ledB.duty_cycle = 0
    time.sleep(wait)
    ledD.duty_cycle = 65535
    time.sleep(wait)
    ledD.duty_cycle = 0
    time.sleep(wait)
    ledC.duty_cycle = 65535
    time.sleep(wait)
    ledC.duty_cycle = 0
    color_chase(RED,0.01)
    time.sleep(wait)

def UpDown(wait):
    ledA.duty_cycle = 65535
    time.sleep(wait)
    ledA.duty_cycle = 0
    color_chase(WHITE,0.01)
    time.sleep(wait)
    ledB.duty_cycle = 65535
    ledC.duty_cycle = 65535
    time.sleep(wait)
    ledB.duty_cycle = 0
    ledC.duty_cycle = 0
    color_chase(RED,0.01)
    time.sleep(wait)
    ledD.duty_cycle = 65535
    time.sleep(wait)
    ledD.duty_cycle = 0
    time.sleep(wait)
    ledB.duty_cycle = 65535
    ledC.duty_cycle = 65535
    time.sleep(wait)
    ledB.duty_cycle = 0
    ledC.duty_cycle = 0
    color_chase(GREEN,0.01)
    time.sleep(wait)


while True:
    UpDown(0.1)
    time.sleep(.01)
    UpDown(0.1)
    time.sleep(.01)
    UpDown(0.1)
    time.sleep(.01)
    UpDown(0.1)
    time.sleep(.01)
    AllFastBlink(0.1)
    FastRotateCCW(0.1)
    time.sleep(0.001)
    AllFastBlink(0.1)
    FastRotateCW(0.1)
    time.sleep(0.01)
    AllFastBlink(0.1)
    time.sleep(0.01)
    AllFastBlink(0.1)
    time.sleep(0.01)
    AllFastBlink(0.1)
    time.sleep(0.01)
    AllFastBlink(0.1)
    time.sleep(0.01)
    AllFastBlink(0.1)
    time.sleep(0.01)

