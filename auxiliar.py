import pyautogui
import time

positionHabilidades = None
positionHabilidades = pyautogui.locateOnScreen('habilidades.png', grayscale=True)
if(positionHabilidades != None):
    positionCenterHabilidades = pyautogui.center(positionHabilidades)
    pyautogui.click((positionCenterHabilidades.x + 40),positionCenterHabilidades.y)
    pyautogui.moveTo((positionCenterHabilidades.x),(positionCenterHabilidades.y+20))
    time.sleep(0.3)

pyautogui.displayMousePosition()
