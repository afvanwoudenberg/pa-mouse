# pa-mouse.py
# Aswin van Woudenberg

import cv2
import numpy as np
import os
import tkinter as tk
from pynput.mouse import Button, Controller
from io import BytesIO
from PIL import Image

def run():
    """
    Use the webcam to capture the Pictionary Air pen and control the mouse pointer.
    """
    vc = cv2.VideoCapture(0)
    is_capturing = vc.isOpened()
    if is_capturing:
        # setup canvas
        cam_width  = int(vc.get(cv2.CAP_PROP_FRAME_WIDTH))
        cam_height = int(vc.get(cv2.CAP_PROP_FRAME_HEIGHT))
        
        # find screen dimensions
        root = tk.Tk()
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        
        factor_x = screen_width / cam_width
        factor_y = screen_height / cam_height

    mouse = Controller()

    running = True
    pressed = False
    
    while running and is_capturing:
        try:
            is_capturing, frame = vc.read()
            frame = cv2.flip(frame, 1)
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            
            # red mask
            # setting the lower and upper range for mask1
            lower_red = np.array([0, 100, 100])
            upper_red = np.array([20, 255, 255])
            mask1 = cv2.inRange(hsv, lower_red, upper_red)
            # setting the lower and upper range for mask2
            lower_red = np.array([160, 100, 100])
            upper_red = np.array([180, 255, 255])
            mask2 = cv2.inRange(hsv, lower_red, upper_red)
            mask_red = mask1 + mask2

            contours, _ = cv2.findContours(mask_red.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            
            # if the contours are formed
            if len(contours) > 0:
                # find the largest contour 
                contour = sorted(contours, key = cv2.contourArea, reverse = True)[0] 

                # get the radius and position of the enclosing circle
                ((x, y), _) = cv2.minEnclosingCircle(contour)
                x, y = int(x), int(y)

                # move the mouse
                mouse.position = (int(x * factor_x), int(y * factor_y))
                # release the button is not released already
                if pressed:
                    pressed = False
                    mouse.release(Button.left)
            else:
                # green mask
                # setting the lower and upper range for mask_green
                lower_green = np.array([55, 40, 40])
                upper_green = np.array([95, 255, 255])
                mask_green = cv2.inRange(hsv, lower_green, upper_green)

                contours, _ = cv2.findContours(mask_green.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

                # if the contours are formed
                if len(contours) > 0:
                    # find the largest contour 
                    contour = sorted(contours, key = cv2.contourArea, reverse = True)[0] 

                    # get the radius and position of the enclosing circle
                    ((x, y), _) = cv2.minEnclosingCircle(contour)
                    x, y = int(x), int(y)

                    # move the mouse
                    mouse.position = (int(x * factor_x), int(y * factor_y))
                    # press the button is not pressed already
                    if not pressed:
                        pressed = True
                        mouse.press(Button.left)
        except KeyboardInterrupt:
            running = False    
    is_capturing = False
    vc.release()

def set_short_exposure_time():
    """Setup webcam with shorter exposure time"""
    os.system("v4l2-ctl -c auto_exposure=1 -c exposure_dynamic_framerate=0 -c exposure_time_absolute=10")

def restore_camera_settings():
    """Restore camera settings"""
    os.system("v4l2-ctl -c auto_exposure=3 -c exposure_dynamic_framerate=1")

if __name__ == '__main__':
    set_short_exposure_time()
    run()
    restore_camera_settings()

