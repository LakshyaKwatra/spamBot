import pyautogui, time, keyboard, sys

#Constants
INITIAL_WAIT = 5
CLIENT_WAIT = 5
STEP_WAIT = 2
TYPEWRITE_DELAY = 0.03
GREETING_TEXT = "F 18"
EXIT_MESSAGE = "Goodbye!"
EXIT_KEY = 'shift'
NEW_CHAT_KEY = 'esc'
SEND_KEY = 'enter'


def omegleStep():
    pyautogui.press(SEND_KEY)
    time.sleep(CLIENT_WAIT)
    pyautogui.press(NEW_CHAT_KEY)
    
def run():
    time.sleep(INITIAL_WAIT)
    while(True):
        f = open("script.txt",'r')
        for line in f:
            time.sleep(CLIENT_WAIT)
            for char in line:
                pyautogui.typewrite(char,TYPEWRITE_DELAY)
                if keyboard.is_pressed(EXIT_KEY):
                    print(EXIT_MESSAGE)
                    return
            omegleStep()
        pyautogui.press(NEW_CHAT_KEY)

run()
