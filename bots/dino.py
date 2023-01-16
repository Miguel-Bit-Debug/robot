from PIL import ImageGrab
import pyautogui

while True:
    image = ImageGrab.grab().convert("L")
    data = image.load()

    for i in range(780, 840):
        for j in range(290, 330):
            data[i, j] = 0

    image.show()
    break