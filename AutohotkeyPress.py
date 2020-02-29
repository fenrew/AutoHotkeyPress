#! python3

import pyautogui
import keyboard
import threading

keyToPress = None
intervalToPress = None


while keyToPress == None:
    print("What key do you want to auto press?")
    keyToPress = input()
    if len(keyToPress) != 1:
        keyToPress = None
        print("You can only auto press ONE key")
        continue
    else:
        print("You chose the key: " + keyToPress)


while intervalToPress == None:
    print("How long interval (seconds) should it be between each key press?")
    intervalToPress = input()
    try:
        intervalToPress = float(intervalToPress)
        if intervalToPress < 0.5:
            print("The number is too small")
            intervalToPress = None
            continue
    except ValueError:
        print("That's not a number")
        intervalToPress = None
        continue
    

def keypressFunction(keyToPress):
    pyautogui.typewrite(keyToPress)

def startTimer(keyToPress, stop):
    if stop == False:
        print("The loop has been stoped")
    else:
        timer = threading.Timer(intervalToPress, startTimer, [keyToPress, True]).start()
        keypressFunction(keyToPress)


startTimer(keyToPress, True)

stopTimerLoop = False
while not stopTimerLoop:
    if keyboard.is_pressed("q"):
        startTimer(keyToPress, False)
        stopTimerLoop = True
        break
    else:
        pass
