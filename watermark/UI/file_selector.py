from tkinter import *
from tkinter import filedialog
import os


class FileSelector(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

        self.base_dir = StringVar()
        self.error = StringVar()
        self.files = []

        self.files_view = Listbox(self, width=75, height=15)
        self.folder_entry = Entry(self, width=60,
                                  textvariable=self.base_dir)
        self.warning_label = Label(self, textvariable=self.error)
        self.create_widgets()

    def create_widgets(self):
        pad_y = 5
        pad_x = 10
        self.files_view.pack(pady=pad_y)

        self.folder_entry.pack(pady=pad_y)
        Button(self, text="Choose Folder",
               command=self.fill_list).pack(pady=pad_y, side=LEFT,
                                            padx=pad_x)
        Button(self, text="Load files",
               command=self.refresh_files).pack(pady=pad_y, side=LEFT)
        self.warning_label.pack(padx=pad_x, side=LEFT)

    def prompt_directory(self):
        """Prompt the user for a base dir"""
        self.base_dir.set(filedialog.askdirectory())

    def refresh_files(self):
        """Update files list"""
        try:
            self.files = [file for file in os.listdir(self.base_dir.get())
                          if os.path.isfile(os.path.join(self.base_dir.get(),
                                                         file))]
        except FileNotFoundError:
            self.error.set('Directory not found')
            return

        self.files_view.delete(0, END)
        for file in self.files:
            self.files_view.insert(END, file)

    def fill_list(self):
        """Fill the list, by first asking the user to choose a directory
        and then loading all the files from the directory"""
        self.prompt_directory()
        self.refresh_files()

    def get_files(self):
        """Might as well go full java now that we're at it"""
        return self.files
