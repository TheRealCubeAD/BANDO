import matplotlib.pyplot as plt
import numpy as np
import time
import threading




class DATA:

    def __init__(self):
        plt.ion()
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111)
        self.line1, = self.ax.plot(0, 0, 'r-', color="red")
        self.line2, = self.ax.plot(0, 0, 'r-', color="blue")
        self.t_data = []
        self.h_data = []

    def add(self, t, h):
        self.t_data.append(t)
        self.line1.set_xdata([i for i in range(len(self.t_data))])
        self.line1.set_ydata(self.t_data)
        plt.xlim([0, len(self.t_data)])
        plt.ylim([0, max(self.t_data + self.h_data)])

        self.h_data.append(h)
        self.line2.set_xdata([i for i in range(len(self.h_data))])
        self.line2.set_ydata(self.h_data)
        self.fig.canvas.draw()
        self.fig.canvas.flush_events()





d = DATA()
yy = [1,2,3,5,2,1]

for x, y in enumerate(yy):
    d.add(y, y*2)
    time.sleep(1)