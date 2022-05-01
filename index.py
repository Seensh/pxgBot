import pyautogui
import keyboard
import time


def functionMain():   

    while keyboard.is_pressed('c') == False:
        positionVara = None
        positionAgua = None
        positionAguaBorbulhando = None
        positionNameMagi = None
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
        #CAPTURA POSIÇÃO AGUA BORBULHANDO
        while (positionAguaBorbulhando == None):
            positionAguaBorbulhando = pyautogui.locateOnScreen('aguaBorbulhando.png', grayscale=True,confidence=0.8)
        pyautogui.click(positionCenterVara.x,positionCenterVara.y)
        pyautogui.moveTo((positionCenterVara.x),(positionCenterVara.y+20))
        print('Agua Borbulhando')
        time.sleep(2)

        #CAPTURA POSIÇÃO Magikarp

        while (positionNameMagi == None):      
            positionNameMagi = pyautogui.locateOnScreen('nameMagi.png', grayscale=True,confidence=0.8)
            count = count + 1
            if(count > 5):
                positionNameMagi = None
        if(positionNameMagi != None):
            positionCenterNameMagi = pyautogui.center(positionNameMagi)
            #pyautogui.click(positionCenterNameMagi.x,positionCenterNameMagi.y)
            print('Magikarp')
        time.sleep(2)

        #CAPTURA POSIÇÃO Hanilidades
        positionHabilidades = pyautogui.locateOnScreen('habilidades.png', grayscale=True)
        while(positionNameMagi != None):
            if(positionHabilidades != None):
                positionCenterHabilidades = pyautogui.center(positionHabilidades)
                time.sleep(1)
                pyautogui.click((positionCenterHabilidades.x + 40),positionCenterHabilidades.y)
                time.sleep(2)
                pyautogui.click((positionCenterHabilidades.x + 80),positionCenterHabilidades.y)
                time.sleep(2)
                pyautogui.click((positionCenterHabilidades.x + 120),positionCenterHabilidades.y)
                time.sleep(1)                
            positionNameMagi = pyautogui.locateOnScreen('nameMagi.png', grayscale=True,confidence=0.8)

            print('Habilidades')

def functionPositionVara(positionVara):
    positionVara = pyautogui.locateOnScreen('vara.png')
    return positionVara


functionMain()