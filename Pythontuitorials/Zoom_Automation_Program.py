import subprocess
import pyautogui
import time
from datetime import datetime


def sign_in(meetingid, pswd):
      while True:
            if datetime.now().hour == 3 and datetime.now().minute == 29:

                  # open zoom app
                  subprocess.call(r'C:\Users\Deshmukh\AppData\Roaming\Zoom\bin\Zoom.exe')

                  time.sleep(3)

                  # clicks join button
                  join_btn = pyautogui.locateCenterOnScreen(r'C:\Users\Deshmukh\Desktop\misc\C++\.vscode\Pythontuitorials\join_button.png',confidence=.7)
                  pyautogui.moveTo(join_btn)
                  pyautogui.click()

                  time.sleep(2)

                  # types meeting id
                 # meeting_id_btn = pyautogui.locateCenterOnScreen(r'C:\Users\Deshmukh\Desktop\misc\C++\.vscode\Pythontuitorials\meeting_id_button.png',confidence=.5)
                 # pyautogui.moveTo(meeting_id_btn)
                 # pyautogui.click()
                  pyautogui.write(meetingid)

                  # checks boxes
                  media_btn = pyautogui.locateAllOnScreen(r'C:\Users\Deshmukh\Desktop\misc\C++\.vscode\Pythontuitorials\media_btn.png')
                  for btn in media_btn:
                       pyautogui.moveTo(btn)
                       pyautogui.click()
                       time.sleep(2)

                  
                 # Hits the join button
                  join_btn = pyautogui.locateCenterOnScreen(r'C:\Users\Deshmukh\Desktop\misc\C++\.vscode\Pythontuitorials\join_btn.png', confidence=.7)
                  pyautogui.moveTo(join_btn)
                  pyautogui.click()
                 
                  time.sleep(7)

                  # Types the password and hits enter
                  meeting_pswd_btn = pyautogui.locateCenterOnScreen(r'C:\Users\Deshmukh\Desktop\misc\C++\.vscode\Pythontuitorials\meeting_pswd.png')
                  pyautogui.moveTo(meeting_pswd_btn)
                  pyautogui.click()
                  pyautogui.write(pswd)
                  pyautogui.press('enter')

                  break

sign_in('777 501 9057', '5Ha1RS')