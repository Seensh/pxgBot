import pyautogui
import time
from PIL import Image
import numpy as np

#pyautogui.displayMousePosition()

positionBatalha = pyautogui.locateOnScreen('images/batalha/batalha.png', grayscale=True, confidence=0.7)
if(positionBatalha):
    positionCenterBatalha = pyautogui.center(positionBatalha)
    positionX = positionCenterBatalha.x-45
    positionY = positionCenterBatalha.y+78
    largura = positionX-577
    altura = positionY-490
    scBatalha = pyautogui.screenshot(region=(positionX,positionY,largura,altura))
    scBatalha.save('images/batalha/batalhaCheia.png')

positionBatalhaVazia = pyautogui.locateOnScreen('images/batalha/batalhaCheia.png', grayscale=True, confidence=0.7)

if(positionBatalhaVazia):
    print("Vazia")
else:
    print("Tem algo")




