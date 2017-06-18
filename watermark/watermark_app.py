from tkinter import *
from watermark.UI.file_selector import FileSelector
from watermark.UI.watermark_selector import WatermarkSelector


class WaterMarkApp(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

        self.create_widgets()

    def create_widgets(self):
        pad_y = 5
        Label(self.master, text='Image Watermarker', font=16).pack(pady=pad_y)

        # Create listbox for files
        file_selector = FileSelector(self.master)
        file_selector.pack(side=LEFT)

        watermark_selector = WatermarkSelector(self.master)
        watermark_selector.pack(side=RIGHT)
