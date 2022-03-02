# from gpiozero import Robot
# from time import sleep

# motor = Robot(left=(7,8),right=(10,12))
# motor.forward()
# sleep(2)
# motor.backward()
# sleep(2)
# motor.reverse
# sleep(2)
# motor.stop()

import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(8, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.output(12, 50)

# try catch keyboard interrupt
# try :
#     while True :
#         GPIO.output(8, GPIO.HIGH)
# except KeyboardInterrupt :
#     GPIO.output(7, GPIO.LOW)
#     GPIO.output(8, GPIO.LOW)
#     GPIO.output(12, GPIO.LOW)
#     GPIO.cleanup()


try :
    while True :
        x = input("direction:")
        if x == "a":
            GPIO.output(7, GPIO.HIGH)
            GPIO.output(8, GPIO.LOW)
        elif x == "d":
            GPIO.output(7, GPIO.LOW)
            GPIO.output(8, GPIO.HIGH)
        elif x == "s":
            GPIO.output(7, GPIO.LOW)
            GPIO.output(8, GPIO.LOW)

except KeyboardInterrupt :
    GPIO.output(7, GPIO.LOW)
    GPIO.output(8, GPIO.LOW)
    GPIO.output(12, GPIO.LOW)
    GPIO.cleanup()
        