
# this is my code on how to track blue,green,red colors with open cv
import cv2 as cv 
import numpy as np

cap = cv.VideoCapture(0) # captures video

while(1):
    _, frame = cap.read() # reads vidoe
    
    # now the bgr colors are converted to hsv coloring
    hsv_blue = cv.cvtColor(frame, cv.COLOR_BGR2HSV) # hsv blue
    hsv_green = cv.cvtColor(frame, cv.COLOR_BGR2HSV) # hsv green
    hsv_red = cv.cvtColor(frame, cv.COLOR_BGR2HSV) # hsv red

    # now the minium and maximum colors are set
    min_blue  = np.array([94,50,50])
    max_blue  = np.array([108,255,255])
    min_green  = np.array([60,110,60])
    max_green = np.array([80,115,255])
    min_red  = np.array([0,150,127])
    max_red  = np.array([178,255,255])
    
    # now the colors ranges are set
    blue_mask = cv.inRange(hsv_blue,min_blue,max_blue)
    green_mask = cv.inRange(hsv_green,min_green,max_green)
    red_mask = cv.inRange(hsv_red,min_red,max_red)
    

    # also the res is set
    res_blue = cv.bitwise_and(frame,frame, mask= blue_mask)
    res_green = cv.bitwise_and(frame,frame, mask= green_mask)
    res_red = cv.bitwise_and(frame,frame, mask= red_mask)
     

    # now camera shows the mask colors and res. 
    cv.imshow('frame',frame)
    cv.imshow('mask',blue_mask)
    cv.imshow('mask',green_mask)
    cv.imshow('mask',red_mask)
    
    cv.imshow('res',res_blue)

    cv.imshow('res',res_green)
    cv.imshow('res',res_red)
    if cv.waitKey(1) == ord('q'):
        break

# When everything done, release the capture
# 

    
cv.destroyAllWindows()