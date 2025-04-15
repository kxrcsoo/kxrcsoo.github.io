import webbrowser
import pyautogui
import time

url = 'https://kxrcsoo.github.io/'
webbrowser.open(url)

time.sleep(0.5)

screenWidth, screenHeight = pyautogui.size()

centerX, centerY = screenWidth // 2, screenHeight // 2

pyautogui.click(centerX, centerY)

pyautogui.press('o')
time.sleep(0.1)
pyautogui.press('f11')
