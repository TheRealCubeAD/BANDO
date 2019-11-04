
# - Importware - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


from sys import exit # Methode für Terminierung
from pygame.color import THECOLORS # Importiert Liste von Farben
import pygame # Engine
import Level_inf
import pickle
pygame.init() # Zündschlüssel



# - Hilfsmethoden - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


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


def fill(surface,strColor):
    """
    Färbt den gesamten Bildschirm in der entsprechenden Farbe ein.
    :param strColor: Farbe der neuen Bildschirmfläche
    """
    surface.fill(color(strColor))


def drawCircle(surface,strColor,pos,radius,lineWidth=0):
    """
    Zeichnet den beschriebenen Kreis auf dem Bildschirm
    :param strColor: Farbe des Kreises als str
    :param pos: Position des Kreismittelpunkts als (x,y) int-Tupel
    :param radius: Radius des Kreises als int
    :param lineWidth: Linienstärke des Kreises als int
    """
    pygame.draw.circle(surface,color(strColor),pos,radius,lineWidth)


def drawRectangle(surface,strColor,pos,width,height,lineWidth=0):
    """
    Zeichnet das beschriebene Rechteck auf dem Bildschirm
    :param strColor: Farbe des Rechtecks als str
    :param pos: Position der links-oberen Ecke des Rechtecks als (x,y) int-Tupel
    :param width: Breite des Rechtecks als int
    :param height: Hoehe des Rechtecks als int
    :param lineWidth: Linienstärke des Rechtecks als int
    """
    rect = pygame.Rect(pos[0],pos[1],width,height) # Erstellt das Rechteck
    pygame.draw.rect(surface,color(strColor),rect,lineWidth)


def drawSquare(surface,strColor,pos,width,lineWidth=0):
    """
    Zeichnet das beschriebene Quadrat auf dem Bildschirm
    :param strColor: Farbe des Quadrats als str
    :param pos: Position der links-oberen Ecke des Quadrats als (x,y) int-Tupel
    :param width: Breite des Quadrats als int
    :param lineWidth: Linienstärke des Quadrats als int
    """
    drawRectangle(surface,strColor,pos,width,width,lineWidth)


def drawPixel(surface,strColor,pos):
    """
    Färbt den beschriebenen Pixel entsprechend ein.
    :param strColor: Farbe des Pixels als str
    :param pos: Position des Pixels als (x,y) int-Tupel
    """
    drawSquare(surface,strColor,pos,1)


def drawLines(surface,strColor,closed,pointlist,lineWidth=1):
    """
    Verbindet eine Liste von Punkten der Reihe nach mit Linien.
    :param strColor: Farbe der Linien als str
    :param closed: Soll der letzte Punkt mit dem ersten verbunden werden? (True/False)
    :param pointlist: Liste von (x,y) int-Tupel
    :param lineWidth: Linienstärke der Linien
    """
    pygame.draw.lines(surface,strColor,closed,pointlist,lineWidth)


def drawKreidrat(surface,strColor,pos,width):
    """
    Zeichnet das beschriebene Kreidrat auf dem Bildschirm.
    :param strColor: Farbe des Kreidrats.
    :param pos: Position der links-oberen Ecke des Kreidrats als (x,y) int-Tupel
    :param width: Ein Drittel der Breite des Kreidrats.
    """
    drawCircle(surface, strColor, (pos[0] + width, pos[1] + width), width)
    drawCircle(surface, strColor, (pos[0] + 2*width, pos[1] + width), width)
    drawCircle(surface, strColor, (pos[0] + width, pos[1] + 2*width), width)
    drawCircle(surface, strColor, (pos[0] + 2*width, pos[1] + 2*width), width)
    drawSquare(surface, strColor, (pos[0] + width, pos[1]), width)
    drawSquare(surface, strColor, (pos[0], pos[1] + width), width)
    drawSquare(surface, strColor, (pos[0] + 2*width, pos[1] + width), width)
    drawSquare(surface, strColor, (pos[0] + width, pos[1] + 2*width), width)


def drawSprite(surface,sprite):
    """
    :param surface: Zeichenfläche
    :param sprite: Zu zeichnendes Sprite
    """
    surface.blit(sprite.image, sprite.rect)


def drawSpriteGroup(surface,group):
    """
    :param surface: Zeichenfläche
    :param group: Zu zeichnende Sprite Gruppe
    """
    for sprite in group:
        drawSprite(surface,sprite)


# - Sprites - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


class stoneSprite(pygame.sprite.Sprite):

    def __init__(self,pos):

        # Initiert Sprite
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([einheit, einheit])

        # Erstellt ein graues Kreidrat mit transparentem Hintergrund als Bild.
        fill(self.image,"white")
        drawKreidrat(self.image,"black",(0,0),int(einheit/3))
        self.image.set_colorkey(color("white"))

        # Setze rechteckige Hülle des Sprites fest.
        self.rect = self.image.get_rect()
        self.rect.left = pos[0]
        self.rect.top = pos[1]



class playerSprite(pygame.sprite.Sprite):

    def __init__(self,pos):

        # Initiert Sprite
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([einheit, einheit])

        # Erstellt ein graues Kreidrat mit transparentem Hintergrund als Bild.
        fill(self.image,"white")
        drawKreidrat(self.image,"purple",(0,0),int(einheit/3))
        self.image.set_colorkey(color("white"))

        # Setze rechteckige Hülle des Sprites fest.
        self.rect = self.image.get_rect()
        self.rect.left = pos[0]
        self.rect.top = pos[1]

        # Setze Geschwindigkeit
        self.velocity = [0,0]
        self.inMotion = False


    def move(self):
        self.rect = self.rect.move(self.velocity)


if __name__ == '__main__':


    # - Setup - - -  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    # Setze Standardeinheit fest
    einheit = 16
    einheit *= 3 # Standardeinheit muss wegen der Kreidrate ein Vielfaches von 3 sein.

    # Setzt Bewegungsgeschwindgkeit fest
    speed = 8

    # Startposition
    startpos = ((1)*einheit,(9)*einheit)

    # Setze Fenstergröße fest
    height = einheit * (16+2)
    width = int( height * 4 / 3)
    size = (width,height)

    # Erstelle Fenster
    screen = pygame.display.set_mode(size)
    setCaption("Your Dad Lesbian")

    # Initialisiert Zeitbegrenzung
    clock = pygame.time.Clock()

    # Generiert alle Steine, die den Rand bilden und gruppiert sie.
    Border = pygame.sprite.Group()
    Border.add( stoneSprite([0,0]) )
    Border.add( stoneSprite([0,(16+1)*einheit]) )
    Border.add( stoneSprite([(16+1)*einheit,0]) )
    Border.add( stoneSprite([(16+1)*einheit,(16+1)*einheit]) )
    for i in range(1,17):
        if i != 8:
            Border.add( stoneSprite([i*einheit,0]) )
        if i != 9:
            Border.add( stoneSprite([0,i * einheit]) )
        if i != 8:
            Border.add( stoneSprite([(16+1)*einheit,i * einheit]) )
        if i != 9:
            Border.add( stoneSprite([i*einheit, (16 + 1) * einheit]))




    # Erstellt Spieler
    player = playerSprite(startpos)





    # Erstelle Level
    level_number = "test"
    level = Level_inf.create_level(level_number)

    raum = level.matrix[1][1]

    Stones = pygame.sprite.Group()
    for x in range(16):
        for y in range(16):
            if raum.matrix[y][x] == 1:
                Stones.add( stoneSprite([(x+1)*einheit,(y+1)*einheit]) )


    # - Mainschleife - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


    while True:

        # Ereignisschleife
        for event in pygame.event.get():

            # Das Fenster lässt sich mit dem X-Knopf schließen
            if event.type == pygame.QUIT:
                exit("Das Fenster wurde geschlossen.")

            # Eine Pfeiltaste wurde degrückt
            elif event.type == pygame.KEYDOWN:

                if event.key == pygame.K_r:
                    player.rect.left = startpos[0]
                    player.rect.top = startpos[1]
                    player.inMotion = False
                    player.velocity = [0, 0]

                # Ist der Spieler in Bewegung?
                if not player.inMotion:

                    if event.key == pygame.K_UP:
                        player.inMotion = True
                        player.velocity = [0, -speed]

                    elif event.key == pygame.K_DOWN:
                        player.inMotion = True
                        player.velocity = [0, speed]

                    elif event.key == pygame.K_LEFT:
                        player.inMotion = True
                        player.velocity = [-speed, 0]

                    elif event.key == pygame.K_RIGHT:
                        player.inMotion = True
                        player.velocity = [speed, 0]


        # Färbt den Bildschirm hellblau.
        fill(screen, "lightblue")  # Eisfläche

        # Legt alle Steine an den Rand.
        drawSpriteGroup(screen, Border)
        drawSpriteGroup(screen, Stones)

        # Bewege den Spieler
        player.move()
        drawSprite(screen, player)

        # Kollidiert der Spieler mit einer Wand, so setze ihn vor die Wand
        if pygame.sprite.spritecollide(player, Border, False)\
                or pygame.sprite.spritecollide(player, Stones, False):
            player.rect.left = round(player.rect.left / einheit) * einheit
            player.rect.top = round(player.rect.top / einheit) * einheit
            player.velocity = [0,0]
            player.inMotion = False


        # Aktualisiert das Fenster
        flip()

        # 90 FPS
        clock.tick(90)