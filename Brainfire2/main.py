
# - Importware - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


from sys import exit # Methode für Terminierung
from pygame.color import THECOLORS # Importiert Liste von Farben
import pygame # Engine
from copy import deepcopy
import Level_inf
import pickle
pygame.init() # Zündschlüssel
pygame.font.init()



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


class mapSprite(pygame.sprite.Sprite):

    def __init__(self,pos):

        # Initiert Sprite
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([einheit, einheit])

        # Erstellt ein graues Kreidrat mit transparentem Hintergrund als Bild.
        fill(self.image,"white")
        drawKreidrat(self.image,"gray",(0,0),int(einheit/3))
        self.image.set_colorkey(color("white"))

        # Setze rechteckige Hülle des Sprites fest.
        self.rect = self.image.get_rect()
        self.rect.left = pos[0]
        self.rect.top = pos[1]


class doorSprite(pygame.sprite.Sprite):

    def __init__(self,pos, strWand):

        # Initiert Sprite
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([einheit, einheit])

        # Erstellt ein graues Kreidrat mit transparentem Hintergrund als Bild.
        fill(self.image,"white")
        drawKreidrat(self.image,"darkred",(0,0),int(einheit/3))
        self.image.set_colorkey(color("white"))

        # Setze rechteckige Hülle des Sprites fest.
        self.rect = self.image.get_rect()
        self.rect.left = pos[0]
        self.rect.top = pos[1]

        self.wand = strWand


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


class cursorSprite(pygame.sprite.Sprite):

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


class aimSprite(pygame.sprite.Sprite):

    def __init__(self,pos):

        # Initiert Sprite
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([einheit, einheit])

        # Erstellt ein graues Kreidrat mit transparentem Hintergrund als Bild.
        fill(self.image,"white")
        drawKreidrat(self.image,"gold",(0,0),int(einheit/3))
        self.image.set_colorkey(color("white"))

        # Setze rechteckige Hülle des Sprites fest.
        self.rect = self.image.get_rect()
        self.rect.left = pos[0]
        self.rect.top = pos[1]



if __name__ == '__main__':


    # - Setup - - -  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    # Maus nicht sichtbar
    # pygame.mouse.set_visible(False)

    # Debugging Tool
    debugging = True

    # Setze Standardeinheit fest
    einheit = 15
    einheit *= 3 # Standardeinheit muss wegen der Kreidrate ein Vielfaches von 3 sein.

    # Setzt Bewegungsgeschwindgkeit fest
    speed = 8

    # Startpositionen
    start_links = (einheit, 9 * einheit)
    start_oben = (8 * einheit, einheit)
    start_rechts = (16 * einheit, 8 * einheit)
    start_unten = (9 * einheit, 16 * einheit)

    # Setze Fenstergröße fest
    height = einheit * (16+2)
    width = einheit * 26
    # width = height
    size = (width,height)

    # Erstelle Fenster
    screen = pygame.display.set_mode(size)
    setCaption("Brainfire (Closed Alpha)")
    icon = pygame.Surface((1,1))
    icon.set_alpha(0)
    pygame.display.set_icon(icon)

    # Initialisiert Zeitbegrenzung
    clock = pygame.time.Clock()

    # Generiert alle Steine, die den Rand bilden und gruppiert sie.
    Border = pygame.sprite.Group()
    Border.add(stoneSprite([0,0]))
    Border.add(stoneSprite([0,(16+1)*einheit]))
    Border.add(stoneSprite([(16+1)*einheit,0]))
    Border.add(stoneSprite([(16+1)*einheit,(16+1)*einheit]))
    for i in range(1,17):
        if i != 8:
            Border.add(stoneSprite([i*einheit,0]))
        if i != 9:
            Border.add(stoneSprite([0,i * einheit]))
        if i != 8:
            Border.add(stoneSprite([(16+1)*einheit,i * einheit]))
        if i != 9:
            Border.add(stoneSprite([i*einheit, (16 + 1) * einheit]))

    # Erstellt Spieler
    player = playerSprite(start_unten)
    last_start = start_unten

    # Erstelle Level
    level_number = "test"
    level = Level_inf.create_level(level_number)

    # Bereite Dungeon vor
    level_matrix = [ [ None for _ in range(16)] for _ in range(16) ]
    for x in range(6):
        for y in range(6):
            level_matrix[y][x] = level.matrix[y][x].getMatrix()

    anfangsraum = [ [ 0 for x in range(16) ] for y in range(16) ]
    anfangsraum[7][0] = 1
    anfangsraum[15][7] = 1
    anfangsraum[8][15] = 1
    anfangsraum[0][8] = 1
    level_matrix[0][0] = anfangsraum
    level_matrix[5][5] = anfangsraum

    dpos = [0, 0]
    raum = level_matrix[dpos[0]][dpos[1]]
    cursor = cursorSprite([(dpos[1] + 19) * einheit, (dpos[0] + 1) * einheit])

    # Generiert alle Türen
    Doors = pygame.sprite.Group()

    if dpos[0] != 0:
        Doors.add(doorSprite([8 * einheit, 0], "oben"))
    else:
        Doors.add(stoneSprite([8 * einheit, 0]))

    if dpos[1] != 0:
        Doors.add(doorSprite([0, 9 * einheit], "links"))
    else:
        Doors.add(stoneSprite([0, 9 * einheit]))

    if dpos[1] != 5:
        Doors.add(doorSprite([17 * einheit, 8 * einheit], "rechts"))
    else:
        Doors.add(stoneSprite([17 * einheit, 8 * einheit]))

    if dpos[0] != 5:
        Doors.add(doorSprite([9 * einheit, 17 * einheit], "unten"))
    else:
        Doors.add(stoneSprite([9 * einheit, 17 * einheit]))

    # Generiert alle Steine
    Stones = pygame.sprite.Group()
    for x in range(16):
        for y in range(16):
            if raum[y][x] == 1:
                Stones.add(stoneSprite([(x+1)*einheit,(y+1)*einheit]))


    # Generiert Map
    Map = pygame.sprite.Group()
    for x in range(6):
        for y in range(6):
            Map.add( mapSprite([(x+19)*einheit,(y+1)*einheit]) )

    aim = aimSprite([(5 + 19) * einheit, (5 + 1) * einheit])



    zielraumErreicht = False

    timer = 0.0
    font = pygame.font.SysFont('Consolas', int(einheit*2/3))
    elapsed_time_text = font.render("Elapsed Seconds:", False, (0, 0, 0))

    seconds_left_to_text = font.render("Seconds left to", False, (0, 0, 0))
    reach_the_exit_text = font.render("reach the exit:", False, (0,0,0))
    countdown = 5*60

    thanks_for_playing_text = font.render("Thanks for playing!", False, (0,0,0))

    gameover_text = font.render("Game Over!", False, (0,0,0))

    time_stop = False

    # - Mainschleife - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


    while True:

        # Ereignisschleife
        for event in pygame.event.get():


            # Das Fenster lässt sich mit dem X-Knopf schließen
            if event.type == pygame.QUIT:
                exit("Das Fenster wurde geschlossen.")

            # Eine Taste wurde degrückt
            elif event.type == pygame.KEYDOWN:

                # Reset-Button
                if event.key == pygame.K_r:
                    player.rect.left = last_start[0]
                    player.rect.top = last_start[1]
                    player.inMotion = False
                    player.velocity = [0, 0]

                # Debugging Tool:
                # Der Spieler kann sich an eine beliebige Tür mit WASD transportieren lassen.
                if debugging:

                    if event.key == pygame.K_w:
                        player.rect.left = start_oben[0]
                        player.rect.top = start_oben[1]
                        player.inMotion = False
                        player.velocity = [0, 0]

                    elif event.key == pygame.K_a:
                        player.rect.left = start_links[0]
                        player.rect.top = start_links[1]
                        player.inMotion = False
                        player.velocity = [0, 0]

                    elif event.key == pygame.K_s:
                        player.rect.left = start_unten[0]
                        player.rect.top = start_unten[1]
                        player.inMotion = False
                        player.velocity = [0, 0]

                    if event.key == pygame.K_d:
                        player.rect.left = start_rechts[0]
                        player.rect.top = start_rechts[1]
                        player.inMotion = False
                        player.velocity = [0, 0]



                # Ist der Spieler nicht in Bewegung?
                if not player.inMotion:

                    # Bewege den Spieler mit den Pfeiltasten
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


                    # Der Spieler will durch eine Tür gehen.
                    elif event.key == pygame.K_SPACE:

                        # Switch, ob der Raum neu zu zeichnen ist.
                        zeichneNeu = False

                        # Ist der Spieler and der oberen Tür?
                        if player.rect.left == start_oben[0] and player.rect.top == start_oben[1]:
                            # Gibt es einen darüberliegenden Raum?
                            if dpos[0] != 0:
                                # Bringe den Spieler in diesen Raum!
                                zeichneNeu = True
                                dpos[0] -= 1
                                player.rect.left = start_unten[0]
                                player.rect.top = start_unten[1]
                                last_start = start_unten

                        # Ist der Spieler an der links Tür?
                        elif player.rect.left == start_links[0] and player.rect.top == start_links[1]:
                            # Gibt es einen Raum links?
                            if dpos[1] != 0:
                                # Bringe den Spieler in diesen Raum!
                                zeichneNeu = True
                                dpos[1] -= 1
                                player.rect.left = start_rechts[0]
                                player.rect.top = start_rechts[1]
                                last_start = start_rechts

                        # Ist der Spieler an der unteren Tür?
                        elif player.rect.left == start_unten[0] and player.rect.top == start_unten[1]:
                            # Gibt es einen darüberliegenden Raum?
                            if dpos[0] != 5:
                                # Bringe den Spieler in diesen Raum!
                                zeichneNeu = True
                                dpos[0] += 1
                                player.rect.left = start_oben[0]
                                player.rect.top = start_oben[1]
                                last_start = start_oben


                        # Ist der Spieler an der rechten Tür?
                        elif player.rect.left == start_rechts[0] and player.rect.top == start_rechts[1]:
                            # Gibt es einen darüberliegenden Raum?
                            if dpos[1] != 5:
                                # Bringe den Spieler in diesen Raum!
                                zeichneNeu = True
                                dpos[1] += 1
                                player.rect.left = start_links[0]
                                player.rect.top = start_links[1]
                                last_start = start_links



                        if zeichneNeu:

                            zeichneNeu = False
                            raum = deepcopy(level_matrix[dpos[0]][dpos[1]])
                            Doors = pygame.sprite.Group()

                            if dpos[0] != 0:
                                Doors.add(doorSprite([8 * einheit, 0], "oben"))
                            else:
                                Doors.add(stoneSprite([8 * einheit, 0]))

                            if dpos[1] != 0:
                                Doors.add(doorSprite([0, 9 * einheit], "links"))
                            else:
                                Doors.add(stoneSprite([0, 9 * einheit]))

                            if dpos[1] != 5:
                                Doors.add(doorSprite([17 * einheit, 8 * einheit], "rechts"))
                            else:
                                Doors.add(stoneSprite([17 * einheit, 8 * einheit]))

                            if dpos[0] != 5:
                                Doors.add(doorSprite([9 * einheit, 17 * einheit], "unten"))
                            else:
                                Doors.add(stoneSprite([9 * einheit, 17 * einheit]))

                            # Generiert alle Steine
                            Stones = pygame.sprite.Group()

                            for x in range(16):
                                for y in range(16):
                                    if raum[y][x] == 1:
                                        Stones.add(stoneSprite([(x + 1) * einheit, (y + 1) * einheit]))

                            cursor.rect.left = (dpos[1] + 19) * einheit
                            cursor.rect.top = (dpos[0] + 1) * einheit

                            if dpos == [5,5]:
                                zielraumErreicht = True
                                aim.rect.left = (0 + 19) * einheit
                                aim.rect.top = (0 + 1) * einheit

                            if dpos == [0,0] and zielraumErreicht:
                                time_stop = True

        # Färbt den Bildschirm hellblau.
        fill(screen, "lightblue")  # Eisfläche

        # Legt alle Steine an den Rand.
        drawSpriteGroup(screen, Border)
        drawSpriteGroup(screen, Stones)
        drawSpriteGroup(screen, Doors)
        drawSpriteGroup(screen, Map)
        drawSprite(screen,aim)
        drawSprite(screen,cursor)

        # Bewege den Spieler
        player.move()
        drawSprite(screen, player)

        # Kollidiert der Spieler mit einer Wand, so setze ihn vor die Wand
        if pygame.sprite.spritecollide(player, Border, False)\
                or pygame.sprite.spritecollide(player, Stones, False)\
                or pygame.sprite.spritecollide(player, Doors, False):
            player.rect.left = round(player.rect.left / einheit) * einheit
            player.rect.top = round(player.rect.top / einheit) * einheit
            player.velocity = [0,0]
            player.inMotion = False





        if not time_stop:

            timer += 0.01
            timertext = font.render(str(int(timer)), False, (0, 0, 0))
            screen.blit(elapsed_time_text,(20 * einheit, 9*einheit))
            screen.blit(timertext,(20*einheit,10*einheit))

            if zielraumErreicht:
                countdown -= 0.01
                screen.blit(seconds_left_to_text, (20*einheit,12*einheit))
                screen.blit(reach_the_exit_text, (20 * einheit, 13 * einheit))
                countdowntext = font.render(str(int(10*countdown)/10), False, (0, 0, 0))
                screen.blit(countdowntext, (20 * einheit, 14 * einheit))

        else:
            timertext = font.render(str(int(100*timer)/100), False, (0, 0, 0))
            screen.blit(elapsed_time_text, (20 * einheit, 9 * einheit))
            screen.blit(timertext, (20 * einheit, 10 * einheit))
            screen.blit(seconds_left_to_text, (20 * einheit, 12 * einheit))
            screen.blit(reach_the_exit_text, (20 * einheit, 13 * einheit))
            countdowntext = font.render(str(int(100 * countdown) / 100), False, (0, 0, 0))
            screen.blit(countdowntext, (20 * einheit, 14 * einheit))
            screen.blit(thanks_for_playing_text, (20 * einheit, 16 * einheit))

        if countdown <= 0:
            fill(screen,"red")
            screen.blit(gameover_text, (width/2 - 1.5* einheit, height/2 - 0.5*einheit))

        # Aktualisiert das Fenster
        flip()

        # 100 FPS
        clock.tick(100)