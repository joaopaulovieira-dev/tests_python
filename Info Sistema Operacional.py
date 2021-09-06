# import os
# from tkinter import *
# from tkinter import ttk

# for line in os.popen('systeminfo'):
#     print(line.rstrip())
import os
from tkinter import *
Outputfileobject = os.popen('systeminfo')
Output = Outputfileobject.read()
Outputfileobject.close()
root = Tk()
root.title("Output text")
Text = Label(root, text=Output).pack()
root.mainloop()
