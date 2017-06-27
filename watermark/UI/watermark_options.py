from tkinter import *
# tkinter OptionMenu is hella ugly so use ttk
from tkinter.ttk import OptionMenu


class WatermarkOptions(Frame):

    def __init__(self, master=None):
        super().__init__(master)

        self.position = StringVar()
        self.position.set("SE")

        self.padx = StringVar()
        self.pady = StringVar()
        self.unit_x = StringVar()
        self.unit_y = StringVar()
        self.padx.set(20)
        self.pady.set(5)
        # ttk is super weird and demands that the first option is left blank
        self.unit_options = ["", "px", "%"]
        self.unit_x.set(self.unit_options[1])
        self.unit_y.set(self.unit_options[1])

        self.create_widgets()

    def create_widgets(self):
        padx = 5
        pady = 5
        Label(self, text="Watermark options", font=14).pack(anchor=W)

        Label(self, text="Position").pack(anchor=W)

        validate = (self.register(self.validate_int), '%P')

        padding_frame = Frame(self)
        # Horizontal padding
        Label(padding_frame, text="Pad x").grid(column=0, row=0)
        Entry(padding_frame, textvariable=self.padx, validate="key", width=5,
              validatecommand=validate).grid(column=1, row=0, padx=padx)
        OptionMenu(padding_frame, self.unit_x,
                   *self.unit_options).grid(column=3, row=0)

        # Vertical padding
        Label(padding_frame, text="Pad y").grid(column=0, row=1)
        Entry(padding_frame, textvariable=self.pady, validate="key", width=5,
              validatecommand=validate).grid(column=1, row=1,
                                             padx=padx, pady=pady)
        OptionMenu(padding_frame, self.unit_y,
                   *self.unit_options).grid(column=3, row=1)

        padding_frame.pack(side=LEFT)

        pos_frame = Frame(self)
        radio_pad = 5

        Radiobutton(pos_frame, text="Top left", variable=self.position,
                    value="NW").grid(column=0, row=0, sticky=W,
                                     padx=radio_pad, pady=radio_pad)

        Radiobutton(pos_frame, text="Top right", variable=self.position,
                    value="NE").grid(column=1, row=0, sticky=W,
                                     padx=radio_pad, pady=radio_pad)

        Radiobutton(pos_frame, text="Bottom left", variable=self.position,
                    value="SW").grid(column=0, row=1,
                                     padx=radio_pad, pady=radio_pad)

        Radiobutton(pos_frame, text="Bottom right", variable=self.position,
                    value="SE").grid(column=1, row=1,
                                     padx=radio_pad, pady=radio_pad)
        pos_frame.pack(side=LEFT, padx=30)

    @staticmethod
    def validate_int(number):
        try:
            int(number)
        except ValueError:
            return False
        else:
            return True
