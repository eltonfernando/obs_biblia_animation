import os
from setup import __VERSION__
from cx_Freeze import setup, Executable
from glob import glob

GUI2Exe_Target_1 = Executable(
    script = "main.py",
    initScript = None,
    base = 'Win32GUI',
    targetName = "main.exe",
    #compress = True,
    #copyDependentFiles = True,
    #appendScriptToExe = False,
    #appendScriptToLibrary = False
    #icon = "YOUR ICON FILE.ico"
    )
excludes = ["tkinter"]
includes = ["PyQt5"]
#namespace_packages=["multiprocessing.pool"]
packages=["PyQt5"]
path = []
include_files=[("historico","historico"),
               ("from.ui","from.ui"),
               ("biblia_aa.db","biblia_aa.db"),
               ("templates","templates")]
setup(
    version = __VERSION__,
    description = "Biblia OBS",
    author = "Elton Fernandes dos Santos",
    author_email = "eltonfernando90@email.com",
    name = "main",
    options = {"build_exe": {"includes": includes,
                             "excludes": excludes,
                             "packages": packages,
                             "include_msvcr": True,
                            # "namespace_packages":namespace_packages,
                             "path": path,
                            'include_files':include_files
                            }
               },
    executables = [GUI2Exe_Target_1]
    )
