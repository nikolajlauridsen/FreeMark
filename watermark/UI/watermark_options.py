from tkinter import *


class WatermarkOptions(Frame):

    def __init__(self, master=None):
        super().__init__(master)

        self.position = StringVar()
        self.position.set("SE")

        self.create_widgets()

    def create_widgets(self):
        Label(self, text="Watermark options", font=14).pack(anchor=W)

        Label(self, text="Position").pack(anchor=W)
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
        pos_frame.pack()
