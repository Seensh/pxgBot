import string
import pyautogui
import time
from PIL import Image
import numpy as np
import keyboard
import datetime


#pyautogui.displayMousePosition()
dateTimeNow = datetime.datetime.now()
StringDateTimeNow = str(dateTimeNow)
StringDateTimeNowReplaces = StringDateTimeNow.replace(":", "-")
scBatalhaLog = pyautogui.screenshot()
nomeImagem = 'images/logBatalha/' + StringDateTimeNowReplaces + '.png'
scBatalhaLog.save(nomeImagem)
print(nomeImagem)



