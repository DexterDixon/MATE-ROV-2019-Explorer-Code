#Created by: Dexter Dixon

import time
from adafruit_servokit import ServoKit
import pygame
pygame.init()

motor_1 = 0
motor_2 = 0
motor_3 = 0
motor_4 = 0

servo_1 = 0
servo_2 = 0

pinM1 = 0
pinM2 = 1
pinM3 = 2
PinM4 = 3
pinM5 = 4
pinM6 = 5
pinS1 = 6
pinS2 = 7

#pwm.servo[6].angle = 180
pwm = ServoKit(channels=16)
pwm.continuous_servo[0].throttle = 0

joystick = pygame.joystick.Joystick(0)
joystick.init()

while(True):
    
    move = joystick.get_axis(1)
    move2 = joystick.get_axis(2)
    pygame.event.get()

    motor_1 = 0
    motor_2 = 0
    motor_3 = 0
    motor_4 = 0
    pwm.continuous_servo[0].throttle = move
    pwm.continuous_servo[1].throttle = move2

    
