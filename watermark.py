"""
cx_freeze needs to be pointed towards something, therefore this.
Also gives non-windows users a nice 'double-click-able' file
"""
import watermark.__main__ as watermark

watermark.main()
