#Created by: Dexter Dixon
import cv2
import numpy as np
import pygame
import json

# Set the width and height of the screen [width,height]
size = [500, 700]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Benthic Species")


cv2.namedWindow("Vision")

camera1 = cv2.VideoCapture(0)
camera2 = cv2.VideoCapture(1)

camera1.set(3,480);
camera1.set(4,320);

camera2.set(3,480);
camera2.set(4,320);


while(True):
    
    screen.fill(WHITE)
    textPrint.reset()
    # Capture frame-by-frame
    ret, frame1 = camera1.read()
    ret, frame2 = camera2.read()
    
    # Combines both cameras into one frame & saves the frame of the image as Image.png
    final = cv2.hconcat([frame1, frame2])
    cv2.imwrite("Image.png", final)

    # Makes a request sending our Image file and retreives the predictions in the variable
    predictions = requests.post('https://northcentralus.api.cognitive.microsoft.com/customvision/v3.0/Prediction/7551bb7b-b510-423e-870e-3807dd1e3c4d/detect/iterations/Iteration4/image',
        headers={
        "Prediction-Key"   : "3e932ad5bed84b548310d92f76c595d3",
        "Content-Type" : "application/octet-stream"
        },data{"Image.png":/home/pi/Desktop})
    
    predictoins_Decoded = json.loads(predictions)

    textPrint.output(screen, "Results")
    textPrint.indent()
    textPrint.output(screen, predictions_Decoded)
    pygame.display.flip()

    #Display the resulting frame
    cv2.imshow('Vission',final)
    #cv2.imshow('Camera 2',frame2)

    key = cv2.waitKey(20)
    if key == 27: # exit on ESC
        break

cv2.destroyWindow("Vission")
vc.release()
