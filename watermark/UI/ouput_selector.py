from tkinter import *
from tkinter import filedialog

NONE = 0
PRE = 1
SUFFIX = 2


class OutputSelector(Frame):
    """Class for selecting output destination an generating paths"""
    def __init__(self, master=None):
        super().__init__(master)

        self.fix = StringVar()
        self.fix_position = IntVar()
        self.output_dir = StringVar()
        self.output_dir.set("Choose output folder")
        self.create_widgets()

    def create_widgets(self):
        Label(self, text="Output options", font=14).pack(anchor=W)

        entry_frame = Frame(self)
        Entry(entry_frame, width=50,
              textvariable=self.output_dir).pack(side=LEFT)
        Button(entry_frame, text="Choose folder",
               command=self.choose_dir).pack(side=LEFT, padx=10)
        entry_frame.pack(fill=X)

        Label(self, text="Rename files").pack(anchor=W)

        fix_frame = Frame(self)
        Label(fix_frame, text="Fix: ").pack(side=LEFT)
        Entry(fix_frame, width=25,
              textvariable=self.fix).pack(side=LEFT, padx=10)
        radio_frame = Frame(fix_frame)
        Radiobutton(radio_frame, text="None", variable=self.fix_position,
                    value=NONE).pack(side=RIGHT)
        Radiobutton(radio_frame, text="Prefix", variable=self.fix_position,
                    value=PRE).pack(side=RIGHT)
        Radiobutton(radio_frame, text="Suffix", variable=self.fix_position,
                    value=SUFFIX).pack(side=RIGHT)
        radio_frame.pack(padx=10)
        fix_frame.pack(fill=X)

    def choose_dir(self):
        self.output_dir.set(filedialog.askdirectory())

    def get_dir(self):
        return self.output_dir.get()
