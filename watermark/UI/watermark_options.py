from tkinter import *


class WatermarkOptions(Frame):

    def __init__(self, master=None):
        super().__init__(master)

        self.position = StringVar()
        self.position.set("SE")

        self.padding_frame = Frame(self)
        validate = (self.register(self.validate_int), '%P')
        self.padx = Spinbox(self.padding_frame, validate="key",
                            validatecommand=validate)
        self.pady = Spinbox(self.padding_frame, validate="key",
                            validatecommand=validate)
        self.padx.insert(0, 20)
        self.pady.insert(0, 5)

        self.create_widgets()

    def create_widgets(self):
        Label(self, text="Watermark options", font=14).pack(anchor=W)

        Label(self, text="Position").pack(anchor=W)

        Label(self.padding_frame, text="Pad x").grid(column=0, row=0)
        self.padx.grid(column=1, row=0)

        Label(self.padding_frame, text="Pad y").grid(column=0, row=1)
        self.pady.grid(column=1, row=1)
        self.padding_frame.pack(side=LEFT)

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
