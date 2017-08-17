"""
cx_freeze needs to be pointed towards something, therefore this.
Also gives non-windows users a nice 'double-click-able' file
"""
import FreeMark.__main__ as free_mark

free_mark.main()
