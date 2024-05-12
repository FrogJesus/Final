import tkinter as tk
from tkinter import ttk
from matInput import materialInputWindow
from whereMatsAre import wheretofindWindow

# The creation of the material window, gives you the option to go to overall materials window or where to find
# materials.
def materialWindow():
    materialsWindow = tk.Toplevel()
    materialsWindow.title('Material')
    materialsWindow.geometry('300x100')
    materialButton1 = ttk.Button(materialsWindow, text='Material Inputs', command=materialInputWindow)
    materialButton1.pack(expand=True)
    materialButton2 = ttk.Button(materialsWindow, text='Where to Find', command=wheretofindWindow)
    materialButton2.pack(expand=True)

    # The exit button to close this window.
    def exit():
        materialsWindow.destroy()

    exitButton = ttk.Button(materialsWindow, text='EXIT', command=exit)
    exitButton.pack(expand=True)