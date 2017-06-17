from tkinter import *
from tkinter import filedialog
import os


class FileSelector(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

        self.base_dir = StringVar()
        self.error = StringVar()
        self.error.set("Choose folder")
        self.files = []

        self.button_frame = Frame(self)
        self.folder_frame = Frame(self)

        self.files_view = Listbox(self, width=65, height=20)
        self.folder_entry = Entry(self.folder_frame, width=60,
                                  textvariable=self.base_dir)
        self.warning_label = Label(self.button_frame, textvariable=self.error)

        self.create_widgets()

    def create_widgets(self):
        pad_y = 5
        pad_x = 10
        # List for files
        self.files_view.pack(pady=pad_y)

        # Folder entry field
        Label(self.folder_frame, text="Folder:").pack(side=LEFT)
        self.folder_entry.pack(side=RIGHT)

        # Button panel and error message
        Button(self.button_frame, text="Choose Folder",
               command=self.fill_list).pack(side=LEFT, padx=pad_x)
        Button(self.button_frame, text="Load files",
               command=self.refresh_files).pack(side=LEFT)
        self.warning_label.pack(padx=pad_x*2, side=RIGHT)

        # Pack frames
        self.folder_frame.pack()
        self.button_frame.pack(pady=pad_y)

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
        self.error.set("Waiting")

    def fill_list(self):
        """Fill the list, by first asking the user to choose a directory
        and then loading all the files from the directory"""
        self.prompt_directory()
        self.refresh_files()

    def get_files(self):
        """Might as well go full java now that we're at it"""
        return self.files
