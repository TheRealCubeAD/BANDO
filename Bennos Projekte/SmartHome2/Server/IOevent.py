

EVENT_IN = 0
EVENT_OUT = 1
PRIO_LOW = 0
PRIO_HIGH = 1

class EVENT:
    def __init__(self, type):
        self.type = type
        self.priority = PRIO_LOW
        self.device = None
        self.message = None

    def set_prio_high(self):
        self.priority = PRIO_HIGH

    def set_device(self, device):
        self.device = device

    def set_message(self, message):
        self.message = message

    def get_device(self):
        return self.device

    def get_message(self):
        return self.message

    def is_prio_high(self):
        return self.priority == PRIO_HIGH



class INPUT_EVENT(EVENT):
    def __init__(self):
        super().__init__(EVENT_IN)

class OUTPUT_EVENT(EVENT):
    def __init__(self):
        super().__init__(EVENT_OUT)

