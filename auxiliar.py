import string
import pyautogui
import time
from PIL import Image
import numpy as np
import keyboard
import datetime
import cv2


#pyautogui.displayMousePosition()
path = "images/deadPokemon/dugtrio1.png"
img = cv2.imread(path)
print(img.shape)

width,height = 51,42
imgResize = cv2.resize(img,(width,height))
print(imgResize.shape)


cv2.imwrite("images/deadPokemon/testDugtrio.png",imgResize)
time.sleep(0.4)
position = pyautogui.locateOnScreen('images/deadPokemon/testDugtrio.png', confidence=0.6)

if(position):
    print("Encontrou")
else:
    print("None")

cv2.waitKey(0)



