import pyautogui
import keyboard
import time
import datetime


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

        salvaLog()
        #CAPTURA POSIÇÃO Habilidades
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
            print("coletando espólios de batalha")
            keyboard.press('e')
            print("comparando se existe pokemons")
                
            
        print("Não há mais pokemons")
        positionDeadPokemon = pyautogui.locateOnScreen('images/deadPokemon/shinyGrantMagikarp.png', grayscale=True, confidence=0.7)
        positionDeadPokemon2 = pyautogui.locateOnScreen('images/deadPokemon/shinyMagikarp2.png', grayscale=True, confidence=0.7)
        time.sleep(0.5)
        while(positionDeadPokemon != None or positionDeadPokemon2 != None):
            if (positionDeadPokemon != None or positionDeadPokemon2 != None):
                positionBall = pyautogui.locateOnScreen('images/ball/ultra.png',confidence=0.7)
                time.sleep(1)
                if(positionBall != None):
                    if(positionCenterDeadPokemon != None):
                        positionCenterball = pyautogui.center(positionBall)
                        positionCenterDeadPokemon = pyautogui.center(positionDeadPokemon)
                        time.sleep(0.5)
                        pyautogui.click(positionCenterball.x,positionCenterball.y-5,button='right')
                        time.sleep(1)
                        pyautogui.click(positionCenterDeadPokemon.x,positionCenterDeadPokemon.y)
                        time.sleep(3)
                    else:
                        if(positionDeadPokemon2 != None):
                            positionCenterball = pyautogui.center(positionBall)
                            positionCenterDeadPokemon2 = pyautogui.center(positionDeadPokemon2)
                            time.sleep(0.5)
                            pyautogui.click(positionCenterball.x,positionCenterball.y-5,button='right')
                            time.sleep(1)
                            pyautogui.click(positionCenterDeadPokemon2.x,positionCenterDeadPokemon2.y)
                            time.sleep(3)
            positionDeadPokemon = pyautogui.locateOnScreen('images/deadPokemon/shinyGrantMagikarp.png', grayscale=True, confidence=0.7)
            positionDeadPokemon2 = pyautogui.locateOnScreen('images/deadPokemon/shinyMagikarp2.png', grayscale=True, confidence=0.7)
            print('Estou capturando')

        time.sleep(1)
        functionAlimentarPoke()
        

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

def functionAlimentarPoke():
    pizza = pyautogui.locateOnScreen('caverna/pizza.png', grayscale=True,confidence=0.8)
    if(pizza):    
        pizzaCenter = pyautogui.center(pizza)
        pyautogui.click(pizzaCenter.x,pizzaCenter.y,button='right')
        poke = pyautogui.locateOnScreen('caverna/poke.png', grayscale=True,confidence=0.8)
        pokeCenter = pyautogui.center(poke)
        pyautogui.click(pokeCenter.x,pokeCenter.y)
        print("entrei e me alimentei")

def salvaLog():
    dateTimeNow = datetime.datetime.now()
    StringDateTimeNow = str(dateTimeNow)
    StringDateTimeNowReplaces = StringDateTimeNow.replace(":", "-")
    scBatalhaLog = pyautogui.screenshot()
    nomeImagem = 'images/logBatalha/' + StringDateTimeNowReplaces + '.png'
    scBatalhaLog.save(nomeImagem)
    print("salvei log de batalha")

functionMain()