# Automatize a criação de um relatório diário abrindo o Bloco de Notas, escrevendo um resumo automatizado com a data de hoje e salvando o arquivo na área de trabalho
\
import os
import time
import pyautogui
from datetime import datetime

day = datetime.now().strftime('%dD-%mM')
hoje = datetime.now().strftime('%d/%m/%Y')
area_de_trabalho = os.path.join(os.path.expanduser('~'), 'Desktop')

pyautogui.PAUSE = 1

pyautogui.hotkey('win')

pyautogui.keyDown('backspace')

time.sleep(3)

pyautogui.keyUp('backspace')

pyautogui.write('Bloco de notas')

pyautogui.press('enter')

time.sleep(3)

pyautogui.write(f'Relatorio Diario de {day}')
pyautogui.write(f'Em {hoje}')
pyautogui.hotkey('ctrl', 'S')

time.sleep(2)

caminho = os.path.join(area_de_trabalho, f"Relatorio_de_{day}")

pyautogui.write(caminho)
pyautogui.hotkey('enter')

time.sleep(2)

pyautogui.hotkey('alt', 'f4')