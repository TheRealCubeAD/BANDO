import os
import filecmp
import string
import time
import shutil
import datetime
import threading


IMAGE = 123
VIDEO = 789

IMAGE_ENDINGS = set(("png","dng","jpg","jpeg"))
VIDEO_ENDINGS = set(("avi","mp4","mpeg"))

IDENT_FILE = "IDENT.config"

INTERNAL = "itd"
EXTERNAL = "etd"
STORAGE = "stc"


def INTERRUPT(cause=None):
    print(cause)
    input()
    pass


class DATE:

    def __init__(self, year, month, day, from_file=None, folder=False):
        if from_file:
            if not folder:
                file_date = os.path.getctime(from_file)
                file_date = str(datetime.datetime.fromtimestamp(file_date))
                file_date = file_date.split()[0].split("-")
                self.year = int(file_date[0])
                self.month = int(file_date[1])
                self.day = int(file_date[2])
            else:
                self.year, self.month, self.day = from_file.split(".")
                self.year = int(self.year) + 2000
                self.month = int(self.month)
                self.day = int(self.day)
        else:
            self.year = year
            self.month = month
            self.day = day

        if type(self.year) != int or type(self.month) != int or type(self.day) != int:
            raise TypeError("date-component must be int")
        if self.month not in range(1, 13) or self.day not in range(1, 32):
            raise AttributeError("invalid date")



    def __eq__(self, other):
        return self.year == other.year and self.month == other.month and self.day == other.day


    def __hash__(self):
        return hash(self.to_string())


    def duplicate(self):
        return DATE(self.year, self.month, self.day)


    def to_string(self):
        s_day = str(self.day)
        s_month = str(self.month)
        s_year = str(self.year)

        if len(s_day) < 2:
            s_day = "0" + s_day
        if len(s_month) < 2:
            s_month = "0" + s_month
        s_year = s_year[2:]

        return s_year + "." + s_month + "." + s_day


    def __str__(self):
        s_day = str(self.day)
        s_month = str(self.month)
        s_year = str(self.year)

        if len(s_day) < 2:
            s_day = "0" + s_day
        if len(s_month) < 2:
            s_month = "0" + s_month
        s_year = s_year[2:]

        return s_day + "." + s_month + "." + s_year


class FILE:

    def __init__(self, path, name=None, ending=None, should_exist=False):
        self.date = None
        path = path.replace("\\", "/")
        self.path = ""
        if name:
            if ending:
                self.ending = ending
                self.name = name
            else:
                self.name, self.ending = name.split(".")
            self.path = path
            if self.path[-1] != "/":
                self.path += "/"
        else:
            parts = path.rstrip("/").split("/")
            self.name, self.ending = parts.pop().split(".")
            for part in parts:
                self.path += part + "/"

        if self.ending.lower() in IMAGE_ENDINGS:
            self.type = IMAGE
        elif self.ending.lower() in VIDEO_ENDINGS:
            self.type = VIDEO
        else:
            print("WARNING: Unknown File-type: " + self.ending)
            self.type = None

        self.should_exist = should_exist
        if self.should_exist:
            self.load_date()


    def get_full_path(self):
        return self.path + self.name + "." + self.ending


    def check_exsitance(self):
        if self.should_exist:
            while 1:
                if self.is_existing():
                    return True
                else:
                    INTERRUPT("missing_file")
        else:
            return self.is_existing()


    def is_existing(self):
        return os.path.exists(self.get_full_path())


    def load_date(self):
        self.check_exsitance()
        try:
            self.date = DATE(0, 0, 0, from_file=self.get_full_path())
        except:
            self.date = None
            print("ERROR while loading file-date")


    def get_size(self):
        self.check_exsitance()
        try:
            return os.path.getsize(self.get_full_path())
        except:
            print("WARNING: file_size_error")
            return 1


    def copy(self, destination):
        full_destination = destination + self.name + "." + self.ending
        while 1:
            try:
                self.check_exsitance()
                if shutil.copy2(self.get_full_path(), full_destination) != full_destination:
                    raise NameError
                if not filecmp.cmp(self.get_full_path(), full_destination, shallow=False):
                    raise FileNotFoundError
                return
            except:
                INTERRUPT("file_copy")
                while 1:
                    if not os.path.exists(destination):
                        INTERRUPT("folder_missing")
                        continue
                    if os.path.exists(full_destination):
                        try:
                            os.remove(full_destination)
                            if not os.path.exists(full_destination):
                                return
                            print("WARNING: File could not be deleted")
                        except:
                            INTERRUPT("file_deletion")



class FOLDER:
    IMAGES_PATH = "Images/"
    VIDEOS_PATH = "Videos/"

    def __init__(self, path, name=None):
        path = path.replace("\\", "/")
        self.path = ""
        if name:
            self.path = path.rstrip()
            if self.path[-1] != "/":
                self.path += "/"
            self.name = name
        else:
            parts = path.split("/")
            self.name = parts.pop()
            for part in parts:
                self.path += part + "/"
        self.date = DATE(0, 0, 0, from_file=self.name, folder=True)


    def get_full_path(self):
        return self.path + self.name + "/"


    def create(self):
        while 1:
            try:
                if not os.path.exists(self.get_full_path()):
                    os.mkdir(self.get_full_path())
                    if not os.path.exists(self.get_full_path()):
                        raise FileNotFoundError
                if not os.path.exists(self.get_full_path() + self.IMAGES_PATH):
                    os.mkdir(self.get_full_path() + self.IMAGES_PATH)
                    if not os.path.exists(self.get_full_path() + self.IMAGES_PATH):
                        raise FileNotFoundError
                if not os.path.exists(self.get_full_path() + self.VIDEOS_PATH):
                    os.mkdir(self.get_full_path() + self.VIDEOS_PATH)
                    if not os.path.exists(self.get_full_path() + self.VIDEOS_PATH):
                        raise FileNotFoundError
                return

            except:
                INTERRUPT("folder_creation")


    def copy_file(self, file):
        full_path = self.get_full_path()
        if file.type == IMAGE:
            full_path += self.IMAGES_PATH
        else:
            full_path += self.VIDEOS_PATH
        file.copy(full_path)


    def does_exist(self, file):
        full_path = self.get_full_path()
        if file.type == IMAGE:
            full_path += self.IMAGES_PATH
        else:
            full_path += self.VIDEOS_PATH

        while 1:
            if os.path.exists(self.get_full_path()):
                break
            else:
                INTERRUPT("folder_missing")
        return os.path.exists(full_path + file.name + "." + file.ending)


    def __eq__(self, other):
        return self.get_full_path() == other.get_full_path()


class SOURCE:

    def __init__(self, type):
        self.active = False
        self.path = None
        self.type = type
        self.files = []
        self.searching = True
        self.search_thread = threading.Thread(target=self.search_path)
        self.search_thread.daemon = True
        self.search_thread.start()


    def search_path(self):
        while self.searching:
            available_drives = [drive + ":/" for drive in string.ascii_uppercase if os.path.exists(drive + ":")]
            for drive in available_drives:
                if os.path.exists(drive + IDENT_FILE):
                    with open(drive + IDENT_FILE, "r") as info:
                        lines = info.readlines()
                        print(lines)
                        if len(lines) < 2:
                            print("WARNING: invalid config file")
                            continue
                        if lines[0].rstrip() == self.type:
                            self.path = drive + lines[1].rstrip()
                            self.search_files()
                            self.active = True
                            print(self.type, "found")
                            return True
            time.sleep(1)


    def search_files(self):
        for folder in os.listdir(self.path):
            if "media" in folder.lower():
                sub_path = self.path + folder + "/"
                for file_name in os.listdir(sub_path):
                    self.check_existance()
                    file = FILE(sub_path, name=file_name, should_exist=True)
                    if file.type:
                        self.files.append(file)


    def get_dates(self):
        all_dates = set()
        for file in self.files:
            all_dates.add(file.date)
        return all_dates


    def stop_searching(self):
        self.searching = False


    def check_existance(self):
        while 1:
            if os.path.exists(self.path):
                return True
            else:
                INTERRUPT(self.type+"_missing")


class DESTINATION:

    def __init__(self):
        self.path = None
        self.folders = []
        self.active = False
        self.search_thread = threading.Thread(target=self.search_path)
        self.search_thread.daemon = True
        self.search_thread.start()


    def search_path(self):
        while 1:
            available_drives = [drive + ":/" for drive in string.ascii_uppercase if os.path.exists(drive + ":")]
            for drive in available_drives:
                if os.path.exists(drive + IDENT_FILE):
                    with open(drive + IDENT_FILE, "r") as info:
                        lines = info.readlines()
                        print(lines)
                        if len(lines) < 2:
                            print("WARNING: invalid config file")
                            continue
                        if lines[0].rstrip() == STORAGE:
                            self.path = drive + lines[1].rstrip()
                            self.search_folders()
                            self.active = True
                            print("dest found")
                            return True
            time.sleep(1)


    def search_folders(self):
        self.check_existance()
        for folder_name in os.listdir(self.path):
            try:
                folder = FOLDER(self.path, name=folder_name)
                self.folders.append(folder)
            except:
                print("Invalid Folder: " + folder_name)


    def get_dates(self):
        all_dates = set()
        for folder in self.folders:
            all_dates.add(folder.date)
        return all_dates


    def check_existance(self):
        while 1:
            if os.path.exists(self.path):
                return True
            else:
                INTERRUPT(STORAGE+"_missing")


    def create_folders(self, dates):
        self.check_existance()
        for date in dates:
            self.check_existance()
            new_folder = FOLDER(self.path, name=date.to_string())
            new_folder.create()
            self.folders.append(new_folder)


    def copy_file(self, file):
        for folder in self.folders:
            if folder.date == file.date:
                folder.copy_file(file)
                return True
        print("WARNING: Date not Found")


    def does_exist(self, file):
        for folder in self.folders:
            if folder.date == file.date:
                return folder.does_exist(file)
        print("WARNING: Date not Found")
        return False


class CONTROL:

    def __init__(self):
        self.source_internal = SOURCE(INTERNAL)
        self.source_external = SOURCE(EXTERNAL)
        self.destination = DESTINATION()


    def start_transfer(self):
        if not (self.source_external.active or self.source_internal.active) or not self.destination.active:
            print("System not ready yet!")
            return False
        self.source_external.stop_searching()
        self.source_internal.stop_searching()
        to_create_dates = self.source_internal.get_dates()
        to_create_dates = to_create_dates.union(self.source_external.get_dates())
        to_create_dates.difference(self.destination.get_dates())
        self.destination.create_folders(to_create_dates)
        all_files = self.source_internal.files + self.source_external.files
        to_copy = [file for file in all_files if not self.destination.does_exist(file)]
        all_space = sum([file.get_size() for file in to_copy])
        print("Copying " + str(all_space) + " Byte in " + str(len(to_copy)) + " Files")
        for file in to_copy:
            print("    Copying " + file.name + " ...")
            self.destination.copy_file(file)

        print("Finished!")
        return True




def test(cause):
    input(">>>")


c = CONTROL()
while 1:
    time.sleep(1)
    input()
    if c.start_transfer():
        break

