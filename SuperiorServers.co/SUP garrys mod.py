import subprocess
import time
import os
import pyautogui
import keyboard
os.system("taskkill /im Steam.exe /f")
while True:
    os.system("taskkill /F /IM hl2.exe")
    os.system("taskkill /im Steam.exe /f")
    time.sleep(3)

    # Open Steam
    steam_path = r"C:\Program Files (x86)\Steam\Steam.exe"
    subprocess.Popen([steam_path])

    
    time.sleep(60)


    # Launch Garry's Mod
    gmod_path = r"C:\Program Files (x86)\Steam\Steam.exe"
    subprocess.Popen([gmod_path, "-applaunch", "4000"])
    time.sleep(60)


    # Connect to RP.SuperiorServers.co using the in-game console
    pyautogui.press('`')  # Open the console

    # Wait for the console to open (adjust the sleep duration if needed)
    time.sleep(5)

    # Type the connection command and press Enter
    pyautogui.typewrite('connect rp.SuperiorServers.co')
    pyautogui.press('enter')

    # Wait for 1 minute (adjust the sleep duration if needed)
    time.sleep(160)


    
    #close
    time.sleep(6)
    click222_x = 512  
    click222_y = 618
    pyautogui.click(click222_x, click222_y)
    time.sleep(6)
    pyautogui.click()

    time.sleep(2)

    #f4
    keyboard.press_and_release('F4')

    #actions
    time.sleep(6)
    click2_x = 200  
    click2_y = 161
    pyautogui.click(click2_x, click2_y)
    time.sleep(6)
    pyautogui.click()

    #org
    time.sleep(6)
    click3_x = 206  
    click3_y = 430
    pyautogui.click(click3_x, click3_y)
    time.sleep(6)
    pyautogui.click()
    
    #bank
    time.sleep(6)
    click4_x = 774  
    click4_y = 158
    pyautogui.click(click4_x, click4_y)
    time.sleep(6)
    pyautogui.click()

    

    #click money
    time.sleep(6)
    click6_x = 751  
    click6_y = 264
    pyautogui.click(click6_x, click6_y)
    time.sleep(6)
    pyautogui.click()

    #type money
    keyboard.press_and_release('backspace')
    time.sleep(6)
    keyboard.write('1')
    keyboard.write('0')
    keyboard.write('0')
    keyboard.write('0')
    keyboard.write('0')
    
    #deposit money
    time.sleep(5)
    click7_x = 818  
    click7_y = 282
    pyautogui.click(click7_x, click7_y)
    time.sleep(6)
    pyautogui.click()

    #click money
    time.sleep(6)
    click6_x = 809  
    click6_y = 352
    pyautogui.click(click6_x, click6_y)
    time.sleep(6)
    pyautogui.click()
    time.sleep(2)
    #delete
    keyboard.press_and_release('backspace')
    keyboard.press_and_release('backspace')
    keyboard.press_and_release('backspace')
    keyboard.press_and_release('backspace')
    keyboard.press_and_release('backspace')
    keyboard.press_and_release('backspace')
    keyboard.write('1234')

    #deposit money
    time.sleep(6)
    click8_x = 812  
    click8_y = 322
    pyautogui.click(click8_x, click8_y)
    time.sleep(6)
    pyautogui.click()

  #deposit money
    time.sleep(6)
    click9_x = 897  
    click9_y = 118
    pyautogui.click(click9_x, click9_y)
    time.sleep(6)
    pyautogui.click()
    
    time.sleep(7200)

    
