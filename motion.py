import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

ms_pin = 4
GPIO.setup(ms_pin,GPIO.IN,pull_up_down = GPIO.PUD_DOWN)
print('armed and ready')
try:
    i = 0
    while True:
        if GPIO.input(ms_pin):
            i = i +1
            print('BOOM!',i)
            sleep(1)
            continue
except KeyboardInterrupt:
    print('bye')
    GPIO.cleanup()
