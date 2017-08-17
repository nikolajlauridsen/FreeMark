from tkinter import *
from tkinter import filedialog

from watermark.tools.errors import BadOptionError


class WatermarkSelector(Frame):
    """
    GUI element letting the user choose the watermark to be applied
    """
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master

        self.watermark_path = StringVar()
        self.watermark_path.set("Choose watermark")

        self.create_widgets()

    def create_widgets(self):
        """Create gui elements"""
        Label(self, text="Watermark source", font=14).pack(anchor=W)
        Entry(self, width=50,
              textvariable=self.watermark_path).pack(side=LEFT)
        Button(self, text="Choose watermark",
               command=self.set_path).pack(side=LEFT, padx=10)

    def set_path(self):
        """Prompt the user, asking the to choose a file"""
        self.watermark_path.set(filedialog.askopenfilename())

    def get_path(self):
        """
        Get the path to the currently selected watermark
        :return: path to watermark as string
        """
        path = self.watermark_path.get()
        if len(path) < 1:
            raise BadOptionError("Watermark not selected, please click the "
                                 "\"Choose watermark\" button")
        return path
