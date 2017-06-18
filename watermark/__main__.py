from tkinter import Tk
from watermark.watermark_app import WaterMarkApp


def main():
    """Main method, starts TK and loads Watermark"""
    root = Tk()
    root.title('Watermark')

    watermark = WaterMarkApp(master=root)
    watermark.mainloop()

if __name__ == '__main__':
    main()
