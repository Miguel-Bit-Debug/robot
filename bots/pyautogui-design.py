import pyautogui

distance = 200

pyautogui.FAILSAFE = False # Não recomendado

while distance > 0:
    pyautogui.drag(distance, 0, duration=0.5)
    distance -= 25
    pyautogui.drag(0, distance, duration=0.5)
    pyautogui.drag(0, distance, duration=0.5)

    distance -= 25
    pyautogui.drag(0, distance, duration=0.5)
