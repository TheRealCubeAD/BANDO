""" 
Python program to automatically join the online zoom classes 
based on the given input in the Excel sheet List.xlsx
the input should be in the given format

Time : dd-mm-yyyy hh:mm AM/PM
Meeting ID : 123456123 (string)
Meeting Password : 1234 (string)

IMP - If you want to change the program path jump to line 40

Disclaimer:
I am not responsible for any troubles caused to you
if the program does not function as intended, or if it is misused,
please make sure to test it before executing

Modules used:

pyautogui - https://pyautogui.readthedocs.io/en/latest/
openpyxl - https://openpyxl.readthedocs.io/en/stable/
PIL - https://pillow.readthedocs.io/en/stable/
"""





import  datetime, time, subprocess, csv, os, webbrowser

try:
    import pyautogui
    from PIL import Image
except ModuleNotFoundError as err:
    print("not installed modules please go through the read me files, press anything to exit")
    input()
#enabling mouse fail safe
pyautogui.FAILSAFE = True


#function to manualy join if no link is provided
def manualjoin(id, password = ""):
    subfolders = [f.path for f in os.scandir("C:\\Users") if f.is_dir()]
    # opening the zoom app, if you are running on a different OS or the path is different
    # change the path here
    for i in subfolders:
        if os.path.isfile(i + "\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe"):
            subprocess.Popen(i + "\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe")
            break
    
    time.sleep(3)
    cur = time.time()
    #locating the zoom app
    print("Locating Zoom")
    while True:
        var = pyautogui.locateOnScreen('final.png')
        if var != None:
            print("Done")
            print("Joining meeting...")
            pyautogui.click(var)
            break
        elif (time.time() - cur) >= 120:
            print("App Not opened")
            break
        print("Not found...")
        #check every 30 secs
        time.sleep(2)

    time.sleep(2)

    #entering the meeting id
    print("Writing id...")
    print(id)
    pyautogui.typewrite(str(id))
    print("Done")

    #disabling video source
    print("Locating Video_off")
    var = pyautogui.locateOnScreen('videooff.png')
    print("Done")
    print("Muting Video...")
    pyautogui.click(var)
    print("Done")

    #clicking the join button
    print("Locating Join_button")
    var = pyautogui.locateOnScreen('join.png')
    print("Done")
    print("Joining")
    pyautogui.click(var)
    print("Done")

    time.sleep(3)

    #checking and entering if meeting password is enabled
    print("Locating Password_field")
    print("Done")
    print("Writing password")
    print(password)
    pyautogui.typewrite(password)
    print("Done")
    print("Locating Join_button")
    var = pyautogui.locateOnScreen('joinmeeting.png')
    print("Done")
    pyautogui.click(var)
    print("You are joining the meeting...")
    print()
    return



def linkjoin(link):
    #open the given link in web browser
    print("Opening link...")
    webbrowser.open(link)
    print("Done")
    start = time.time()
    time.sleep(3)
    if "zoom" not in link:
        return
    while True:
        print("Locating openlink...")
        var = pyautogui.locateOnScreen('openlink.png')
        if var != None:
            print("Done")
            pyautogui.click(var)
            break
        var = pyautogui.locateOnScreen('openzoom.png')
        if var != None:
            print("Done")
            pyautogui.click(var)
            break
        elif (time.time() - start) >= 60:
            print("link " + link + " not opened")
            return
        break
        time.sleep(1)
    print("You are joining the meeting...")
    return


