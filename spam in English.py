# Importing Libraries
import pyautogui, time

# Wait for 5 sec
time.sleep(5)

# Read Persian spam file
with open('spam-en.txt', 'r') as f:
    lines = f.readlines()

for line in lines:

    # Type line
    pyautogui.typewrite(line.strip())
    
    # Press Enter
    pyautogui.press('enter')