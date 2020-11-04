"""
Comlud
2020-11-04

$$$$$$$\  $$$$$$$$\ $$$$$$$$\ $$\   $$\ $$$$$$$$\  $$$$$$\  $$$$$$$\  
$$  __$$\ $$  _____|\____$$  |$$ | $$  |\__$$  __|$$  __$$\ $$  __$$\ 
$$ |  $$ |$$ |          $$  / $$ |$$  /    $$ |   $$ /  $$ |$$ |  $$ |
$$ |  $$ |$$$$$\       $$  /  $$$$$  /     $$ |   $$ |  $$ |$$$$$$$  |
$$ |  $$ |$$  __|     $$  /   $$  $$<      $$ |   $$ |  $$ |$$  ____/ 
$$ |  $$ |$$ |       $$  /    $$ |\$$\     $$ |   $$ |  $$ |$$ |      
$$$$$$$  |$$$$$$$$\ $$$$$$$$\ $$ | \$$\    $$ |    $$$$$$  |$$ |      
\_______/ \________|\________|\__|  \__|   \__|    \______/ \__| - mother fuckerz
"""

import PIL     # PIL.ImageGrab.grab()
import ctypes  # ctypes.windll.user32.SystemParametersInfoW()
import pathlib # pathlib.Path().absolute()
import time    # time.sleep()

def GetScreenshot(box):
    return PIL.ImageGrab.grab(box)

def GetAbsolutePath():
    return str(pathlib.Path().absolute())

def SetDesktopBackground(imageName):
    ctypes.windll.user32.SystemParametersInfoW(20, 0, GetAbsolutePath() + '/' + imageName, 0)

imageName = "screenshot.png"

screenWidth = 1920  # You may need to tweak this.
screenHeight = 1080 # You may need to tweak this.

for i in range(5):
    print("Starting in " + str(5 - i) + " seconds!")
    time.sleep(1)

print("LET'S GO! (Press CTRL + C to stop)")

while True:
    print('.')
    GetScreenshot((-1, -1, screenWidth + 1, screenHeight + 1)).save(imageName)
    SetDesktopBackground(imageName)
    time.sleep(.5) # Increase this if the script terminates prematurely.