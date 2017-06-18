from tkinter import *
from tkinter import filedialog


class OutputSelector(Frame):
    """Class for selecting output destination an generating paths"""
    def __init__(self, master=None):
        super().__init__(master)

        self.output_dir = StringVar()
        self.output_dir.set("Choose output folder")
        self.create_widgets()

    def create_widgets(self):
        Label(self, text="Output options").pack()
        Entry(self, width=50,
              textvariable=self.output_dir).pack(side=LEFT)
        Button(self, text="Choose folder",
               command=self.choose_dir).pack(side=LEFT, padx=10)

    def choose_dir(self):
        self.output_dir.set(filedialog.askdirectory())

    def get_dir(self):
        return self.output_dir.get()
