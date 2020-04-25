import tkinter
class VIEW:
    main_frame = None

    transfer_frame = None
    transfer_drone_frame = None
    transfer_storage_frame = None
    transfer_middle_frame = None
    drone_label = None
    storage_label = None

    tags_frame = None

    white = "#ffffff"
    black = "#000000"

    def __init__(self):
        # main_frame
        self.main_frame = tkinter.Tk()
        self.main_frame.title("Quax Manager 2")
        self.main_frame.configure(bg=self.black)

        ## main_frame - transfer_frame
        self.transfer_frame = tkinter.Frame(self.main_frame, bg=self.black)
        self.transfer_frame.grid(row=0)
        ### main_frame - transfer_frame - left
        self.transfer_drone_frame = tkinter.Frame(self.transfer_frame, bg=self.black)
        self.transfer_drone_frame.grid(column=0)
        #### main_frame - transfer_frame - left - label
        self.drone_label = tkinter.Label(self.transfer_drone_frame,text="DRONE",bg=self.black)
        self.drone_label.grid(row=0)
        ### main_frame - transfer_frame - middle
        self.transfer_middle_frame = tkinter.Frame(self.transfer_frame)
        self.transfer_middle_frame.grid(column=1)
        ### main_frame - transfer_frame - right
        self.transfer_storage_frame = tkinter.Frame(self.transfer_frame)
        self.transfer_storage_frame.grid(column=2)
        #### main_frame - transfer_frame - right - label
        self.storage_label = tkinter.Label(self.transfer_storage_frame,text="STORAGE",bg=self.black)
        self.storage_label.grid(row=0)

        self.tags_frame = tkinter.Frame(self.main_frame)
        self.tags_frame.grid(row=1)

        self.main_frame.mainloop()


v = VIEW()