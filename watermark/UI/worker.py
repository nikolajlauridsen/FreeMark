from tkinter import *
from tkinter.ttk import Progressbar
from tkinter import messagebox
import threading
import queue

from ..tools.errors import BadOptionError
from watermark.tools.watermarker import WaterMarker


class Worker(Frame):
    """
    Worker gui elements, does all the actual work to the images with the
    watermarker class and contains progressbar and startbutton
    """
    def __init__(self, file_selector, options_pane, master=None):
        super().__init__(master)

        self.running = False

        self.image_que = queue.Queue()

        self.file_selector = file_selector
        self.option_pane = options_pane
        self.watermarker = WaterMarker

        self.progress_var = IntVar()
        self.file_count = IntVar()
        self.progress_bar = Progressbar(self, orient="horizontal",
                                        mode="determinate", length=600)

        self.button_frame = Frame(self)
        self.start_button = Button(self.button_frame, text="Start",
                                   command=self.apply_watermarks)
        self.stop_button = Button(self.button_frame, text="Stop",
                                  command=self.stop_work)
        self.counter_frame = Frame(self)

        self.create_widgets()

    def create_widgets(self):
        """Create GUI"""
        Label(self.counter_frame, textvariable=self.progress_var).pack(side=LEFT)
        Label(self.counter_frame, text="/").pack(side=LEFT)
        Label(self.counter_frame, textvariable=self.file_count).pack(side=LEFT)
        self.counter_frame.pack()

        self.progress_bar.pack()

        self.stop_button.config(state=DISABLED)
        self.start_button.pack(side=LEFT, padx=10)
        self.stop_button.pack(side=LEFT)
        self.button_frame.pack(pady=10)

    def fill_que(self):
        """
        Fill the worker que from the files in file selector,
        and prepare te progress bar
        """
        files = self.file_selector.get_file_paths()
        self.file_count.set(len(files))
        self.progress_bar.configure(maximum=len(files))
        for file in files:
            self.image_que.put(file)

    def apply_watermarks(self):
        """
        Fill the que, then prepare the watermarker
        before spawning workers
        """
        if len(self.file_selector.files) < 1:
            messagebox.showerror('Nothing to watermark',
                                 'Please choose one or more files to watermark.')
        self.fill_que()
        try:
            self.watermarker = WaterMarker(self.option_pane.get_watermark_path())
        except Exception as e:
            self.handle_error(e)

        self.stop_button.config(state=NORMAL)
        self.start_button.config(state=DISABLED)
        self.start_work()

    def start_work(self):
        """
        The baby factory, spawns child workers to apply the watermark to
        the images
        """
        try:
            kwargs = {"pos": self.option_pane.get_watermark_pos(),
                      "padding": self.option_pane.get_padding(),
                      "scale": self.option_pane.should_scale(),
                      "opacity": self.option_pane.get_opacity()}
            output = self.option_pane.get_output_path()
            print(output)
        except BadOptionError as e:
            self.handle_error(e)
            return
        self.running = True
        self.option_pane.output_selector.lock()
        thread = threading.Thread(target=self.work,
                                  kwargs=kwargs, args=(output, ))
        thread.start()

    def reset(self):
        self.image_que = queue.Queue()
        self.watermarker = WaterMarker
        self.progress_var.set(0)
        self.file_count.set(0)
        self.start_button.config(state=NORMAL)
        self.stop_button.config(state=DISABLED)
        self.option_pane.output_selector.unlock()

    def handle_error(self, e):
        self.reset()
        messagebox.showerror("Error", str(e))

    def work(self, outpath, **kwargs):
        """
        Work instructions for the child workers
        keep grabbing a new image path and then apply watermark with
        the watermarker, using option pane to create paths
        """
        while self.running:
            try:
                input_path = self.image_que.get(block=False)
            except queue.Empty:
                self.start_button.config(state=NORMAL)
                self.stop_button.config(state=DISABLED)
                self.option_pane.output_selector.unlock()
                self.progress_var.set(0)
                self.file_count.set(0)
                self.running = False
                return
            try:
                self.watermarker.apply_watermark(input_path,
                                                 self.option_pane.create_output_path(input_path, outpath),
                                                 **kwargs)
            except BadOptionError as e:
                self.handle_error(e)
                print("Bad config, stopping\n", e)
                return
            except Exception as e:
                print("Error!\n", type(e), "\n", e)
            self.progress_bar.step(amount=1)
            self.progress_var.set(self.progress_var.get()+1)

        self.reset()

    def stop_work(self):
        self.running = False
