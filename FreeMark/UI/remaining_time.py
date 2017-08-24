from tkinter import *
import time
import threading

from FreeMark.tools.pacer import Pacer


class RemainingTime(Frame):
    def __init__(self, master=None):
        """
        GUI element displaying remaining time for a process,
        resembles tkinter's progress bar
        :param master: Parent frame
        """
        super().__init__(master)

        # Required GUI elements
        self.remaining_time = IntVar()
        self.description = Label(self, text="Time remaining:")
        self.time_label = Label(self, textvariable=self.remaining_time)
        self.unit_label = Label(self, text="s")
        self.show()

        self.pacer = Pacer()

    def set_max(self, _max):
        """
        Set the amount of steps expected in the process.
        :param _max: int steps expected
        """
        self.pacer.set_max(_max)

    def start(self):
        """
        Show the element and start the timer
        """
        self.pacer.start()
        self.remaining_time.set(0)  # Set it to 0 till we have the first step
        threading.Thread(target=self._updater).start()

    def step(self):
        """
        Take a step, adds one to progress.
        """
        self.pacer.step()

    def update(self):
        """
        Update the remaining_time variable, and the label along with it.
        :return:
        """
        self.remaining_time.set(round(self.pacer.get_estimated_remaining()))

    def _updater(self):
        """
        Thread which updates the remaining time variable every half second,
        which keeps the label up to date.
        """
        while self.pacer.running:
            self.update()
            time.sleep(0.5)

    def stop(self):
        """
        Manually stop the pacer
        """
        self.pacer.reset()
        self.remaining_time.set(0)

    def hide(self):
        """
        Hide GUI elements
        """
        for child in self.winfo_children():
            child.grid_forget()

    def show(self):
        """
        Show GUI elements
        """
        self.description.grid(column=0, row=0)
        self.time_label.grid(column=1, row=0)
        self.unit_label.grid(column=2, row=0)
