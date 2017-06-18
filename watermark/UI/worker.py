from tkinter import *
import os
import threading
import queue

from watermark.tools.watermarker import WaterMarker


class Worker(Frame):
    def __init__(self, file_selector, watermark_selector, master=None):
        super().__init__(master)

        self.threads = 5

        self.output_path = None

        self.image_que = queue.Queue()

        self.file_selector = file_selector
        self.watermark_selector = watermark_selector
        self.watermarker = WaterMarker()

        self.create_widgets()

    def create_widgets(self):
        Button(self, text="Start", command=self.apply_watermarks).pack()

    def fill_que(self):
        for file in self.file_selector.get_file_paths():
            self.image_que.put(file)

    def apply_watermarks(self):
        self.output_path = r"D:\Github\Watermark\watermarked_images"
        self.fill_que()
        self.watermarker.preb(self.watermark_selector.get_path())
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
            self.watermarker.apply_watermark(input_path,
                                             os.path.join(self.output_path,
                                                          os.path.split(input_path)[-1]))

