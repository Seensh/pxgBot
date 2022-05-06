import pyautogui
import keyboard
import time
from datetime import datetime

def functionMain():   

    while keyboard.is_pressed('c') == False:

        now = datetime.now()
        print("começo = ", now)

        positionNameDewgong = None
        positionNameCloyster = None
        positionNamePosicao1 = 'posicao1.png'
        positionNamePosicao2 = 'posicao2.png'
        positionNamePosicao3 = 'posicao3.png'
        positionNamePosicao4 = 'posicao4.png'
        positionNamePosicao5 = 'posicao5.png'

        time.sleep(1)
        functionAndar(906,155)
        time.sleep(2)
        functionConferirPosicao(positionNamePosicao1)
        time.sleep(1)
        functionMonstro(positionNameDewgong, positionNameCloyster)
        time.sleep(2)
        functionAndar(877,164)
        time.sleep(2)
        functionConferirPosicao(positionNamePosicao2)
        time.sleep(1)
        functionMonstro(positionNameDewgong, positionNameCloyster)
        time.sleep(2)
        functionAndar(899,169)
        time.sleep(2)
        functionConferirPosicao(positionNamePosicao3)
        time.sleep(1)
        functionMonstro(positionNameDewgong, positionNameCloyster)
        time.sleep(2)
        functionAndar(856,166)
        time.sleep(2)
        functionConferirPosicao(positionNamePosicao4)
        time.sleep(1)
        functionMonstro(positionNameDewgong, positionNameCloyster)
        time.sleep(2)
        functionAndar(822,76)
        time.sleep(2)
        functionConferirPosicao(positionNamePosicao5)
        time.sleep(2)        
        now = datetime.now()
        print("fim = ", now)
        functionAlimentarPoke()



def functionMonstro(positionNameDewgong, positionNameCloyster):
    #ficar parado
    positionNameDewgong = "N/A"
    count = 0
    while (positionNameDewgong != None or positionNameCloyster != None):      
        positionNameDewgong = pyautogui.locateOnScreen('cloyster.png', grayscale=True,confidence=0.8)
        positionNameCloyster = pyautogui.locateOnScreen('dewgong.png', grayscale=True,confidence=0.8)
        time.sleep(4)
        #captura Shiny Jynx
        #positionDeadDugtrio = pyautogui.locateOnScreen('../images/batalha//cloyster.png', grayscale=True, confidence=0.7)
        #time.sleep(0.5)
        #if (positionDeadDugtrio != None):
        #    positionSuperball = pyautogui.locateOnScreen('../images/ball/super.png',confidence=0.7)
        #    time.sleep(1)
        #    if(positionSuperball != None):
        #        positionCenterSuperball = pyautogui.center(positionSuperball)
        #        positionCenterDeadDugtrio = pyautogui.center(positionDeadDugtrio)
        #        time.sleep(0.5)
        #        pyautogui.click(positionCenterSuperball.x,positionCenterSuperball.y,button='right')
        #        time.sleep(1)
        #        pyautogui.click(positionCenterDeadDugtrio.x,positionCenterDeadDugtrio.y)
        print("verificando monstro")
        count += 1
        if(count > 15):
                print("coletando espólios de batalha")
                keyboard.press('e')
        if(count > 35):
            return
    print("coletando espólios de batalha")
    keyboard.press('e')
    return

def functionAndar(x,y):
    pyautogui.click(x,y)
    print("andando")
    return

def functionConferirPosicao(positionName):
    position = None
    while (position == None):
        position = pyautogui.locateOnScreen(positionName, grayscale=True)
        print("Conferindo posicao=" + positionName)
    return

def functionAlimentarPoke():
    pizza = pyautogui.locateOnScreen('pizza.png', grayscale=True,confidence=0.8)
    if(pizza):
        pizzaCenter = pyautogui.center(pizza)
        pyautogui.click(pizzaCenter.x,pizzaCenter.y,button='right')
        poke = pyautogui.locateOnScreen('poke.png', grayscale=True,confidence=0.8)
        if(poke):
            pokeCenter = pyautogui.center(poke)
            pyautogui.click(pokeCenter.x,pokeCenter.y)
            print("entrei e me alimentei")


functionMain()


