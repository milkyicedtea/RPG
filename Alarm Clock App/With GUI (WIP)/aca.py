import os
# import PySimpleGUI
import time
import tkinter as tk
from dataclasses import dataclass

@dataclass
class ClockProperties:
    Seconds: int
    Minutes: int
    Hours: int
    CurrentDay: int
    CurrentMonth: int
    CurrentYear: int

window = tk.Tk()