###############          ##########        #######   #######        #########      #######       #
#              #        #          #             #         #       #         #           #
#               #       #          #            #         #        #         #          #        #
#              #        #          #           #         #         #         #         #         #
###############         ############          #         #          ###########        #          #
#              #        #          #         #         #           #         #       #           #
#               #       #          #        #         #            #         #      #            #
#              #        #          #       #         #             #         #     #             #
###############         #          #      #######    #######       #         #    #######        #

# Developer: Mohammad Ali Bazzazi (me)

########################### START ###########################
# Importing Libraries
import pyautogui, pyperclip, time

# Wait for 5 sec
time.sleep(5)

# Read Persian spam file
with open('spam-fa.txt', 'r', encoding='utf8') as f:
    lines = f.readlines()


for line in lines:
    
    # Copy line
    pyperclip.copy(line)

    # Paste line
    pyautogui.hotkey('ctrl','v')
    
    # Press Enter
    pyautogui.press('enter')
########################### END ###########################
    
