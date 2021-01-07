#Using camelCase for variables, underscore for functions
import subprocess as sub
#enables access to applications
import pyautogui as pag
#automates mouse movement and typing
import time
import pandas as pd
from datetime import datetime

def join_room():
    #clicks the join button
    joinRoom = pag.locateCenterOnScreen('join_room_button.png')
    pag.moveTo(joinRoom)
    pag.click()

def enter_id():
    # Type the meeting ID
    meeting_id =  pag.locateCenterOnScreen('meeting_id_button.png')
    pag.moveTo(meeting_id)
    pag.click()
    pag.write(meetingid)

def disable_media():
    # Disables both the camera and the mic
    mediaButton = pag.locateAllOnScreen('media_btn.png')
    for button in mediaButton:
        pag.moveTo(button)
        pag.click()
        time.sleep(1)

def join_meet():
    # Hits the join button
    joinMeet = pag.locateCenterOnScreen('join_meet_button.png')
    pag.moveTo(joinMeet)
    pag.click()
    time.sleep(5)
    #Sleeping the programme to account for the application delay in between steps

def enter_pswd():
    #Types the password and hits enter
    meeting_pass = pyautogui.locateCenterOnScreen('meeting_pswd.png')
    pyautogui.moveTo(meeting_pass)
    pyautogui.click()
    pyautogui.write(password)
    pyautogui.press('enter')

def sign_in(meetingid, password):
    #you can't use 'pass' as an input parameter, use password or pswd instead
    sub.call(["/usr/bin/open", "/Downloads/zoom.us.app"])
    #Simply launches the zoom app, change the path accourdingly.

    join_room()
    enter_id()
    disable_media()
    join_meet()
    enter_pswd()

if __name__ == '__main__':
# Reading the CSV file of meetings to bunk ;)
dataframe = pd.read_csv('meetingsList.csv')

while True:
    # checking of the current time exists in our csv file
    now = datetime.now().strftime("%H:%M")
    if now in str(dataframe['timings']):
       # This looks for a matching instance of 'now' in the timings column of the db
       details = dataframe.loc[dataframe['timings'] == now]
       ID = str(details.iloc[0,1])
       PASSWORD = str(details.iloc[0,2])
       #details can be a 2x2 matrix, iloc[y,x] finds the entry corresponding to the y'th row, x'th column
       sign_in(ID, PASSWORD)
       print("you're in")

#Honestly, such programmes show that coding isn't some witchcraft but just needs to be done mindfully.
#Computers strictly follow the given instructions, when you know exactly what you want to do, code can be a powerful tool to turn your idea into a reality.
