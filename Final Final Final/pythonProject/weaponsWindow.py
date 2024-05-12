import tkinter as tk
from tkinter import ttk
from primaryWep import primary
from secondaryWep import secondary
from meleeWep import melee


# The Creation of the weapons window that lets you choose between primary, secondary, and melee weapons.
def weaponWindow():
    weaponsWindow = tk.Toplevel()
    weaponsWindow.title('Weapons')
    weaponsWindow.geometry('300x100')
    weaponsButton = ttk.Button(weaponsWindow, text='Primary', command=primary)
    weaponsButton.pack(expand=True)
    weaponsButton2 = ttk.Button(weaponsWindow, text='Secondary', command=secondary)
    weaponsButton2.pack(expand=True)
    weaponsButton3 = ttk.Button(weaponsWindow, text='Melee', command=melee)
    weaponsButton3.pack(expand=True)

    # The exit button to close this window.
    def exit():
        weaponsWindow.destroy()

    exitButton = ttk.Button(weaponsWindow, text='EXIT', command=exit)
    exitButton.pack(expand=True)
