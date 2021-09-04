import os
from tkinter import *
from tkinter import ttk

for line in os.popen('systeminfo'):
    print(line.rstrip())
