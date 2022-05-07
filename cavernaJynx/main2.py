import pyautogui
import keyboard
import time
from datetime import datetime

def functionMain():   

    while keyboard.is_pressed('c') == False:

        now = datetime.now()
        print("começo = ", now)
        positionNameJynx = None
        positionNamePosicao1 = 'posicao1.png'
        positionNamePosicao2 = 'posicao2.png'
        positionNamePosicao3 = 'posicao3.png'
        positionNamePosicao4 = 'posicao4.png'
        positionNamePosicao5 = 'posicao5.png'

        time.sleep(1)
        functionAndar(838,179)
        time.sleep(2)
        functionConferirPosicao(positionNamePosicao1)
        time.sleep(1)
        functionMonstro(positionNameJynx)
        time.sleep(2)
        functionAndar(907,177)
        time.sleep(2)
        functionConferirPosicao(positionNamePosicao2)
        time.sleep(1)
        functionMonstro(positionNameJynx)
        time.sleep(2)
        functionAndar(933,98)
        time.sleep(2)
        functionConferirPosicao(positionNamePosicao3)
        time.sleep(1)
        functionMonstro(positionNameJynx)
        time.sleep(2)
        functionAndar(813,135)
        time.sleep(2)
        functionConferirPosicao(positionNamePosicao4)
        time.sleep(1)
        functionMonstro(positionNameJynx)
        time.sleep(1)      
        now = datetime.now()
        print("fim = ", now)
        functionAlimentarPoke()



def functionMonstro(positionNameJynx):
    #ficar parado
    positionNameJynx = "N/A"
    count = 0
    while (positionNameJynx != None):      
        positionNameJynx = pyautogui.locateOnScreen('Jynx.png', grayscale=True,confidence=0.8)
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


