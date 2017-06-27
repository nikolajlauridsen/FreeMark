from tkinter import *


class WatermarkOptions(Frame):

    def __init__(self, master=None):
        super().__init__(master)

        self.position = StringVar()
        self.position.set("SE")

        self.padx = StringVar()
        self.pady = StringVar()
        self.padx.set(20)
        self.pady.set(5)

        self.create_widgets()

    def create_widgets(self):
        Label(self, text="Watermark options", font=14).pack(anchor=W)

        Label(self, text="Position").pack(anchor=W)

        validate = (self.register(self.validate_int), '%P')

        padding_frame = Frame(self)
        Label(padding_frame, text="Pad x").grid(column=0, row=0)
        Entry(padding_frame, textvariable=self.padx, validate="key",
              validatecommand=validate).grid(column=1, row=0)

        Label(padding_frame, text="Pad y").grid(column=0, row=1)
        Entry(padding_frame, textvariable=self.pady, validate="key",
              validatecommand=validate).grid(column=1, row=1)

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
        pos_frame.pack(side=RIGHT)

    @staticmethod
    def validate_int(number):
        try:
            int(number)
        except ValueError:
            return False
        else:
            return True
