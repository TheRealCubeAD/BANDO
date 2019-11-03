from sys import exit # Methode für Terminierung
from pygame.color import THECOLORS # Importiert Liste von Farben
import pygame # Engine
pygame.init() # Zündschlüssel

# Setze Fenstergröße fest
width = 640
height = 480
size = (width,height)

# Erstelle Fenster
screen = pygame.display.set_mode(size)


def color(strColor):
    """
    Beispiel: color("red") == (255, 0, 0, 255)
    :param strColor: englischsprachige Bezeichnung einer Farbe
    :return: der entsprechende RGB Wert
    """
    return THECOLORS[strColor]


def flip():
    """
    Zeichnet den nächsten Frame.
    """
    pygame.display.flip()


def setCaption(strCaption):
    """
    Setzt den Titel des Pygame-Bildschirms
    :param strCaption: Titel des Bildschirms als str
    """
    pygame.display.set_caption(strCaption)


def fill(strColor):
    """
    Färbt den gesamten Bildschirm in der entsprechenden Farbe ein.
    :param strColor: Farbe der neuen Bildschirmfläche
    """
    screen.fill(color(strColor))


def drawCircle(strColor,pos,radius,lineWidth=0):
    """
    Zeichnet den beschriebenen Kreis auf dem Bildschirm
    :param strColor: Farbe des Kreises als str
    :param pos: Position des Kreismittelpunkts als (x,y) int-Tupel
    :param radius: Radius des Kreises als int
    :param lineWidth: Linienstärke des Kreises als int
    """
    pygame.draw.circle(screen,color(strColor),pos,radius,lineWidth)


def drawRectangle(strColor,pos,width,height,lineWidth=0):
    """
    Zeichnet das beschriebene Rechteck auf dem Bildschirm
    :param strColor: Farbe des Rechtecks als str
    :param pos: Position der links-oberen Ecke des Rechtecks als (x,y) int-Tupel
    :param width: Breite des Rechtecks als int
    :param height: Hoehe des Rechtecks als int
    :param lineWidth: Linienstärke des Rechtecks als int
    """
    rect = pygame.Rect(pos[0],pos[1],width,height) # Erstellt das Rechteck
    pygame.draw.rect(screen,color(strColor),rect,lineWidth)


def drawSquare(strColor,pos,width,lineWidth=0):
    """
    Zeichnet das beschriebene Quadrat auf dem Bildschirm
    :param strColor: Farbe des Quadrats als str
    :param pos: Position der links-oberen Ecke des Quadrats als (x,y) int-Tupel
    :param width: Breite des Quadrats als int
    :param lineWidth: Linienstärke des Quadrats als int
    """
    drawRectangle(strColor,pos,width,width,lineWidth)


def drawPixel(strColor,pos):
    """
    Färbt den beschriebenen Pixel entsprechend ein.
    :param strColor: Farbe des Pixels als str
    :param pos: Position des Pixels als (x,y) int-Tupel
    """
    drawSquare(strColor,pos,1)


def drawLines(strColor,closed,pointlist,lineWidth=1):
    """
    Verbindet eine Liste von Punkten der Reihe nach mit Linien.
    :param strColor: Farbe der Linien als str
    :param closed: Soll der letzte Punkt mit dem ersten verbunden werden? (True/False)
    :param pointlist: Liste von (x,y) int-Tupel
    :param lineWidth: Linienstärke der Linien
    """
    pygame.draw.lines(screen,strColor,closed,pointlist,lineWidth)


def drawKreidrat(strColor,pos,width):
    """
    Zeichnet das beschriebene Kreidrat auf dem Bildschirm.
    :param strColor: Farbe des Kreidrats.
    :param pos: Position der links-oberen Ecke des Kreidrats als (x,y) int-Tupel
    :param width: Ein Drittel der Breite des Kreidrats.
    """
    drawCircle(strColor, (pos[0] + width, pos[1] + width), width)
    drawCircle(strColor, (pos[0] + 2*width, pos[1] + width), width)
    drawCircle(strColor, (pos[0] + width, pos[1] + 2*width), width)
    drawCircle(strColor, (pos[0] + 2*width, pos[1] + 2*width), width)
    drawSquare(strColor, (pos[0] + width, pos[1]), width)
    drawSquare(strColor, (pos[0], pos[1] + width), width)
    drawSquare(strColor, (pos[0] + 2*width, pos[1] + width), width)
    drawSquare(strColor, (pos[0] + width, pos[1] + 2*width), width)




fill("orange")
drawKreidrat("magenta",(200,200),50)
drawKreidrat("magenta",(400,100),30)
flip()
setCaption("Brainfire Early Preview")


# Beginn der Ereignisschleife
while True:

    # Das Fenster lässt sich mit dem X-Knopf schließen
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit("Das Fenster wurde geschlossen.")