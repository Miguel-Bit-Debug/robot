import pyautogui
import time

pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True

pyautogui.hotkey('win', 'r')
pyautogui.typewrite('https://gabrielcasemiro.com.br/atividade_pyautogui \n')
pyautogui.press('enter')

time.sleep(3)

