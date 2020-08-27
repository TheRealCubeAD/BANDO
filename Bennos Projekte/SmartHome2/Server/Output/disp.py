from luma.core.interface.serial import i2c,spi
from luma.core.render import canvas
from luma.oled.device import sh1106
import time
import threading

class DISPLAY:

    device = None  #Display-steurernde Klasse aus dem Luma package
    active = False  #main() wird nur bei active=True arbeiten
    occupied = False  #True wenn gerade etwas gezeichnet wird
    cueList = []  #Liste aller Auftraege die noch bearbeitet werden muessen
                  #[["Schluesselwort_fuer_Aufgabe",Argument_fuer_Aufgabe],...]
    main_thread = None  #Thread fuer main()
    print_meths = None  #Dictionary mit den Schluesseln fuer print-methoden

    def __init__(self):
        serial = i2c(port=1,address=0x3C)
        self.device = sh1106(serial)
        self.print_meths = {"beg":self.print_beg,"time":self.print_time,
                            "starter":self.print_starter,"pout":self.print_fo}
        print(self.device.bounding_box)


    def activate(self):  #Startet main() als Thread (von aussen aufzurufen)
        self.active = True
        self.main_thread = threading.Thread(target=self.main)
        self.main_thread.daemon = True
        self.main_thread.start()
        self.add("beg")

    def deactivate(self):  #Schaltet main() ab (von aussen aufzurufen)
        self.active = False
        while self.occupied:  #Warten bis main() mit der derzeitigen Aufgabe fertig ist
            pass
        time.sleep(1)
        self.print_text(["SHUTTING DOWN"],5)
        with canvas(self.device) as draw:  #Bildschirm schwaerzen
            draw.rectangle(self.device.bounding_box, outline="black", fill="black")

    def add(self,meth,arg=None):  #Fuegt eine Aufgabe der Liste hinten an (von aussen aufzurufen)
        self.cueList.append((meth,arg))

    def main(self):  #Fuehrt Aufgaben aus cueList aus. Gibt es keine Aufgabe wird die Zeit angezeigt
        while self.active:
            if not self.occupied:
                if self.cueList:  #Wenn eine Aufgabe verfuegbar ist
                    meth, arg = self.pick()  #Aufgabe aufschluesseln
                    self.meth_starter(meth,arg)  #Aufgabe ausfuehren
                else:
                    with canvas(self.device) as draw:  # Bildschirm schwaerzen
                        draw.rectangle(self.device.bounding_box, outline="black", fill="black")

    def pick(self):  #uebersetzt die Aufgabe in eine Methode und das Argument
        item = self.cueList[0]  #Aufgabe nehmen
        del(self.cueList[0])  #Aufgabe aus Liste loeschen
        methode = self.print_meths[item[0]]  #Passende Methode aus Dictionary suchen
        argument = item[1]  #Argument aus der Aufgabe nehmen
        return methode, argument  #Methode und Argument zurueckgeben

    def print_fo(self,arg):
        cont, t = arg
        cont = cont.split("##")
        t = int(t)
        self.print_text(cont,t)

    def meth_starter(self,meth,arg):  #Hilfsmethode zum ausfuehren der Aufgabe
        self.occupied = True
        if arg:
            meth(arg)
        else:
            meth()
        self.occupied = False


    def print_beg(self):  #Zeigt eine zu Zeit passenden Begruessung an
        localtime = time.asctime(time.localtime(time.time()))
        localtime = localtime.split()[3]
        hour = localtime.split(":")[0]
        hour = int(hour)  #Stunde rausfiltern
        text = None
        if hour <= 11 :
            text = "Guten Morgen"
        elif hour <= 17 :
            text = " Guten Tag "
        else:
            text = "Guten Abend"
        with canvas(self.device) as draw:  #Bildschirm schwaerzen
            draw.rectangle(self.device.bounding_box, outline="white", fill="black")
        time.sleep(1)
        self.print_text([text,"Benjamin"],10)


    def print_time(self):  #Zeigt die Zeit an in hh:mm
        localtime = time.asctime(time.localtime(time.time()))
        localtime = localtime.split()[3][:5]
        self.print_text([localtime],4)


    def print_starter(self):
        text = ""
        for i in range(32):
            text += "."
            with canvas(self.device) as draw:
                draw.text((0, 30), text, fill="white")


    def print_text(self,lines,t):
        sy_perline = 12
        sx_perchar = 6.5
        y_middle = 37
        x_middle = 66
        with canvas(self.device) as draw:
            for line in lines:
                y = y_middle + int((lines.index(line) - (len(lines)+1)/2) * sy_perline)
                x = x_middle - int(len(line)*sx_perchar/2)
                draw.text((x,y), line, fill="white")

        time.sleep(t)


if __name__ == "__main__":
    d = DISPLAY()
    d.activate()
    d.occupied = True
    d.print_text(["Alogrithm","Muse"],5)