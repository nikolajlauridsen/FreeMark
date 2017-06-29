from tkinter import *
from tkinter.ttk import Progressbar
import threading
import queue

from watermark.tools.watermarker import WaterMarker


class Worker(Frame):
    """
    Worker gui elements, does all the actual work to the images with the 
    watermarker class and contains progressbar and startbutton
    """
    def __init__(self, file_selector, options_pane, master=None):
        super().__init__(master)

        self.threads = 5

        self.image_que = queue.Queue()

        self.file_selector = file_selector
        self.option_pane = options_pane
        self.watermarker = WaterMarker()

        self.progress_frame = Frame(self)
        self.progress_bar = Progressbar(self.progress_frame,
                                        orient="horizontal",
                                        mode="determinate",
                                        length=500)

        self.create_widgets()

    def create_widgets(self):
        """Create GUI"""
        Label(self.progress_frame, text="Progress").pack(side=LEFT, padx=10)
        self.progress_bar.pack(side=RIGHT)
        self.progress_frame.pack()
        Button(self, text="Start", command=self.apply_watermarks).pack(pady=5)

    def fill_que(self):
        """
        Fill the worker que from the files in file selector,  
        and prepare te progress bar
        """
        files = self.file_selector.get_file_paths()
        self.progress_bar.configure(maximum=len(files))
        for file in files:
            self.image_que.put(file)

    def apply_watermarks(self):
        """
        Fill the que, then prepare the watermarker
        before spawning workers
        """
        self.fill_que()
        self.watermarker.prep(self.option_pane.get_watermark_path())
        self.start_work()

    def start_work(self):
        """
        The baby factory, spawns child workers to apply the watermark to 
        the images
        """
        for n in range(self.threads):
            thread = threading.Thread(target=self.work)
            thread.start()

    def work(self):
        """
        Work instructions for the child workers
        keep grabbing a new image path and then apply watermark with 
        the watermarker, using option pane to create paths
        """
        while True:
            try:
                input_path = self.image_que.get(block=False)
            except queue.Empty:
                return
            try:
                kwargs = {"pos": self.option_pane.get_watermark_pos(),
                          "padding": self.option_pane.get_padding(),
                          "scale": self.option_pane.should_scale()}
                self.watermarker.apply_watermark(input_path,
                                                 self.option_pane.create_output_path(input_path),
                                                 **kwargs)
            except Exception as e:
                print("Error!\n", e)
            self.progress_bar.step()

