import pyautogui
import keyboard
import time
from datetime import datetime

def functionMain():   

    while keyboard.is_pressed('c') == False:

        now = datetime.now()
        print("começo = ", now)

        positionNameDiglett = None
        positionNameDugtrio = None
        positionNamePosicao1 = 'posicao1.png'
        positionNamePosicao2 = 'posicao2.png'
        positionNamePosicao3 = 'posicao3.png'
        positionNamePosicao4 = 'posicao4.png'

        time.sleep(1)
        functionAndar(880,176)
        time.sleep(2)
        functionConferirPosicao(positionNamePosicao1)
        time.sleep(1)
        functionMonstro(positionNameDiglett, positionNameDugtrio)
        time.sleep(2)
        functionAndar(908,109)
        time.sleep(2)
        functionConferirPosicao(positionNamePosicao2)
        time.sleep(1)
        functionMonstro(positionNameDiglett, positionNameDugtrio)
        time.sleep(2)
        functionAndar(842,131)
        time.sleep(2)
        functionConferirPosicao(positionNamePosicao3)
        time.sleep(1)
        functionMonstro(positionNameDiglett, positionNameDugtrio)
        time.sleep(2)
        functionAndar(859,171)
        time.sleep(2)
        functionConferirPosicao(positionNamePosicao4)
        time.sleep(1)
        functionMonstro(positionNameDiglett, positionNameDugtrio)
        time.sleep(2)
        now = datetime.now()
        print("fim = ", now)
        functionAlimentarPoke()



def functionMonstro(positionNameDiglett, positionNameDugtrio):
    #ficar parado
    positionNameDiglett = "N/A"
    while (positionNameDiglett != None or positionNameDugtrio != None):      
        positionNameDiglett = pyautogui.locateOnScreen('dugtrio.png', grayscale=True,confidence=0.8)
        positionNameDugtrio = pyautogui.locateOnScreen('diglett.png', grayscale=True,confidence=0.8)
        time.sleep(4)
        positionHabilidades = pyautogui.locateOnScreen('habilidades.png', grayscale=True)
        if (positionHabilidades != None):
            positionCenterHabilidades = pyautogui.center(positionHabilidades)
            pyautogui.click((positionCenterHabilidades.x + 120),positionCenterHabilidades.y)
            pyautogui.moveTo((positionCenterHabilidades.x + 20),positionCenterHabilidades.y)
        time.sleep(1)
        #captura dugtrio
        positionDeadDugtrio = pyautogui.locateOnScreen('../images/deadPokemon/dugtrio.png', grayscale=True, confidence=0.7)
        time.sleep(0.5)
        if (positionDeadDugtrio != None):
            positionSuperball = pyautogui.locateOnScreen('../images/ball/Superball.png',confidence=0.7)
            time.sleep(1)
            if(positionSuperball != None):
                positionCenterSuperball = pyautogui.center(positionSuperball)
                positionCenterDeadDugtrio = pyautogui.center(positionDeadDugtrio)
                time.sleep(0.5)
                pyautogui.click(positionCenterSuperball.x,positionCenterSuperball.y,button='right')
                time.sleep(1)
                pyautogui.click(positionCenterDeadDugtrio.x,positionCenterDeadDugtrio.y)
                
        
        print("verificando monstro")
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
    pizzaCenter = pyautogui.center(pizza)
    pyautogui.click(pizzaCenter.x,pizzaCenter.y,button='right')
    poke = pyautogui.locateOnScreen('poke.png', grayscale=True,confidence=0.8)
    pokeCenter = pyautogui.center(poke)
    pyautogui.click(pokeCenter.x,pokeCenter.y)
    print("entrei e me alimentei")


functionMain()


