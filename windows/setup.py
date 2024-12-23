import sys
import os
from cx_Freeze import setup, Executable

# ADD FILES
files = ['icon.ico','themes/']

# TARGET
target = Executable(
    script="main.py",
    base="Win32GUI",
    icon="icon.ico"
)

# SETUP CX FREEZE
setup(
    name = "GedaEffect",
    version = "1.0",
    description = "Personal account for workers of company LLC GedaEffect",
    author = "mmTvv, Nikita P.",
    options = {'build_exe' : {'include_files' : files}},
    executables = [target]
    
)
