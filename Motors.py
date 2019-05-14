print("Starting")
import os
import time
import pygame
import brooklyn
import cv2
import numpy as np
#from PrintText import TextPrint

pygame.init()

#BLUE = (0, 0, 128)
#WHITE = (255, 255, 255)

#size = [500, 700]
#screen = pygame.display.set_mode(size)

#textPrint = TextPrint()
#clock = pygame.time.Clock()
#pygame.display.set_caption("Robot Status")

#Initialize Board
pwm = brooklyn.Brooklyn("COM20")
pwm.setcard(1, brooklyn.EMPIRE_STATE)
pwm.setcard(2, brooklyn.EMPIRE_STATE)
pwm.setcard(3, brooklyn.EMPIRE_STATE)
pwm.setcard(4, brooklyn.EMPIRE_STATE)
pwm.begin()
Running = True
#white and yellow
#Forward/Backward/Turn
motor_1 = 1500
motor_2 = 1500

#Forward/Backward
motor_3 = 1500

#Front: Up/Down/Rotation
motor_4 = 1500
motor_5 = 1500

#Back: Up/Down
motor_6 = 1500


#Claw Clamp
servo_1 = 1000

#Claw Rotate
servo_2 = 1000

M1 = pwm.getservo(1, 1) #Green/Red  Black/Blue
M2 = pwm.getservo(1, 2) #Green/Black  Black/Red
M3 = pwm.getservo(1, 3) #Green/Red  Black/Blue
M4 = pwm.getservo(2, 1) #Green/Red  Black/Blue
M5 = pwm.getservo(2, 2) #Green/Red  Black/Blue
M6 = pwm.getservo(2, 3) #Green/Red  Black/Blue
S1 = pwm.getservo(1, 4)
S2 = pwm.getservo(2, 4)

joystick = pygame.joystick.Joystick(0)
joystick.init()

M1.setangle(motor_1)
M2.setangle(motor_2)
M3.setangle(motor_3)
M4.setangle(motor_4)
M5.setangle(motor_5)
M6.setangle(motor_6)
S1.setangle(servo_1)
S2.setangle(servo_2)

cv2.namedWindow("Vision")
camera1 = cv2.VideoCapture(1)
camera1.set(3,480)
camera1.set(4,320)

time.sleep(1)
print("Initialized")
while(Running):

    ret, frame1 = camera1.read()
    cv2.imshow('Vision',frame1)

    pygame.event.get()

    M1.setangle(int(motor_1))
    M2.setangle(int(motor_2))
    M3.setangle(int(motor_3))
    M4.setangle(int(motor_4))
    M5.setangle(int(motor_5))
    M6.setangle(int(motor_6))
    S1.setangle(int(servo_1))
    S2.setangle(int(servo_2))
    (hat_x,hat_y) = joystick.get_hat(0)   
    #Forward: LStick
    if joystick.get_axis(1) >= 0.2:
        motor_1 = (200*joystick.get_axis(1))+1500
        motor_2 = (200*joystick.get_axis(1))+1500
        motor_3 = (200*joystick.get_axis(1))+1500
        print("Moving Backwards")
    #Backwards: LStick
    elif joystick.get_axis(1) <= -0.2:
        motor_1 = (200*joystick.get_axis(1))+1500
        motor_2 = (200*joystick.get_axis(1))+1500
        motor_3 = (200*joystick.get_axis(1))+1500
        print(" Moving Forward")
    #Up: R1
    elif joystick.get_button(4) == 1:
        motor_5 = 1610
        motor_4 = 1610
        motor_6 = 1650
        print("Moving Down")
    #Down: L1
    elif joystick.get_button(5) == 1:
        motor_5 = 1350
        motor_4 = 1350
        motor_6 = 1350
        print("Moving Up")

    # Roll-: L3
    elif joystick.get_button(8) == 1:
        motor_5 = 1700
        motor_4 = 1300
        print("Roll-")
    # Roll+: R3
    elif joystick.get_button(9) == 1:
        motor_5 = 1300
        motor_4 = 1700
        print("Roll+ ")
    #Turning +: R2
    elif joystick.get_axis(4) >= 0.5:
        motor_1 = 1300
        motor_2 = 1700
        print("Turning Right")
    #Turning -: L2
    elif joystick.get_axis(4) <= -0.5:
        motor_1 = 1700
        motor_2 = 1300
        print("Turning Left")
     #Nose Up: RStick
    elif joystick.get_axis(3) >= 0.2:
        motor_4 = (200*-joystick.get_axis(3))+1500
        motor_5 = (200*-joystick.get_axis(3))+1500
        motor_6 = (200*joystick.get_axis(3))+1500
        print("Tilting Nose Up")
    #Nose Down RStick
    elif joystick.get_axis(3) <= -0.2:
        #4,5 down 6 up
        motor_4 = (200*joystick.get_axis(3))+1500
        motor_5 = (200*joystick.get_axis(3))+1500
        motor_6 = 1300
        print("Tilting Nose Down")
    #Claw Rotate: D-UP
    elif hat_x == -1:
        if servo_1 == 2100:
            print("Max")
        else:
            servo_1 +=1 
            print("Claw Roatating Clockwise")
    #Claw Rotate: D-Down
    elif hat_x == 1:
        if servo_1 == 800:
            print("Max")
        else:
            servo_1 -=1  
            print("Claw Rotating Counter Clockwise")

    #Claw Open: D-Right
    elif hat_y == -1:
        if servo_1 == 2100:
            print("Max")
        else:
            servo_1 +=1
            print("Claw Opening")
    #Claw Close: D-Left
    elif hat_y == 1:
        if servo_1 == 800:
            print("Max")
        else:
            servo_1 -=1
            print("Claw Closing")
    elif joystick.get_button(7) == 1:
        Running = False
        print("Stopping Program")
    elif joystick.get_button(6) == 1:
        motor_1 = 1500
        motor_2 = 1500
        motor_3 = 1500
        motor_4 = 1360
        motor_5 = 1360
        motor_6 = 1360
    else:
        motor_1 = 1500
        motor_2 = 1500
        motor_3 = 1500
        motor_4 = 1500
        motor_5 = 1500
        motor_6 = 1500
        print("Idle")
    #screen.fill(WHITE)
    #textPrint.reset()

    #textPrint.output(screen, "Testing")
    #textPrint.indent()
   # pygame.display.flip()
    #clock.tick(20)
    time.sleep(0.01)

print("Stoppig Program")
cv2.destroyWindow("Vision")
pwm.end()
pygame.quit()
