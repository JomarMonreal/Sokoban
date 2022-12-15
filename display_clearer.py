import os
import platform

#clears the terminal
def clear():
    if platform.system() == "Linux":  os.system('clear')
    else: os.system('cls')