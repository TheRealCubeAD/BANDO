from pystray import MenuItem as item
import pystray
from PIL import Image
import threading

class Icon:
    def __init__(self, image_path, on_action, off_action, exit_action):
        image = Image.open(image_path)
        menu = (item('Override ON', on_action), item('Override OFF', off_action), item('Exit', exit_action))
        self.icon = pystray.Icon("MeetDetector", icon=image, menu=menu)
        self.icon.title = "DISCONNECTED"
        self.thread = threading.Thread(target=self.icon.run, name="Icon")
        self.thread.daemon = True
        self.thread.start()

    def change(self, image_path, title):
        image = Image.open(image_path)
        self.icon.icon = image
        self.icon.title = title

    def stop(self):
        self.icon.stop()