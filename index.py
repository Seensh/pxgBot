import pyautogui
import keyboard
import time


def functionMain():   

    while keyboard.is_pressed('c') == False:
        positionVara = None
        positionAgua = None
        positionAguaBorbulhando = None
        positionHabilidades = None 
        count = 0
        time.sleep(1)    

        #CAPTURA POSIÇÃO fechar professor
        positionFechaProf = pyautogui.locateOnScreen('fechaProf.png')
        if (positionFechaProf != None):
            positionCenterFechaProf = pyautogui.center(positionFechaProf)
            pyautogui.click(positionCenterFechaProf.x,positionCenterFechaProf.y)

        time.sleep(2) 
        #CAPTURA POSIÇÃO VARA
        while (positionVara == None):
            positionVara = pyautogui.locateOnScreen('vara.png', grayscale=True,confidence=0.8)
        positionCenterVara = pyautogui.center(positionVara)
        pyautogui.click(positionCenterVara.x,positionCenterVara.y)
        pyautogui.moveTo((positionCenterVara.x),(positionCenterVara.y+20))
        print('Vara')
        time.sleep(2)
        #CAPTURA POSIÇÃO AGUA
        while (positionAgua == None):
            positionAgua = pyautogui.locateOnScreen('agua.png', grayscale=True,confidence=0.8)
        positionCenterAgua = pyautogui.center(positionAgua)
        pyautogui.click(positionCenterAgua.x,positionCenterAgua.y)
        pyautogui.moveTo((positionCenterAgua.x),(positionCenterAgua.y+20))
        print('Agua')
        time.sleep(2)
        positionNaoHaRota = pyautogui.locateOnScreen('images/naoHaRota.png', grayscale=True,confidence=0.7)
        if(positionNaoHaRota != None):
            functionRepetirJogarVara()
        #CAPTURA POSIÇÃO AGUA BORBULHANDO
        while (positionAguaBorbulhando == None):
            positionAguaBorbulhando = pyautogui.locateOnScreen('aguaBorbulhando.png', grayscale=True,confidence=0.8)
        pyautogui.click(positionCenterVara.x,positionCenterVara.y)
        pyautogui.moveTo((positionCenterVara.x),(positionCenterVara.y+20))
        print('Agua Borbulhando')
        time.sleep(0.8)
        positionBatalha = pyautogui.locateOnScreen('images/batalha/batalha.png', grayscale=True, confidence=0.7)
        print('Tirando foto dos pokemons')
        if(positionBatalha):
            positionCenterBatalha = pyautogui.center(positionBatalha)
            positionX = positionCenterBatalha.x-45
            positionY = positionCenterBatalha.y+78
            largura = positionX-577
            altura = positionY-490
            scBatalha = pyautogui.screenshot(region=(positionX,positionY,largura,altura))
            scBatalha.save('images/batalha/batalhaCheia.png')
            print('Tirei foto')
        #CAPTURA POSIÇÃO Hanilidades
        positionHabilidades = pyautogui.locateOnScreen('habilidades.png', grayscale=True)
        while(positionBatalha != None):
            if(positionHabilidades != None):
                positionCenterHabilidades = pyautogui.center(positionHabilidades)
                time.sleep(1)
                pyautogui.click((positionCenterHabilidades.x + 40),positionCenterHabilidades.y)
                time.sleep(2)
                pyautogui.click((positionCenterHabilidades.x + 80),positionCenterHabilidades.y)
                time.sleep(2)
                pyautogui.click((positionCenterHabilidades.x + 120),positionCenterHabilidades.y)
                time.sleep(1)     
                print('Habilidades')           
            positionBatalha = pyautogui.locateOnScreen('images/batalha/batalhaCheia.png', grayscale=True, confidence=0.7)
            print("comparando se existe pokemons")
                
            
        print("Não há mais pokemons")
        positionDeadDMagikarp = pyautogui.locateOnScreen('pokemon.png', grayscale=True, confidence=0.7)
        time.sleep(0.5)
        while(positionDeadDMagikarp != None):
            if (positionDeadDMagikarp != None):
                positionSuperball = pyautogui.locateOnScreen('images/ball/ultra.png',confidence=0.7)
                time.sleep(1)
                if(positionSuperball != None):
                    positionCenterSuperball = pyautogui.center(positionSuperball)
                    positionCenterDeadMagikarp = pyautogui.center(positionDeadDMagikarp)
                    time.sleep(0.5)
                    pyautogui.click(positionCenterSuperball.x,positionCenterSuperball.y,button='right')
                    time.sleep(1)
                    pyautogui.click(positionCenterDeadMagikarp.x,positionCenterDeadMagikarp.y)
                    time.sleep(3)
            positionDeadDMagikarp = pyautogui.locateOnScreen('pokemon.png', grayscale=True, confidence=0.7)
        print('Estou capturando')

def functionPositionVara(positionVara):
    positionVara = pyautogui.locateOnScreen('vara.png')
    return positionVara

def functionRepetirJogarVara():
    #CAPTURA POSIÇÃO VARA
    while (positionVara == None):
        positionVara = pyautogui.locateOnScreen('vara.png', grayscale=True,confidence=0.8)
    positionCenterVara = pyautogui.center(positionVara)
    pyautogui.click(positionCenterVara.x,positionCenterVara.y)
    pyautogui.moveTo((positionCenterVara.x),(positionCenterVara.y+20))
    print('Vara')
    time.sleep(2)
    #CAPTURA POSIÇÃO AGUA
    while (positionAgua == None):
        positionAgua = pyautogui.locateOnScreen('agua.png', grayscale=True,confidence=0.8)
    positionCenterAgua = pyautogui.center(positionAgua)
    pyautogui.click(positionCenterAgua.x,positionCenterAgua.y)
    pyautogui.moveTo((positionCenterAgua.x),(positionCenterAgua.y+20))
    print('Agua')

functionMain()