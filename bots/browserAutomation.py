import pyautogui
import time

pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True

pyautogui.hotkey('win', 'r')
pyautogui.typewrite('https://gabrielcasemiro.com.br/atividade_pyautogui \n')
pyautogui.press('enter')

time.sleep(3)

with open('membros.csv') as file:
    next(file)

    for line in file:
        line = line.strip()
        line = line.split(';')

        print(f'Dados: {line}')

        name = line[0]
        sexo = line[1]
        email = line[2]
        phone = line[3]

        