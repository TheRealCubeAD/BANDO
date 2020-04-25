from tkinter import *
from functools import partial

# TODO: button_creator
# TODO: link maker
# TODO: settings bar
# TODO: info bar
# TODO: history
# TODO: history_tools
# TODO: logic
# TODO: current_bar
# TODO: export
# TODO: live view
# TODO: cutter
# TODO: Settings
# TODO: english
# TODO: piano_creator
# TODO: veeh_creator



settings = {
    "language":"german",
    "color_theme":"dark"
}

if settings["language"] == "german":
    keys = ["G", "G#", "A", "Hb", "H", "C", "C#", "D", "Eb", "E", "F", "F#", "G2", "G#2", "A2", "Hb2", "H2",
            "C2", "C#2", "D2", "Eb2", "E2", "F2", "F#2", "G3"]

elif settings["language"] == "english":
    keys = ["G", "G#", "A", "Bb", "B", "C", "C#", "D", "Eb", "E", "F", "F#", "G2", "G#2", "A2", "Bb2", "B2",
            "C2", "C#2", "D2", "Eb2", "E2", "F2", "F#2", "G3"]
else:
    print("corrupt settings")
    exit("Corrupt settings")

if settings["color_theme"] == "dark":
    color1 = "#151515"
    color2 = "#202020"
    color3 = "#303030"
    color4 = "#353535"
    color5 = "#404040"
    color6 = "#454545"
    color7 = "#353535"
    color8 = "#606060"

    colorText1 = "#999999"
    colorText2 = "#ffffff"

elif settings["color_theme"] == "light":
    color1 = "#ffffff"
    color2 = "#ffffff"
    color3 = "#ffffff"
    color4 = "#ffffff"
    color5 = "#ffffff"
    color6 = "#ffffff"
    color7 = "#bbbbbb"
    color8 = "#909090"

    colorText1 = "#000000"
    colorText2 = "#000000"
else:
    print("corrupt settings")
    exit("Corrupt settings")


class main: # Controlling Class

    def __init__(self):
        self.frame = Tk()
        self.frame.title("Veeh-Harpenator 2.0 (Benjamin Schaab)")
        self.frame.bind("<Configure>", self.configure)
        self.frame.configure(bg=color6)

        #Initial Resolution / Scaling
        self.fx, self.fy = 1000, 500

        #INIT
        self.create_gui_structure()

        self.but_wo = button_worker(self.main_frame.get("create_frame"), 800, 300)
        self.but_wo.activate()

        #START
        self.frame.mainloop()



    def create_gui_structure(self):
        # GUI Structure
        self.main_frame = FRAME("main_frame", self, LEFT, 1000, 500, color6)

        self.main_frame.add_frame("work_frame", LEFT, 800, 500, color6, border=1)

        self.main_frame.get("work_frame").add_frame("create_frame", TOP, 800, 300, color1, border=1)

        self.main_frame.get("work_frame").add_frame("tool_frame", TOP, 800, 50, color3)

        self.main_frame.get("tool_frame").add_frame("link_frame", LEFT, 500, 50, color3, border=1)

        self.main_frame.get("tool_frame").add_frame("current_frame", RIGHT, 300, 50, color2, border=1)

        self.main_frame.get("work_frame").add_frame("bottom_frame", TOP, 800, 200, color4)

        self.main_frame.get("bottom_frame").add_frame("settings_frame", LEFT, 400, 200, color4, border=1)

        self.main_frame.get("bottom_frame").add_frame("info_frame", RIGHT, 400, 200, color3, border=1)

        self.main_frame.add_frame("history_frame", RIGHT, 200, 500, color6, border=1)

        self.main_frame.get("history_frame").add_frame("notes_frame", TOP, 200, 350, color5, border=1)

        self.main_frame.get("history_frame").add_frame("note_tools", TOP, 200, 150, color4, border=1)


    def configure(self, event): # Called when Window changes
        # Resize all Widgets
        sx, sy = self.frame.winfo_width(), self.frame.winfo_height()
        print(sx, sy)


        if sx / self.fx < sy / self.fy:
            factor = sx / self.fx
        else:
            factor = sy / self.fy

        print(factor)
        self.main_frame.resize(factor)
        self.but_wo.resize(factor)


class FRAME: # handles Frame-widgets

    def __init__(self, name, mother, orientation, sx, sy, color, border=False, anchor=None):
        self.name = name
        self.children = {}
        self.mother = mother
        self.sx, self.sy = sx, sy

        self.frame = Frame(mother.frame, height=sy, width=sx, relief=SOLID, bd=border, bg=color)
        self.frame.pack_propagate(0)
        self.frame.pack(side=orientation, anchor=anchor)

    def resize(self, factor): # on window resize
        self.frame.configure(width=int(factor*self.sx), height=int(factor*self.sy))
        for child in self.children.values():
            child.resize(factor)

    def add_frame(self, name, orientation, sx, sy, color, border=False): # creates new FRAME, adds it as child
        obj = FRAME(name, self, orientation, sx, sy, color, border=border)
        self.children.update({name : obj})

    def add_obj(self,obj): # add object to childs
        self.children.update({obj.name : obj})


    def get(self, name): # tree search for name
        if self.name == name:
            return self
        else:
            for child in self.children.values():
                val = child.get(name)
                if val:
                    return val

        return None


class BUTTON:

    def __init__(self, name, mother, orientation, sx, sy, _text, color, method):
        self.name = name
        self.mother = mother
        self.sx = sx
        self.sy = sy

        self.frame = Frame(mother.frame, height=sy, width=sx, bd=0, relief=SOLID, bg=color)
        self.frame.pack_propagate(0)
        self.frame.pack(side=orientation)

        self.button = Button(self.frame, command=method, bd=1, relief=SOLID, bg=color, fg=colorText1, )
        self.button.pack_propagate(0)
        self.button.pack(fill=BOTH, expand=1)
        self.re_text(_text)

    def re_text(self, new_text):
        self.button.configure(text=new_text)

    def resize(self, scale):

        self.frame.configure(height=int(scale*self.sy), width=int(scale*self.sx))


class BLANK:

    def __init__(self, name, mother, orientation, sx, sy):
        self.name = name
        self.mother = mother
        self.sx = sx
        self.sy = sy
        self.canvas = Canvas(mother.frame)
        self.canvas.pack(side=orientation)

    def resize(self, scale):
        self.canvas.configure(height=int(scale*self.sy), width=int(scale*self.sx))


class WORK_FRAME:

    def __init__(self, mother, sx, sy):
        self.sx = sx
        self.sy = sy
        self.frame = Frame(mother.frame,  height=sy, width=sx, bg=color1)
        self.frame.pack_propagate(0)
        self.create_structure()

    def create_structure(self):
        pass

    def resize(self, factor):
        pass

    def activate(self):
        self.frame.pack()

    def deactivate(self):
        self.frame.pack_forget()


class button_worker(WORK_FRAME):

    def create_structure(self):
        self.is_pause = False

        self.main_keys = {}
        self.sec_keys = {}

        self.main_label_frame = FRAME("main_label_frame", self, TOP, 800, 30, color1, anchor=NW)
        self.main_label = Label(self.main_label_frame.frame, fg=colorText1, bg=color1, text="Hauptnote:")
        self.main_label.pack(fill=BOTH, expand=1)

        self.main_key_frame = FRAME("main_key_frame", self, TOP, 800, 30, color1, anchor=None)

        self.sec_label_frame = FRAME("sec_label_frame", self, TOP, 800, 30, color1, anchor=NW)
        self.sec_label = Label(self.sec_label_frame.frame, fg=colorText1, bg=color1, text="Beinote:")
        self.sec_label.pack(fill=BOTH, expand=1)

        self.sec_key_frame = FRAME("main_sec_frame", self, TOP, 800, 30, color1)


        def temp(value):
            self.main_key_callback(value)

        for i in range(len(keys)):
            key = keys[i]
            button = BUTTON("main_"+key, self.main_key_frame, LEFT, 30, 30, key, color7, partial(temp, value=key))
            self.main_key_frame.add_obj(button)
            self.main_keys.update({key : button})

        self.pause_button = BUTTON("pause_button", self.main_key_frame, LEFT, 50, 30, "Note", color8, self.pause_button_callback)
        self.main_key_frame.add_obj(self.pause_button)


        def temp(value):
            self.sec_key_callback(value)

        for i in range(len(keys)):
            key = keys[i]
            button = BUTTON("sec_"+key, self.sec_key_frame, LEFT, 30, 30, key, color7, partial(temp, value=key))
            self.sec_key_frame.add_obj(button)
            self.sec_keys.update({key : button})


    def main_key_callback(self, value):
        print("MAIN", value)


    def sec_key_callback(self, value):
        print("SEC", value)


    def pause_button_callback(self):
        self.is_pause = not self.is_pause



    def resize(self, factor):
        self.frame.configure(width=int(factor*self.sx), height=int(factor*self.sy))

        for item in self.main_key_frame, self.main_label_frame, self.sec_key_frame, self.sec_label_frame:
            item.resize(factor)



if __name__ == '__main__':
    MAIN = main()