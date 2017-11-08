from tkinter import Tk
from FreeMark.FreeMark_app import FreeMarkApp


def main():
    """
    Main method, starts TK and loads Watermark
    """
    root = Tk()
    root.title('FreeMark')
    root.iconbitmap('logo.ico')

    watermark = FreeMarkApp(master=root)
    watermark.mainloop()

if __name__ == '__main__':
    main()
