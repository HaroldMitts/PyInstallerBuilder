# PyInstallerBuilder is a Python script that uses PyInstaller to build a standalone executable.
# It allows the user to browse for a Python script to be converted, and then builds the executable.
# The executable will be named the same as the Python script.
# Dependencies: PyInstaller, Python 3.6, tkinter
# Author: Harold Mitts
# Date: February 24, 2023
# License: GNU
# Website: https://github.com/HaroldMitts/PyInstallerBuilder

version_num = "1.2"
import os
import subprocess
import tkinter as tk
from tkinter import filedialog

COLORS = ["black", "red", "green", "yellow", "blue", "magenta", "cyan", "white"]
CODES = ["0;30", "0;31", "0;32", "0;33", "0;34", "0;35", "0;36", "0;37", "1;30", "1;31", "1;32", "1;33", "1;34", "1;35", "1;36", "1;37"]
COLOR_CODES = dict(zip(COLORS, CODES))

def print_color(text, color):
    print(f"\033[{COLOR_CODES[color]}m{text}\033[0m")

def get_file_path():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(filetypes=[("Python scripts", "*.py"), ("All files", "*.*")])
    return file_path

def main():
    print_color("Running PyInstaller Builder", "green")
    print_color("By Harold Mitts", "green")
    print("\033[32mVersion: \033[0m", version_num)
    print()

    file_path = get_file_path()
    if not file_path:
        print_color("No file selected.", "red")
        return

    print(f"File selected: {file_path}")
    print()

    os.chdir(os.path.dirname(os.path.abspath(file_path)))

    file_name = os.path.basename(file_path)
    file_name_no_ext = os.path.splitext(file_name)[0]

    if not file_name.endswith(".py"):
        print_color(f"File {file_name} is not a Python script.", "red")
        return

    print(f"Building executable {file_name}...")
    print()
    print("This may take some time, depending on your system and the file size.")
    print()
    print_color("Please wait...", "red")
    print()

    with open(os.devnull, "w") as devnull:
        subprocess.call(["pyinstaller", "--onefile", file_name], stdout=devnull, stderr=devnull)

    print()
    print_color("Executable built.", "green")
    exe_path = os.path.join(os.path.abspath("dist"), f"{file_name_no_ext}.exe")
    print(f"File path: {exe_path}")
    print_color("Preparing to exit...", "green")

if __name__ == "__main__":
    main()
