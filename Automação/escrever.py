import pyautogui # Biblioteca para usar os comandos
import pyperclip
import time # Biblioteca que mexe com o tempo em geral

pyautogui.FAILSAFE = True

pyautogui.PAUSE = 1

pyautogui.press('win')

pyautogui.keyDown('backspace')

time.sleep(1)

pyautogui.keyUp('backspace')

pyautogui.write('office', interval=0.3)

pyautogui.press('enter')

time.sleep(3)

position = pyautogui.locateCenterOnScreen('Automação/1.jpg', confidence= 0.8)

pyautogui.moveTo(position, duration=1.5)

pyautogui.doubleClick()

time.sleep(0.5)

text = 'Olá, eu sou o programador Emanuel e está é a minha primeira automação'
pyperclip.copy(text)
pyautogui.hotkey('ctrl' or 'command', 'V')
pyautogui.press('enter')