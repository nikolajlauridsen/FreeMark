from tkinter import *
from watermark.UI.file_selector import FileSelector
from watermark.UI.options_pane import OptionsPane
from watermark.UI.worker import Worker


class WaterMarkApp(Frame):
    """
    Top most frame of the application, represents the 'app'
    brings together all the other major pieces, which in turn brings together 
    the smaller pieces
    """
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

        self.create_widgets()

    def create_widgets(self):
        """Create the GUI elements"""
        pad_y = 5
        Label(self.master, text='Image Watermarker', font=16).pack(pady=pad_y)

        # Create listbox for files
        options_frame = Frame(self.master)
        file_selector = FileSelector(options_frame)
        options_pane = OptionsPane(options_frame)

        file_selector.pack(side=LEFT)
        options_pane.pack(side=RIGHT, fill=Y)

        options_frame.pack()

        worker = Worker(file_selector, options_pane)
        worker.pack()
