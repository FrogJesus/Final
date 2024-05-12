import tkinter as tk
from tkinter import ttk
from weaponsWindow import weaponWindow
from warframes import warframes
from companions import companions


# The creation of the items window that lets users choose between Weapons, Warframes, and Companions Windows
def itemWindow():
    itemsWindow = tk.Toplevel()
    itemsWindow.title('Items')
    itemsWindow.geometry('300x100')
    itemButton = ttk.Button(itemsWindow, text='Weapons', command=weaponWindow)
    itemButton.pack(expand=True)
    itemButton2 = ttk.Button(itemsWindow, text='Warframes', command=warframes)
    itemButton2.pack(expand=True)
    itemButton3 = ttk.Button(itemsWindow, text='Companions', command=companions)
    itemButton3.pack(expand=True)

    # Creation of exit button so you can close this window.
    def exit():
        itemsWindow.destroy()

    exitButton = ttk.Button(itemsWindow, text='EXIT', command=exit)
    exitButton.pack(expand=True)