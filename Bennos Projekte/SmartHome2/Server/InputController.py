import Device_init_list

class INPCON:
    def __init__(self, controller):
        self.main_controller = controller
        self.devices = []
        self.input_queue = QUEUE()
        self.occupied = False
        for device in Device_init_list.INPUT_DEVICES:
            print(device)
            self.add_device(device(self.add_event))



    def add_device(self, device):
        self.devices.append(device)


    def add_event(self, event):
        if not self.occupied:
            self.occupied = True
            print("sending event...")
            self.main_controller.new_input_event(event)
        else:
            print("adding event to queue")
            if event.is_prio_high():
                self.input_queue.add_front(event)
            else:
                self.input_queue.add(event)


    def activate(self):
        for device in self.devices:
            device.activate()

    def deactivate(self):
        for device in self.devices:
            device.deactivate()


    def signal_finished(self):
        if not self.input_queue.is_empty():
            print("sending event")
            self.main_controller.new_input_event(self.input_queue.pop())
        else:
            self.occupied = False


class QUEUE:
    def __init__(self):
        self.queue = []

    def add(self, item):
        self.queue.append(item)

    def add_front(self, item):
        self.queue.insert(0, item)

    def pop(self):
        return self.queue.pop(0)

    def clear(self):
        self.queue.clear()

    def __len__(self):
        return len(self.queue)

    def is_empty(self):
        return  len(self) == 0



if __name__ == '__main__':
    q = QUEUE()
    q.add(1)
    q.add(2)
    q.add_front(3)
    q.pop()
    q.pop()