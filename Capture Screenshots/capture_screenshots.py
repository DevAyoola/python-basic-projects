# Capture Screenshots

import numpy as np
import cv2
import pyautogui

# Capture screenshot with pyautogui
image = pyautogui.screenshot()

# Convert image from PIL(pillow) and in RGB to numpy array and BGR
image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

# Write image to disk using opencv
cv2.imwrite("image1.png", image)