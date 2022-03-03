import RPi.GPIO as GPIO
import time

# left - 7, 8, 11
# right - 10, 12, 13 


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(8, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(10, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.output(11, 100)
GPIO.output(13, 100)

try :
    while True :
        x = input("direction:")
        if x == "a":
            GPIO.output(7, GPIO.HIGH)
            GPIO.output(8, GPIO.LOW)
            GPIO.output(10, GPIO.LOW)
            GPIO.output(12, GPIO.HIGH)
        elif x == "d":
            GPIO.output(7, GPIO.LOW)
            GPIO.output(8, GPIO.HIGH)
            GPIO.output(10, GPIO.HIGH)
            GPIO.output(12, GPIO.LOW)
        elif x == "s":
            GPIO.output(7, GPIO.HIGH)
            GPIO.output(8, GPIO.LOW)
            GPIO.output(10, GPIO.HIGH)
            GPIO.output(12, GPIO.LOW)
        elif x == "w":
            GPIO.output(7, GPIO.LOW)
            GPIO.output(8, GPIO.HIGH)
            GPIO.output(10, GPIO.LOW)
            GPIO.output(12, GPIO.HIGH)
        elif x == "q":
            GPIO.output(7, GPIO.LOW)
            GPIO.output(8, GPIO.LOW)
            GPIO.output(12, GPIO.LOW)
            GPIO.output(10, GPIO.LOW)

except KeyboardInterrupt :
    GPIO.output(7, GPIO.LOW)
    GPIO.output(8, GPIO.LOW)
    GPIO.output(11, GPIO.LOW)
    GPIO.cleanup()
        