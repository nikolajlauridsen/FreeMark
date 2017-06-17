"""setup script for creating windows executable with cx_freeze"""
import sys
from cx_Freeze import setup, Executable
import os

python_path = r"C:\Users\EUC\AppData\Local\Programs\Python\Python35"

os.environ['TCL_LIBRARY'] = os.path.join(python_path, "tcl", "tcl8.6")
os.environ['TK_LIBRARY'] = os.path.join(python_path, "tcl", "tk8.6")

package_list = ["watermark", "tkinter", "os"]

build_exe_options = {"packages": package_list,
                     "include_files": [os.path.join("include", file) for file
                                       in os.listdir("include")]}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(name="Watermark",
      version="0.0.1",
      description="Watermark images, easily",
      options={"build_exe": build_exe_options},
      executables=[Executable(os.path.join("watermark", "__main__.py"),
                              base=base)])
