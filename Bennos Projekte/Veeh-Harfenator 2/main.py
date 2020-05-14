from tkinter import *
from functools import partial
import color_themes, languages

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
# TODO: piano_creator
# TODO: veeh_creator



settings = {
    "language" : "english",
    "color_theme" : "dark"
}

def load_settings():
    global color
    global text
    global keys

    color = color_themes.load_theme(settings["color_theme"])

    text = languages.load_language(settings["language"])
    keys = text.keys


class main: # Controlling Class

    # For main:

    def __init__(self):
        self.frame = Tk()
        self.frame.title("Veeh-Harpenator 2.0 (Benjamin Schaab)")
        self.frame.configure(bg=color.surface_6)
        self.frame.bind("<Configure>", self.configure)

        #Variables
        self.current_note = [None, None, None, False, False, 0] #[main_note, sec_note, lenght, is_point, is_pause, link]

        #Initial resolution for scaling
        self.fx, self.fy = 1000, 500

        #INIT
        self.create_gui_structure()

        self.but_wo = button_worker(self.main_frame.get("create_frame"), 800, 300, self.get_update, self.get_add)
        self.but_wo.activate()

        #START
        self.frame.mainloop()



    def create_gui_structure(self):
        # GUI Structure
        self.main_frame = FRAME("main_frame", self, LEFT, 1000, 500, color.surface_6)

        self.main_frame.add_frame("work_frame", LEFT, 800, 500, color.surface_6, border=1)

        self.main_frame.get("work_frame").add_frame("create_frame", TOP, 800, 300, color.surface_1, border=1)

        self.main_frame.get("work_frame").add_frame("tool_frame", TOP, 800, 50, color.surface_3)

        self.main_frame.get("tool_frame").add_frame("link_frame", LEFT, 500, 50, color.surface_3, border=1)

        self.main_frame.get("tool_frame").add_frame("current_frame", RIGHT, 300, 50, color.surface_3, border=1)

        self.current_label = LABEL("current_label", self.main_frame.get("current_frame"), LEFT, 300, 50, "",
                                   color.color_text_low, color.surface_3)
        self.main_frame.get("current_frame").add_obj(self.current_label)

        self.main_frame.get("work_frame").add_frame("bottom_frame", TOP, 800, 200, color.surface_4)

        self.main_frame.get("bottom_frame").add_frame("settings_frame", LEFT, 400, 200, color.surface_4, border=1)

        self.main_frame.get("bottom_frame").add_frame("info_frame", RIGHT, 400, 200, color.surface_3, border=1)

        self.main_frame.add_frame("history_frame", RIGHT, 200, 500, color.surface_6, border=1)

        self.main_frame.get("history_frame").add_frame("notes_frame", TOP, 200, 350, color.surface_5, border=1)

        self.main_frame.get("history_frame").add_frame("note_tools", TOP, 200, 150, color.surface_4, border=1)


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


    def verify_note(self, note):
        if note[0] == None:
            return False
        if note[2] == None:
            return False
        return True


    def note_to_text(self, note, simple=False):
        if not simple:
            final = ""
            if note[4] == False:
                final += text.pause_but_note
            else:
                final += text.pause_but_pause + " "
                if note[0] != None:
                    final += text.text_at

            if note[0] != None:
                final += " " + keys[note[0]]
            else:
                if note[1] != None:
                    final += " ?"

            if note[1] != None:
                final += " " + text.text_with + " " + keys[note[1]]

            if note[2] != None:
                final += " " + text.text_of_lenght + " 1/" + str(note[2])
                if note[3]:
                    final += "."
        return final

    # For Crator:

    def get_update(self, note):
        for i in range(len(note)):
            self.current_note[i] = note[i]
        self.current_label.re_text(self.note_to_text(note))
        if self.verify_note(note):
            self.current_label.re_color(color.color_text_high)
        else:
            self.current_label.re_color(color.color_text_low)


    def get_add(self):
        if self.verify_note(self.current_note):
            return True
        else:
            return False





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

    def get_all(self):
        return self.children


class BUTTON:

    def __init__(self, name, mother, orientation, sx, sy, _text, _color, method):
        self.color = _color
        self.name = name
        self.mother = mother
        self.sx = sx
        self.sy = sy

        self.frame = Frame(mother.frame, height=sy, width=sx, bd=0, relief=SOLID, bg=_color)
        self.frame.pack_propagate(0)
        self.frame.pack(side=orientation)

        self.button = Button(self.frame, command=method, bd=1, relief=SOLID, bg=_color, fg=color.color_text_low, activebackground=color.color_click)
        self.button.pack_propagate(0)
        self.button.pack(fill=BOTH, expand=1)
        self.re_text(_text)


    def re_text(self, new_text):
        self.button.configure(text=new_text)


    def resize(self, scale):
        self.frame.configure(height=int(scale*self.sy), width=int(scale*self.sx))


    def activate(self):
        self.button.configure(bg=color.color_active)


    def deactivate(self):
        self.button.configure(bg=self.color)


    def get(self, name):
        if self.name == name:
            return self
        else:
            return None


class LABEL:

    def __init__(self, name, mother, orientation, sx, sy, _text, color_fg, color_bg):
        self.name = name
        self.mother = mother
        self.sx = sx
        self.sy = sy

        self.frame = Frame(mother.frame, height=sy, width=sx, bd=0, relief=SOLID, bg=color_bg)
        self.frame.pack_propagate(0)
        self.frame.pack(side=orientation)

        self.label = Label(self.frame, bd=0, bg=color_bg, fg=color_fg)
        self.label.pack_propagate(0)
        self.label.pack(fill=BOTH, expand=1)
        self.re_text(_text)

    def re_text(self, new_text):
        self.label.configure(text=new_text)

    def resize(self, scale):
        self.frame.configure(height=int(scale * self.sy), width=int(scale * self.sx))

    def re_color(self, _color):
        self.label.configure(fg=_color)

    def get(self, name):
        if self.name == name:
            return self
        else:
            return None


class WORK_FRAME:

    def __init__(self, mother, sx, sy, update_methode, add_methode):
        self.note = [None, None, None, False, False] #  [main_note, sec_note, lenght, is_point, is_pause]
        self.update = update_methode
        self.add = add_methode
        self.sx = sx
        self.sy = sy
        self.children = {}
        self.frame = Frame(mother.frame,  height=sy, width=sx, bg=color.surface_1)
        self.frame.pack_propagate(0)
        self.create_structure()


    def create_structure(self):
        pass


    def resize(self, factor):
        self.frame.configure(width=int(factor * self.sx), height=int(factor * self.sy))
        for item in self.children.values():
            item.resize(factor)


    def activate(self):
        self.frame.pack()


    def deactivate(self):
        self.frame.pack_forget()


class button_worker(WORK_FRAME):

    def create_structure(self):
        self.main_keys = {}
        self.sec_keys = {}

        main_label = LABEL("main_key_labal", self, TOP, 800, 30, text.label_main_note, color.color_text_low, color.surface_1)
        self.children.update({"main_key_label" : main_label})

        self.main_key_frame = FRAME("main_key_frame", self, TOP, 800, 30, color.surface_1, anchor=None)
        self.children.update({"main_key_frame" : self.main_key_frame})

        sec_label = LABEL("sec_key_label", self, TOP, 800, 30, text.label_sec_note, color.color_text_low, color.surface_1)
        self.children.update({"sec_key_label" : sec_label})

        self.sec_key_frame = FRAME("main_sec_frame", self, TOP, 800, 30, color.surface_1)
        self.children.update({"sec_key_frame" : self.sec_key_frame})

        self.blank_frame = FRAME("blank_frame", self, TOP, 800, 60, color.surface_1)
        self.lenght_label_frame = FRAME("lenght_label_frame", self, TOP, 800, 30, color.surface_1)

        lenght_label = LABEL("lenght_label", self.lenght_label_frame, LEFT, 100, 30, text.label_lenght_note, color.color_text_low, color.surface_1)
        self.children.update({"blank_frame": self.blank_frame})
        self.children.update({"lenght_label_frame" : self.lenght_label_frame})

        self.lenght_key_frame = FRAME("lenght_key_frame", self, TOP, 800, 30, color.surface_1)
        self.children.update({"lenght_key_frame" : self.lenght_key_frame})


        def temp(value):
            self.main_key_callback(value)

        for i in range(len(keys)):
            key = keys[i]
            button = BUTTON("main_"+key, self.main_key_frame, LEFT, 30, 30, key, color.surface_7, partial(temp, value=i))
            self.main_key_frame.add_obj(button)
            self.main_keys.update({key : button})

        self.pause_button = BUTTON("pause_button", self.main_key_frame, LEFT, 50, 30, text.pause_but_note, color.surface_8,
                                   self.pause_button_callback)
        self.main_key_frame.add_obj(self.pause_button)


        def temp(value):
            self.sec_key_callback(value)

        for i in range(len(keys)):
            key = keys[i]
            button = BUTTON("sec_"+key, self.sec_key_frame, LEFT, 30, 30, key, color.surface_7, partial(temp, value=i))
            self.sec_key_frame.add_obj(button)
            self.sec_keys.update({key : button})

        self.no_sec_button = BUTTON("noe_sec_button", self.sec_key_frame, LEFT, 50, 30, text.no_sec_but, color.surface_7,
                                   partial(temp, value=None))
        self.sec_key_frame.add_obj(self.no_sec_button)
        self.no_sec_button.activate()

        def temp(value):
            self.lenght_callback(value)

        self.lenght_key_frame.add_obj(BUTTON("lenght_1", self.lenght_key_frame, LEFT, 30, 30, "1/1", color.surface_7,
                                                        partial(temp, value=1)))
        self.lenght_key_frame.add_obj( BUTTON("lenght_2", self.lenght_key_frame, LEFT, 30, 30, "1/2", color.surface_7,
                                                         partial(temp, value=2)))
        self.lenght_key_frame.add_obj(BUTTON("lenght_4", self.lenght_key_frame, LEFT, 30, 30, "1/4", color.surface_7,
                                                         partial(temp, value=4)))
        self.lenght_key_frame.add_obj(BUTTON("lenght_8", self.lenght_key_frame, LEFT, 30, 30, "1/8", color.surface_7,
                                                         partial(temp, value=8)))
        self.lenght_key_frame.add_obj(FRAME("blank_button", self.lenght_key_frame, LEFT, 30, 30, color.surface_1))

        self.lenght_key_frame.add_obj(BUTTON("lenght_.", self.lenght_key_frame, LEFT, 30, 30, ".", color.surface_7,
                                                         partial(temp, value=0)))

        self.add_button = BUTTON("add_button", self, RIGHT, 120, 60, text.add_but, color.surface_7, self.add_button_callback)
        self.children.update({"add_button" : self.add_button})


    def lenght_callback(self, value):
        if value == 0:
            self.note[3] = not self.note[3]
            if self.note[3]:
                self.lenght_key_frame.get("lenght_.").activate()
            else:
                self.lenght_key_frame.get("lenght_.").deactivate()
        else:
            self.lenght_key_frame.get("lenght_1").deactivate()
            self.lenght_key_frame.get("lenght_2").deactivate()
            self.lenght_key_frame.get("lenght_4").deactivate()
            self.lenght_key_frame.get("lenght_8").deactivate()

            self.lenght_key_frame.get("lenght_"+str(value)).activate()
            self.note[2] = value
        self.push_update()


    def main_key_callback(self, value):
        self.note[0] = value
        for button in self.main_key_frame.get_all().values():
            button.deactivate()
        self.main_key_frame.get("main_"+keys[value]).activate()
        self.push_update()


    def sec_key_callback(self, value):
        self.note[1] = value
        for button in self.sec_key_frame.get_all().values():
            button.deactivate()
        if value == None:
            self.no_sec_button.activate()
        else:
            self.sec_key_frame.get("sec_" + keys[value]).activate()
        self.push_update()


    def pause_button_callback(self):
        self.note[4] = not self.note[4]
        if self.note[4]:
            self.pause_button.re_text(text.pause_but_pause)
        else:
            self.pause_button.re_text(text.pause_but_note)
        self.push_update()


    def add_button_callback(self):
        if self.add():
            self.reset()
            self.push_update()


    def push_update(self):
        if self.update(self.note):
            self.reset()



    def reset(self):
        for element in self.main_key_frame.get_all().values():
            element.deactivate()
        for element in self.sec_key_frame.get_all().values():
            element.deactivate()
        self.lenght_key_frame.get("lenght_1").deactivate()
        self.lenght_key_frame.get("lenght_2").deactivate()
        self.lenght_key_frame.get("lenght_4").deactivate()
        self.lenght_key_frame.get("lenght_8").deactivate()
        self.lenght_key_frame.get("lenght_.").deactivate()
        self.pause_button.re_text(text.pause_but_note)
        self.no_sec_button.activate()
        self.note = [None, None, None, False, False]



if __name__ == '__main__':
    load_settings()
    MAIN = main()