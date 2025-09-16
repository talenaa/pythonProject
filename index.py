import pyautogui
import time

pyautogui.PAUSE = 2

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

time.sleep(3)

pyautogui.click(x=910, y=370)

pyautogui.write("talenabarbosa7@gmail.com")