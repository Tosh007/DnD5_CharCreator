import sys
from cx_Freeze import setup, Executable

build_exe_options = {"packages": ["sip"]}

setup(
    name = "DnD-CharCreator",
    version = "1.0",
    description = "Character Creation Utility for DnD5",
    options = {'build_exe': build_exe_options},
    executables = [Executable("Main.py", base="Win32Gui")]
    )