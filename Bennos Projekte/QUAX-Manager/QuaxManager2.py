import os
import string
import time
import shutil
import datetime
import tkinter


gui = False


#Im Programm verwendete Ausgabemethode. Entscheidet ob der Text ausgegeben oder an das Gui weitergegeben wird
def out(content):
    if gui:
        pass  #Noch nicht implementiert
    else:
        print(content)


#Im Programm verwendete Eingabemethode. Entscheidet ob die Eingabe aus der Konsole oder aus dem Gui ausgelesen wird
def inp(out_content):
    if gui:
        if out_content:
            out(out_content)
        pass
    else:
        cont = input(out_content)
    return cont



#Klasse HDD: übernimmt die Steuerung für den geordneten Speicherort
class HDD:
    path = None   #Speicherort der Tages-Ordner
    folders = []  #Namen der Tages-Ordner ["19.02.01,...] (yy,mm,dd)

    def init(self):
        if not self.searchHDD():
            return False
        return True

    #Durchsucht alle verfügbaren Laufwerke nach der IDENT.HDD.txt Datei
    # und liest aus dieser den relativen Speicherort aus
    def searchHDD(self):
        available_drives = ['%s:' % d for d in string.ascii_uppercase if os.path.exists('%s:' % d)]
        for drive in available_drives:
            if os.path.exists(drive+"/IDENT.HDD.txt"):
                HDD_config = open(drive+"/IDENT.HDD.txt")
                relativ_path = HDD_config.readline()
                self.path = drive+relativ_path
                HDD_config.close()
                return True
        return False

    #Speichert alle bereits existierenden (Tages-)Ordner in folders
    # ["19.02.01",...]
    def loadFolders(self):
        self.folders = [folder.split(".") for folder in os.listdir(self.path)]

    #Erstellt für ein gegebenes Datum einen neuen Ordner sowie die Unterordner Images und Videos
    def createFolder(self,date):
        os.mkdir(self.path+"/"+date)
        os.mkdir(self.path+"/"+date+"/Images")
        os.mkdir(self.path+"/"+date+"/Videos")

    #Erstellt für gegebenes Datum und Datentyp einer Datei den passenden Speicherpfad und gibt diesen zurück
    # "F:/.../19.02.01/Images"
    def getPath(self,date,type):
        path = self.path + "/" + date
        if type == "I":
            path += "/Images"
        elif type == "V":
            path += "/Videos"
        return path

    #Gibt alle existirenden Tages-Ordner aus
    def printFolders(self):
        for folder in self.folders:
            out(folder)

    #Gibt alle existirenden Tages-Ordner zurück
    # ["19.02.01",...]
    def getDates(self):
        return self.folders


class QUAX:
    path_internal = None  #Speicherpfad des internen Dronen-Speichers
    path_external = None  #Speicherpfad des externen Dronen-Speichers
    files_internal = []   #Namen der Dateien im internen Dronen-Speicher ["DJI_067",...]
    files_external = []   #Namen der Dateien im externen Dronen-Speicher ["DJI_067",...]
    iteration = [0,0]     #Zählvariable für die getNextFile Methode.
                          # Erste Stelle ist die Liste: 0 = intern 1 = extern
                          # Zweite Stelle ist der Index in dieser Liste

    def init(self):
        if not self.serachQuax():
            return False
        return True

    # Durchsucht alle verfügbaren Laufwerke nach der IDENT.Q_EXTERNAL.txt und IDENT.Q_INTERNAL.txt Datei
    # und liest aus diesen die relativen Speicherorte aus. EXTERNAL muss nicht existieren
    def serachQuax(self):
        available_drives = ['%s:' % d for d in string.ascii_uppercase if os.path.exists('%s:' % d)]
        storages = 0

        for drive in available_drives:
            if os.path.exists(drive + "/IDENT.Q_EXTERNAL.txt"):
                out("      External Storage is online")
                EXTERNAL_config = open(drive+"/IDENT.Q_EXTERNAL.txt")
                relative_path = EXTERNAL_config.readline()
                self.path_external = drive + relative_path
                EXTERNAL_config.close()
                storages += 1

        for drive in available_drives:
            if os.path.exists(drive + "/IDENT.Q_INTERNAL.txt"):
                out("      Internal Storage is online")
                INTERNAL_config = open(drive + "/IDENT.Q_INTERNAL.txt")
                relative_path = INTERNAL_config.readline()
                self.path_internal = drive + relative_path
                INTERNAL_config.close()
                storages += 1

        return storages

    def deleteAll(self):
        for file in self.files_internal:
            out("--removing: "+file)
            os.remove(self.path_internal+"/"+file)
        for file in self.files_external:
            out("--removing: "+file)
            os.remove(self.path_external+"/"+file)

    def loadFiles(self):
        self.files_internal = os.listdir(self.path_internal)
        if self.path_external:
            self.files_external = os.listdir(self.path_external)

    def getNextFile(self):
        files = [self.files_internal,self.files_external]
        file = files[self.iteration[0]][self.iteration[1]]
        if self.iteration[0] == 0:
            path = self.path_internal
        else:
            path = self.path_external
        date = self.convertTimeStamp(os.path.getctime(path+"/"+file))
        out("[ "+str(self.iteration[0]*len(self.files_internal)+self.iteration[1]+1)+" / "
            +str(len(self.files_internal)+len(self.files_external))+" ]")

        self.iteration[1] += 1
        if self.iteration[1] >= len(files[self.iteration[0]]):
            self.iteration[1] = 0
            self.iteration[0] += 1
        if self.iteration[0] <= 1:
            return file,path,date,True
        else:
            return file,path,date,False

    def readDates(self):
        dates = []
        for file in self.files_internal:
            file_date = self.convertTimeStamp(os.path.getctime(self.path_internal+"/"+file))
            if file_date not in dates:
                dates.append(file_date)

        for file in self.files_external:
            file_date = self.convertTimeStamp(os.path.getctime(self.path_external+"/"+file))
            if file_date not in dates:
                dates.append(file_date)
        return dates

    def convertTimeStamp(self,timestamp):
        converted = str(datetime.datetime.fromtimestamp(timestamp))
        date = converted.split()[0]
        date_list = date.split("-")
        date_list[0] = date_list[0][2:]
        return date_list

    def printFiles(self):
        for file in self.files_external:
            out(file)
        for file in self.files_internal:
            out(file)

    def reset(self):
        self.iteration = [0,0]


class CONTROL:
    hdd = None
    quax = None


    def __init__(self):
        if not gui:
            self.start_screen()
        out("Initalizing...")
        time.sleep(2)
        self.hdd = HDD()
        self.quax = QUAX()
        out("   Searching Storage...")
        while 1:
            time.sleep(1)
            if not self.hdd.init():

                inp("      HDD could not be found")
            else:
                break
        out("      Storage is online")
        out("")
        time.sleep(2)
        out("   Searching QUAX...")
        while 1:
            time.sleep(1)
            storage_count = self.quax.init()
            if not storage_count:
                inp("      QUAX could not be found")
            else:
                break

        out("")
        time.sleep(2)
        inp("Start Prozess?")
        time.sleep(1)
        self.copy_main()

    def convert_date(self,date):
        conv = date[0]+"."+date[1]+"."+date[2]
        return conv

    def copy_main(self):
        self.hdd.loadFolders()
        self.quax.loadFiles()
        self.hdd.printFolders()
        self.quax.printFiles()
        missing_dates = [date for date in self.quax.readDates() if date not in self.hdd.getDates()]
        out("--MISSING:")
        out(missing_dates)
        for date in missing_dates:
            date = self.convert_date(date)
            out("- CREATING "+date)
            self.hdd.createFolder(date)

        next = True
        while next:
            file,path,date,next = self.quax.getNextFile()
            destination = self.hdd.getPath(self.convert_date(date),self.determine_type(file))
            if not os.path.isfile(destination+"/"+file):
                out("- COPYING  "+file)
                out(" -"+path+" -> ")
                out(" -"+destination)
                shutil.copy2(path+"/"+file,destination+"/"+file)
                out("")
            else:
                out("- file: "+file+" is already copied")
        out("--FINISHED--")
        out("")
        self.quax.reset()

        if inp("Do you want to remove all files from the Drone? (y/n) >>>") == "y":
            out("Please verify all copies before continuing")
            time.sleep(2)
            inp("Ready >>>")
            out("")
            time.sleep(1)
            out("Starting in ")
            time.sleep(1)
            out("... 3")
            time.sleep(1)
            out("... 2")
            time.sleep(1)
            out("... 1")
            time.sleep(1)
            out("removing...")
            self.quax.deleteAll()
            out("--FINISHED--")


    def determine_type(self,file):
        image_endings = ["png","dng","jpg","jpeg"]
        video_endings = ["avi","mp4","mpeg"]
        ending = file.split(".")[-1].lower()
        if ending in image_endings:
            return "I"
        elif ending in video_endings:
            return "V"
        else:
            return None




    def start_screen(self):
        print("############################")
        print("#-------QUAX-MANAGER-------#")
        print("#--------Versin 2.0--------#")
        print("#-----Benjamin  Schaab-----#")
        print("############################")
        print()
        print()


c = CONTROL()