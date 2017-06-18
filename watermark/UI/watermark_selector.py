from tkinter import *
from tkinter import filedialog


class WatermarkSelector(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master

        self.watermark_path = StringVar()
        self.watermark_path.set("Choose watermark")

        self.create_widgets()

    def create_widgets(self):
        Label(self, text="Watermark source").pack()
        Entry(self, width=50,
              textvariable=self.watermark_path).pack(side=LEFT)
        Button(self, text="Choose watermark",
               command=self.set_path).pack(side=LEFT, padx=10)

    def set_path(self):
        self.watermark_path.set(filedialog.askopenfilename())

    def get_path(self):
        return self.watermark_path.get()
