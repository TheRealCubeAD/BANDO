from tkinter import *
from functools import partial

keys = ["G", "G#", "A", "Bb", "B", "C", "C#", "D", "Eb", "E", "F", "F#", "G2", "G#2", "A2", "Bb2", "B2", "C2", "C#2",
         "D2", "Eb2", "E2", "F2", "F#2", "G3"]

class main:

    def __init__(self):
        self.frame = Tk()
        self.frame.title("Veeh-Harpenator 2.0 (Benjamin Schaab)")

        self.fx, self.fy = 2500, 100


        self.create_gui_structure()

        self.but_wo = button_worker(self.main_frame.get("create_frame"), 2500, 100)
        self.but_wo.activate()

       #self.main_frame.resize(1)

        self.frame.bind("<Configure>", self.configure)

        self.frame.mainloop()



    def create_gui_structure(self):
        # GUI Structure
        self.main_frame = FRAME("main_frame", self, 0, 0, 2500, 100)

        self.main_frame.add_frame("work_frame", 0, 0, 2500, 100)

        self.main_frame.get("work_frame").add_frame("create_frame", 0, 0, 2500, 100)

        self.main_frame.get("work_frame").add_frame("tool_frame", 1, 0, 0, 0)

        self.main_frame.get("tool_frame").add_frame("link_frame", 0, 0, 0, 0)

        self.main_frame.get("tool_frame").add_frame("current_frame", 0, 1, 0, 0)

        self.main_frame.get("work_frame").add_frame("bottom_frame", 2, 0, 0, 0)

        self.main_frame.get("bottom_frame").add_frame("settings_frame", 0, 0, 0, 0)

        self.main_frame.get("bottom_frame").add_frame("info_frame", 0, 1, 0, 0)

        self.main_frame.add_frame("history_frame", 0, 1, 0, 0)

        self.main_frame.get("history_frame").add_frame("notes_frame", 0, 0, 0, 0)

        self.main_frame.get("history_frame").add_frame("note_tools", 1, 0, 0, 0)




    def configure(self, event):
        sx, sy = self.frame.winfo_width(), self.frame.winfo_height()
        print(sx, sy)


        if sx / self.fx < sy / self.fy:
            factor = sx / self.fx
        else:
            factor = sy / self.fy

        print(factor)
        self.main_frame.resize(factor)
        self.but_wo.resize(factor)


class FRAME:

    def __init__(self, name, mother, _row, _column, sx, sy):
        self.name = name
        self.children = {}
        self.mother = mother
        self.sx, self.sy = sx, sy

        self.frame = Frame(mother.frame, height=sy, width=sx)
        self.frame.grid_propagate(0)
        self.frame.grid(row=_row, column=_column)


    def resize(self, factor):
        self.frame.configure(width=int(factor*self.sx), height=int(factor*self.sy))
        for child in self.children.values():
            child.resize(factor)


    def add_frame(self, name, _row, _column, sx, sy):
        obj = FRAME(name, self, _row, _column, sx, sy)
        self.children.update({name : obj})


    def add_obj(self,obj):
        self.children.update({obj.name : obj})


    def get(self, name):
        if self.name == name:
            return self
        else:
            for child in self.children.values():
                val = child.get(name)
                if val:
                    return val

        return None


class BUTTON:

    def __init__(self, name, mother, _row, _column, sx, sy, _text, color, method):
        self.name = name
        self.mother = mother
        self.sx = sx
        self.sy = sy
        self.frame = Frame(mother.frame, height=sy, width=sx, borderwidth=1, relief=SOLID)
        self.frame.grid_propagate(0)
        self.frame.grid(row=_row, column=_column)

        self.button = Button(self.frame, command=method, bd=1)
        self.button.grid(sticky='nsew')
        self.re_text(_text)


    def re_text(self, new_text):
        self.button.configure(text=new_text)

    def resize(self, scale):

        self.frame.configure(height=int(scale*self.sy), width=int(scale*self.sx))


class BLANK:

    def __init__(self, name, mother, _row, _column, sx, sy):
        self.name = name
        self.mother = mother
        self.sx = sx
        self.sy = sy
        self.canvas = Canvas(mother.frame)
        self.canvas.grid(row=_row, column=_column)

    def resize(self, scale):
        self.canvas.configure(height=int(scale*self.sy), width=int(scale*self.sx))


class WORK_FRAME:

    def __init__(self, mother, sx, sy):
        self.sx = sx
        self.sy = sy
        self.frame = Frame(mother.frame,  height=sy, width=sx)
        self.frame.grid_propagate(0)
        self.create_structure()

    def create_structure(self):
        pass

    def resize(self, factor):
        pass

    def activate(self):
        self.frame.grid()

    def deactivate(self):
        self.frame.grid_forget()


class button_worker(WORK_FRAME):

    def create_structure(self):
        self.main_keys = {}
        self.sec_keys = {}

        self.main_button_frame = Frame(self.frame)

        def temp(value):
            self.main_key_callback(value)

        for i in range(len(keys)):
            key = keys[i]
            button = BUTTON("main_"+key, self, 0, i, 100, 100, key, "grey", partial(temp, value=key))
            self.main_keys.update({key : button})

    def main_key_callback(self, value):
        print(value)

    def resize(self, factor):
        self.frame.configure(width=int(factor*self.sx), height=int(factor*self.sy))
        for button in self.main_keys.values():
            button.resize(factor)



if __name__ == '__main__':
    MAIN = main()