from tkinter import *
from tkinter.ttk import Progressbar
import threading
import queue

from watermark.tools.watermarker import WaterMarker


class Worker(Frame):
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
        Label(self.progress_frame, text="Progress").pack(side=LEFT, padx=10)
        self.progress_bar.pack(side=RIGHT)
        self.progress_frame.pack()
        Button(self, text="Start", command=self.apply_watermarks).pack(pady=5)

    def fill_que(self):
        files = self.file_selector.get_file_paths()
        self.progress_bar.configure(maximum=len(files))
        for file in files:
            self.image_que.put(file)

    def apply_watermarks(self):
        self.fill_que()
        self.watermarker.preb(self.option_pane.get_watermark_path())
        self.start_work()

    def start_work(self):
        for n in range(self.threads):
            thread = threading.Thread(target=self.work)
            thread.start()

    def work(self):
        while True:
            try:
                input_path = self.image_que.get(block=False)
            except queue.Empty:
                return
            try:
                self.watermarker.apply_watermark(input_path,
                                                 self.option_pane.create_output_path(input_path))
            except Exception as e:
                print("Error!\n", e)
            self.progress_bar.step()

