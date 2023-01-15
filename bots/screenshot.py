import pyautogui
import time

while True:
    pyautogui.screenshot(f"print_{time.time()}.png")
    time.sleep(2)

