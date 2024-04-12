# Imports required for this program to function
import pyautogui as pg
from pynput.keyboard import Key, Controller as kb
from pynput.mouse import Button, Controller as ms
import os

# Define mouse button constants
l = Button.left
r = Button.right
m = Button.middle

# Create keyboard and mouse controller objects
keyboard = kb()
mouse = ms()

# Get the directory path of the script
dir_path = os.path.dirname(os.path.abspath(__file__))

# Function to press enter
def enter():
    pressrelease(Key.enter)

# Function to type text using pyautogui (may be less reliable on some applications)
def write(phrases):
    pg.write(phrases)

# Function to press and release a keyboard key
def pressrelease(key):
    keyboard.press(key)
    keyboard.release(key)

# Function to locate an image on the screen and move the mouse to its center
def locate(name, confidence):
    try:
        locateimage = pg.locateOnScreen(f"{dir_path}/images/{name}.png", confidence=confidence)
        located = pg.center(locateimage)
        pg.moveTo(located)
    except:
        locate(name, confidence)

# Function to click the mouse button a specified number of times (with error handling)
def click(button, amount=1):
    canclickbutton = True
    while canclickbutton == True:
        "Clicks the mouse button a specified number of times"
        if not isinstance(amount, int):
            print("Invalid click amount specified. Using 1 click instead.")
            amount = 1
        mouse.click(button, amount)
        canclickbutton = False

# Press the command key (might be different on some systems)
pressrelease(Key.cmd)

# Use pyautogui to locate an image named "checkfortaskbar" and write "Ubuntu"
locate("checkfortaskbar", .8)
write("Ubuntu")
# Use locate to find "checkforlinuxapp" and press enter
locate("checkforlinuxapp", .8)
enter()

# Similar steps to locate "checkfortaskbar", click it, write "cd privateGPT", etc.
locate("checkforlinuxsys", .8)
click(l)
write("cd privateGPT")
locate("cdprivateGPTtyped", .8)
enter()

# Similar steps to locate "checkforlinuxsys", click it, write "cd privateGPT", etc.
locate("privateGPTcd", .8)
write("make run")
locate("checkformakeruncmd", .8)
enter()