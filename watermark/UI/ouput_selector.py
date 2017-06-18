from tkinter import *
from tkinter import filedialog
import os

NONE = 0
PRE = 1
SUFFIX = 2


class OutputSelector(Frame):
    """Class for selecting output destination and generating paths"""
    def __init__(self, master=None):
        super().__init__(master)

        self.fix = StringVar()
        self.fix_position = IntVar()
        self.output_dir = StringVar()
        self.output_dir.set("Choose output folder")
        self.create_widgets()

    def create_widgets(self):
        """Create and pack the TK widgets"""
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
        Entry(fix_frame, width=30,
              textvariable=self.fix).pack(side=LEFT, padx=5)
        # Me? I know who I am
        # I'm a frame playing a frame, disguised as another frame!
        radio_frame = Frame(fix_frame)
        Radiobutton(radio_frame, text="None", variable=self.fix_position,
                    value=NONE).pack(side=RIGHT)
        Radiobutton(radio_frame, text="Prefix", variable=self.fix_position,
                    value=PRE).pack(side=RIGHT)
        Radiobutton(radio_frame, text="Suffix", variable=self.fix_position,
                    value=SUFFIX).pack(side=RIGHT)
        radio_frame.pack(anchor=CENTER)
        fix_frame.pack(fill=X)

    def choose_dir(self):
        """
        Prompts the user to choose a folder.
        Bound to button next to folder entry
        """
        self.output_dir.set(filedialog.askdirectory())

    def get_dir(self):
        """Returns the currently selected dir"""
        return self.output_dir.get()

    def rename_file(self, filename, abs_path=False):
        """
        extract file name and apply suffix or prefix
        :param filename: file name or path
        :param abs_path: kwarg, true if filename isn't a filename but a path
        :return: 
        """
        if abs_path:
            filename = os.path.split(filename)[-1]

        if self.fix_position.get() == NONE:
            return filename
        elif self.fix_position.get() == PRE:
            return "{}_{}".format(self.fix.get(), filename)
        elif self.fix_position.get() == SUFFIX:
            filename = filename.rsplit('.', maxsplit=1)
            return "{}_{}.{}".format(filename[0], self.fix.get(), filename[1])

    def get_output_path(self, input_path):
        """
        Get output path from an input path
        :param input_path: path to original image
        :return: path to image destination
        """
        filename = self.rename_file(input_path, abs_path=True)
        return os.path.join(self.output_dir.get(), filename)
