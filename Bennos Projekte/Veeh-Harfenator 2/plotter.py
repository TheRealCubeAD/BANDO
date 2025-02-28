from PIL import Image, ImageDraw, ImageFont
from song import SONG

size = 2000
max_note = 24
border_x = 1
border_y = 50
max_notes_per_site = 51

lng = None

def plott(song, grid=False):
    """
    Plots the song
    :param song: Song object
    :param grid: Show grid
    """
    sites = calc_notes(song)
    for site in sites:
        plott_site(site, grid)

def plott_site(entrys, grid):
    """
    Plots a site
    :param entrys: List of notes
    :param grid: Show grid
    """
    image = Image.new("1", (size, size), 1)
    draw = ImageDraw.Draw(image)

    # Grid
    if grid:
        draw_grid(draw, len(entrys))

    # Vert lines
    for ey in range(len(entrys) - 1):
        n1 = entrys[ey]
        n2 = entrys[ey + 1]
        y1 = calc_y(len(entrys), ey)
        y2 = calc_y(len(entrys), ey + 1)
        x1 = calc_x(n1.notes[0])
        x2 = calc_x(n2.notes[0])
        draw.line(((x1, y1), (x2, y2)), width=5)

    # Notes and horizontal lines
    for ey in range(len(entrys)):
        notes = entrys[ey].notes
        y = calc_y(len(entrys), ey)
        for i in range(len(notes) - 1):
            ex1 = notes[i]
            ex2 = notes[i + 1]
            if ex1 == None or ex2 == None:
                continue
            draw.line(((calc_x(ex1), y), (calc_x(ex2), y)), width=3)
        draw_note(draw, entrys[ey], y)
    image.show()


def draw_note(draw, note, y):
    """
    Draws a note
    :param draw: draw object
    :param note: Note
    :param y: y position
    """

    sizes = {1: 20, 2: 15, 4: 15, 8: 10}
    size = sizes[note.lenght]
    if note.lenght == 1 or note.lenght == 2:
        hollow = True
    else:
        hollow = False

    for n in note.notes:
        if n == None:
            continue
        x = calc_x(n)
        if note.mode == 0:
            draw_ellipse(draw, x, y, size, hollow)
        else:
            draw_rect(draw, x, y, size, hollow)

        if note.point:
            draw.circle((x+size*1.5, y+size), 5, fill=0)


def draw_ellipse(draw, x, y, size, hollow=False):
    """
    Draws an ellipse
    :param draw: draw object
    :param x: x position
    :param y: y position
    :param size: size
    :param hollow: hollow
    """
    stretch = 1.5
    if hollow:
        draw.ellipse(((x - size*stretch, y - size), (x + size*stretch, y + size)), outline=0, fill=1, width=5)
    else:
        draw.ellipse(((x - size*stretch, y - size), (x + size*stretch, y + size)), fill=0)

def draw_rect(draw, x, y, size, hollow=False):
    """
    Draws a rectangle
    :param draw: draw object
    :param x: x position
    :param y: y position
    :param size: size
    :param hollow: hollow
    """
    stretch = 0.75
    if hollow:
        draw.rectangle(((x - size*stretch, y - size), (x + size*stretch, y + size)), outline=0, fill=1, width=5)
    else:
        draw.rectangle(((x - size*stretch, y - size), (x + size*stretch, y + size)), fill=0)

def draw_grid(draw, count_y):
    """
    Draws the grid
    :param draw: draw object
    :param count_y: count of y lines
    """
    font = ImageFont.truetype(font="arial.ttf", size=30)
    for i in range(max_note + 1):
        x = calc_x(i)
        draw.line(((x, 0), (x, size)))
    draw.rectangle(((0, 25), (size, 60)), fill="white")
    for i in range(max_note + 1):
        x = calc_x(i)
        text_size = draw.textlength(lng.keys[i], font=font)
        draw.text((x - text_size/2, 25), lng.keys[i], font=font)
    for i in range(count_y):
        y = calc_y(count_y, i)
        draw.line(((0, y), (size, y)))



def calc_notes(song):
    """
    Splits the notes into sites
    :param song: Song
    :return: List of sites
    """
    notes = song.get_notes()
    site_count = int(len(notes) / max_notes_per_site) + 1
    result = [None for _ in range(site_count)]
    for i in range(len(result)):
        count = int(len(notes)/site_count)
        site_count -= 1
        result[i] = notes[:count]
        del(notes[:count])
    return result


def calc_x(index):
    return int(size / (max_note + border_x * 2) * (border_x + index))

def calc_y(lenght, index):
    return int((size - 2 * border_y) / (lenght + 1) * (index + 1) + border_y)


class test:
    def get_notes(self):
        return [i for i in range(153)]


if __name__ == '__main__':
    print(plott(test()))