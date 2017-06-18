from tkinter import Tk
from watermark.watermark_app import WaterMarkApp


def main():
    root = Tk()
    root.title('Watermark')

    watermark = WaterMarkApp(master=root)
    watermark.mainloop()

if __name__ == '__main__':
    main()
