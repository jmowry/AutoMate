#AutoMate:  Game automation for repetitive tasks.
#Author:    Joseph Mowry

import pyautogui
import pyautogui.tweens
import time

screenWidth, screenHeight = pyautogui.size()
currentMouseX, currentMouseY = pyautogui.position()
pyautogui.moveTo(100, 150)
pyautogui.click()
pyautogui.moveRel(None, 10)  # move mouse 10 pixels down
time.sleep(2)
pyautogui.doubleClick()

# This line throws an error due to not recognizing "tweens" member.
# Please see: https://pyautogui.readthedocs.io/en/latest/introduction.html for this example.
pyautogui.moveTo(500, 500, duration=2, tween=pyautogui.tweens.easeInOutQuad)  # use tweening/easing function to move mouse over 2 seconds.

pyautogui.typewrite('Hello world!', interval=0.25)  # type with quarter-second pause in between each key
pyautogui.press('esc')
pyautogui.keyDown('shift')
pyautogui.press(['left', 'left', 'left', 'left', 'left', 'left'])
pyautogui.keyUp('shift')
pyautogui.hotkey('ctrl', 'c')
