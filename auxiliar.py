import pyautogui
import time
from datetime import datetime

now = datetime.now()
 
pizza = pyautogui.locateOnScreen('pizza.png', grayscale=True,confidence=0.8)
pizzaCenter = pyautogui.center(pizza)
pyautogui.click(pizzaCenter.x,pizzaCenter.y,button='right')
poke = pyautogui.locateOnScreen('poke.png', grayscale=True,confidence=0.8)
pokeCenter = pyautogui.center(poke)
pyautogui.click(pokeCenter.x,pokeCenter.y)
pyautogui.displayMousePosition()
