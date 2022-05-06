import pyautogui


positionName = 'Jynx.png'
position = None
while (position == None):
    position = pyautogui.locateOnScreen(positionName, grayscale=True,confidence=0.8)
    print("Conferindo posicao=" + positionName)