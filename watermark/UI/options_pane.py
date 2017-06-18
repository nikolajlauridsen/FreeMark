from tkinter import *
import os

from watermark.UI.ouput_selector import OutputSelector
from watermark.UI.watermark_selector import WatermarkSelector


class OptionsPane(Frame):
    def __init__(self, master=None):
        super().__init__(master)

        self.output_selector = OutputSelector(self)
        self.watermark_selector = WatermarkSelector(self)
        self.create_widgets()

    def create_widgets(self):
        self.watermark_selector.pack(fill=X, pady=5)
        self.output_selector.pack(fill=X, pady=5)

    def get_watermark_path(self):
        return self.watermark_selector.get_path()

    def get_output_path(self):
        return self.output_selector.get_dir()

    def create_output_path(self, input_path):
        filename = os.path.split(input_path)[-1]
        return os.path.join(self.output_selector.get_dir(), filename)

