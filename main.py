import RPi.GPIO as GPIO  # needed to use IO Pins on the Raspberry Pi
import time  # to use the sleep function
from tkinter import *  # just to create a temporary UI
from tkinter import ttk
import threading  # needed to run direction loop and GUI runnning simultaneously

# current direction
direction = 'stop'

# Pin configuration
right_motor = (7, 8, 10, 12)  # rotates clockwise to move forward
left_motor = (12, 11, 13, 15)  # rotates anit-clockwise to move forward

# array of controls
arr = [[GPIO.HIGH, GPIO.LOW, GPIO.LOW, GPIO.LOW],
       [GPIO.LOW, GPIO.HIGH, GPIO.LOW, GPIO.LOW],
       [GPIO.LOW, GPIO.LOW, GPIO.HIGH, GPIO.LOW],
       [GPIO.LOW, GPIO.LOW, GPIO.LOW, GPIO.HIGH]]

# stopped state
stop = [GPIO.LOW, GPIO.LOW, GPIO.LOW, GPIO.LOW]

# setup
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(right_motor, GPIO.OUT)
GPIO.setup(left_motor, GPIO.OUT)


def rotate_clockwise(motor):
    for i in range(3, -1, -1):
        GPIO.output(motor, arr[i])
        time.sleep(0.03)


def rotate_anticlockwise(motor):
    for i in range(0, 4):
        GPIO.output(motor, arr[i])
        time.sleep(0.03)


# To keep the motors running
def direction_loop():
    global direction
    while True:
        if direction == 'forward':
            rotate_clockwise(right_motor)
            rotate_anticlockwise(left_motor)
            print('moving forward')
        elif direction == 'left':
            rotate_anticlockwise(right_motor)
            rotate_anticlockwise(left_motor)
            print('turning left')
        elif direction == 'backward':
            rotate_anticlockwise(right_motor)
            rotate_clockwise(left_motor)
            print('moving backward')
        elif direction == 'right':
            rotate_clockwise(right_motor)
            rotate_clockwise(left_motor)
            print('turning right')
        elif direction == 'stop':
            GPIO.output(right_motor, stop)
            GPIO.output(left_motor, stop)
            print('stopped')
            continue
        else:
            continue


# set new direction
def set_direction(new_direction):
    global direction
    direction = new_direction


# Controller
def create_gui():
    root = Tk()
    frm = ttk.Frame(root, padding=10)
    frm.grid()
    ttk.Label(frm, text="Controller").grid(column=0, row=0)
    ttk.Button(frm, text="Forward", command=lambda: set_direction(
        'forward')).grid(column=2, row=1)
    ttk.Button(frm, text="Backward", command=lambda: set_direction(
        'backward')).grid(column=2, row=3)
    ttk.Button(frm, text="Left", command=lambda: set_direction(
        'left')).grid(column=1, row=2)
    ttk.Button(frm, text="Right", command=lambda: set_direction(
        'right')).grid(column=3, row=2)
    ttk.Button(frm, text="Stop", command=lambda: set_direction(
        'stop')).grid(column=2, row=2)
    ttk.Button(frm, text="Quit", command=root.destroy).grid(column=5, row=6)
    root.mainloop()


# threading
if __name__ == '__main__':
    p1 = threading.Thread(target=direction_loop)
    p2 = threading.Thread(target=create_gui)
    p1.start()
    p2.start()
    p1.join()
    p2.join()


# main loop
# while True:
#     GPIO.output(right_motor, arr[3])
#     time.sleep(0.03)
#     GPIO.output(right_motor, arr[2])
#     time.sleep(0.03)
#     GPIO.output(right_motor, arr[1])
#     time.sleep(0.03)
#     GPIO.output(right_motor, arr[0])
#     time.sleep(0.03)

# except KeyboardInterrupt:
#    GPIO.cleanup()

# def take_input():
#     global direction
#     while True:
#         x = input("Enter a direction: ")
#         if x == "f":
#             print("forward")
#             direction = 'forward'
#         elif x == "l":
#             print("left")
#             direction = 'left'
#         elif x == "b":
#             print("backward")
#             direction = 'backward'
#         elif x == "r":
#             print("right")
#             direction = 'right'
#         elif x == "s":
#             print("stop")
#             direction = 'stop'
#         elif x == "q":
#             direction = 'stop'
#             GPIO.cleanup()
#             print("quit")
#             break
#         else:
#             print("invalid input")
#             continue
