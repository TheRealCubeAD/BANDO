from PIL import Image, ImageDraw, ImageFont
from song import SONG

size = 2000
max_note = 24
border_x = 1
border_y = 50
max_notes_per_site = 51

lng = None

def plott(song, grid=False):
    sites = calc_notes(song)
    for site in sites:
        plott_site(site, grid)

def plott_site(entrys, grid):
    image = Image.new("1", (size, size), 1)
    draw = ImageDraw.Draw(image)
    if grid:
        draw_grid(draw, len(entrys))
    for ey in range(len(entrys)):
        notes = entrys[ey].notes
        y = calc_y(len(entrys), ey)
        for i in range(len(notes) - 1):
            ex1 = notes[i]
            ex2 = notes[i + 1]
            if ex1 == None or ex2 == None:
                continue
            draw.line(((calc_x(ex1), y), (calc_x(ex2), y)), width=5)
    image.show()


def draw_grid(draw, count_y):
    font = ImageFont.truetype(font="arial.ttf", size=30)
    for i in range(max_note + 1):
        x = calc_x(i)
        draw.line(((x, 0), (x, size)))
    draw.rectangle(((0, 25), (size, 60)), fill="white")
    for i in range(max_note + 1):
        x = calc_x(i)
        text_size = draw.textsize(lng.keys[i], font=font)
        draw.text((x - text_size[0]/2, 25), lng.keys[i], font=font)
    for i in range(count_y):
        y = calc_y(count_y, i)
        draw.line(((0, y), (size, y)))



def calc_notes(song):
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