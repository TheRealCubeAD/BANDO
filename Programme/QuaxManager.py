import os
import time
import shutil

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
    

def allfiles():
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

def getDFolders():
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
        
fpq = "G:/DCIM/100MEDIA"
fps = "E:/QUAX/Days"
print("--------QuaxManager--------")
print("           V1.2")
print("         16.03.2018")
print("---------------------------")
print()
searchdirs()
print()
input("Bereit >>")
print()
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


