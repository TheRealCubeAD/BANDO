from luma.core.interface.serial import i2c,spi
from luma.core.render import canvas
from luma.oled.device import sh1106
import time
import threading

class DISPLAY:

    device = None  #Display-steurernde Klasse aus dem Luma package
    active = False  #main() wird nur bei active=True arbeiten
    occupied = False  #True wenn gerade etwas gezeichnet wird
    cueList = []  #Liste aller Aufträge die noch bearbeitet werden müssen
                  #[["Schlüsselwort_für_Aufgabe",Argument_für_Aufgabe],...]
    main_thread = None  #Thread für main()
    print_meths = None  #Dictionary mit den Schlüsseln für print-methoden

    def __init__(self):
        serial = i2c(port=1,address=0x3C)
        self.device = sh1106(serial)
        self.print_meths = {"beg":self.print_beg}
        print(self.device.bounding_box)

    def activate(self):  #Startet main() als Thread (von außen aufzurufen)
        self.active = True
        self.main_thread = threading.Thread(target=self.main)
        self.main_thread.daemon = True
        self.main_thread.start()

    def deactivate(self):  #Schaltet main() ab (von außen aufzurufen)
        self.active = False
        while self.occupied:  #Warten bis main() mit der derzeitigen Aufgabe fertig ist
            pass
        with canvas(self.device) as draw:  #Bildschirm schwärzen
            draw.rectangle(self.device.bounding_box, outline="black", fill="black")

    def add(self,meth,arg=None):  #Fügt eine Aufgabe der Liste hinten an (von außen aufzurufen)
        self.cueList.append((meth,arg))

    def main(self):  #Führt Aufgaben aus cueList aus. Gibt es keine Aufgabe wird die Zeit angezeigt
        while self.active:
            if not self.occupied:
                if self.cueList:  #Wenn eine Aufgabe verfügbar ist
                    meth, arg = self.pick()  #Aufgabe aufschlüsseln
                    self.meth_starter(meth,arg)  #Aufgabe ausführen
                else:
                    self.meth_starter(self.print_time,None)  #Zeit anziegen

    def pick(self):  #Übersetzt die Aufgabe in eine Methode und das Argument
        item = self.cueList[0]  #Aufgabe nehmen
        del(self.cueList[0])  #Aufgabe aus Liste löschen
        methode = self.print_meths[item[0]]  #Passende Methode aus Dictionary suchen
        argument = item[1]  #Argument aus der Aufgabe nehmen
        return methode, argument  #Methode und Argument zurückgeben

    def meth_starter(self,meth,arg):  #Hilfsmethode zum ausführen der Aufgabe
        self.occupied = True
        if arg:
            meth(arg)
        else:
            meth()
        self.occupied = False


    def print_beg(self):  #Zeigt eine zu Zeit passenden Begrüssung an
        localtime = time.asctime(time.localtime(time.time()))
        localtime = localtime.split()[3]
        hour = localtime.split(":")[0]
        hour = int(hour)  #Stunde rausfiltern
        text = None
        if hour <= 11 :
            text = "Guten Morgen"
        elif hour <= 17 :
            text = "Guten Tag"
        else:
            text = "Guten Abend"

        with canvas(self.device) as draw:
            draw.rectangle(self.device.bounding_box, outline="white", fill="black")  #fancy Rand
            draw.text((30, 20), text, fill="white")  #Bergüssung
            draw.text((40,35),"Benjamin",fill="white")  #Name
        time.sleep(10)  #10 sec

    def print_time(self):  #Zeigt die Zeit an in hh:mm
        localtime = time.asctime(time.localtime(time.time()))
        localtime = localtime.split()[3][:5]
        with canvas(self.device) as draw:
            draw.text((53,30),localtime,fill="white")
        time.sleep(0.5)  #0.5 sec (-> Takt der main-Methode)

