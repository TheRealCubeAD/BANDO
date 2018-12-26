import os
import time
import shutil
import tkinter
from tkinter import scrolledtext
from PIL import Image

def searchdirs():
    dirs = [fpq,fps]
    try:
        for path in dirs:
            if os.path.isdir(path):
                print(path,"gefunden")
            else:
                print(path,"nicht gefunden!")
                raise IndexError
    except IndexError:
        input("Bitte Problem beheben und erneut versuchen >>")
        searchdirs()
    print("Alle Ordner gefunden")
    

def allFilesFromQuax():
    f = os.listdir(fpq)
    for element in f:
        print(element,"gefunden")
    return f


def getDates():
    allDates = []
    Dates = []
    for element in files:
        currd = time.gmtime(os.path.getmtime(fpq+"/"+element))[:3]
        currd = list(currd[::-1])
        for inti in range(3):
            currd[inti] = str(currd[inti])
        if len(currd[0]) < 2:
            currd[0] = "0"+currd[0]
        if len(currd[1]) < 2:
            currd[1] = "0"+currd[1]
        currd[2] = currd[2][2:]
        print(element,currd)
        Dates.append(currd)
        if allDates.count(currd) == 0:
            allDates.append(currd)
    print()
    print(allDates)
    return allDates,Dates

def getDFoldersFromSave():
    allFolders = []
    for folder in os.listdir(fps):
        print(folder)
        allFolders.append(folder.split("."))
    return allFolders
        
def getMerge(a,b):
    res = []
    for element in a:
        if element not in b and element not in res:
            res.append(element)
        else:
            print(element,"vorhanden")
    print(res,"fehlt")
    return res

def newDirs(merge):
    for element in merge:
        print(element)
        date = element[0] + "." + element[1] + "." + element[2]
        os.mkdir(fps+"/"+date)
        os.mkdir(fps+"/"+date+"/Images")
        os.mkdir(fps+"/"+date+"/Videos")
        print("Ordner",element,"erstellt")
    print("alle Ordner erstellt")
    print()

def copy():
    for i in range(len(files)):
        mod = (files[i].split("."))[-1]
        if mod == "jpg" or mod == "DNG" or mod == "JPG":
            mod = "Images"
        else:
            mod = "Videos"
        Date = aDates[i][0]+"."+aDates[i][1]+"."+aDates[i][2]
        path = fps+"/"+Date+"/"+mod+"/"+files[i]
        if not os.path.isfile(path):
            shutil.copy2(fpq+"/"+files[i],path)
            print(files[i],"nach",path,"verschoben")
        else:
            print(files[i],"existiert bereits")
        
def delete():
    for i in files:
        os.remove(fpq+"/"+i)
        print(i,"gelöscht")

def loadConfig():
    global fps
    Tags = []
    try:
        config = open("SETUP.config","r")
        dirr, path = config.readline().split(":")
        yield dirr == "fps"
        if path != "NONE":
            fps = path
            config.close()
        else:
            config.close()
            with open("SETUP.config","w") as config:
                config[0] = "fps:" + chooseDir()
            loadConfig()
    except:
        if(quest("Die SETUP.config Datei ist beschädigt oder nicht vorhanden. "
              "Bei einer Wiederherstellung gehen alle Einstellungen verloren. Wiederherstellen?")):
            try:
                os.remove("SETUP.config")
            except FileNotFoundError:
                pass
            with open("SETUP.config","w+") as new_config:
                new_config.write("fps:NONE")
            exit("RESTART")
        else:
            exit("SETUP corrupted")

def initWindow():
    global window
    global droneImageObjekt
    window = tkinter.Tk()
    window.title("Quax Manager V2.0")
    window.configure(bg="#ffffff")

    area_connect = tkinter.Frame(window)
    area_connect.grid(column=0)

    area_connect_drone = tkinter.Frame(area_connect)
    area_connect_location = tkinter.Frame(area_connect)
    area_connect_drone.grid(row=0)
    area_connect_location.grid(row=1)

    area_operation = tkinter.Frame(window)
    area_operation.grid(column=1)

    area_operation_copy = tkinter.Frame(area_operation)
    area_operation_info = tkinter.Frame(area_operation)
    area_operation_select = tkinter.Frame(area_operation)
    area_operation_copy.grid(row=0)
    area_operation_info.grid(row=1)
    area_operation_select.grid(row=2)

    droneImageObjekt = tkinter.PhotoImage(file="HLXS3.pgm")
    droneImage = tkinter.Label(area_connect_drone,image=droneImageObjekt)
    droneImage.grid(column=0)

    info = tkinter.Label(area_operation_info,text="INFO",bg="#ffffff")
    info.grid()


    
fpq = ":/DCIM/100MEDIA"
fps = ""
window = None
droneImageObjekt = None
initWindow()
window.mainloop()
loadConfig()

files = allfiles()
print()
Dates, aDates = getDates()
newDirs(getMerge(Dates,getDFolders()))
print("Starte Kopiervorgang...")
copy()
print()
print("Alle Dateien kopiert")
time.sleep(1)
print()
if input("Dateien von Drohne löschen?") == "j":
    delete()
    print()
    print("Alle Dateien gelöscht")
time.sleep(4)


