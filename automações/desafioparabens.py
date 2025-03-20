import pyautogui
import time
import os

# Abre o Microsoft Word
os.system("start winword")
time.sleep(5)  # Aguarda o Word abrir completamente

# Escreve "Parabéns Manu" no novo documento
pyautogui.typewrite("Parabens Manu")
pyautogui.typewrite("\nParabens")
pyautogui.press("enter")