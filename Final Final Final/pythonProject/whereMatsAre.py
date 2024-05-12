import tkinter as tk
from tkinter import ttk


# The creation of the Where to Find Materials window.
def wheretofindWindow():
    wheretofindMats = tk.Toplevel()
    wheretofindMats.title('Where to Find Materials')
    wheretofindMats.geometry('250x300')

    # This shows a list of materials and where to find them.
    label1 = ttk.Label(wheretofindMats, text='Orokin Cell', background='Yellow')
    label1_1 = ttk.Label(wheretofindMats, text='Saturn, Ceres, Deimos', background='White')
    label1.grid(row=0, column=3, sticky='nw')
    label1_1.grid(row=1, column=3, sticky='nw')

    # Filler label to create an empty row to make it slightly better visually
    labelFiller = ttk.Label(wheretofindMats, text='', background='White')
    labelFiller.grid(row=2, column=0, sticky='nw')

    label1 = ttk.Label(wheretofindMats, text='Neural Sensors', background='Yellow')
    label1_1 = ttk.Label(wheretofindMats, text='Jupiter, Kuva Fortress', background='White')
    label1.grid(row=3, column=3, sticky='nw')
    label1_1.grid(row=4, column=3, sticky='nw')

    # Filler label to create an empty row to make it slightly better visually
    labelFiller2 = ttk.Label(wheretofindMats, text='', background='White')
    labelFiller2.grid(row=5, column=0, sticky='nw')

    label3 = ttk.Label(wheretofindMats, text='Argon Crystals', background='Yellow')
    label3_1 = ttk.Label(wheretofindMats, text='The Void', background='White')
    label3.grid(row=6, column=3, sticky='nw')
    label3_1.grid(row=7, column=3, sticky='nw')

    # Filler label to create an empty row to make it slightly better visually
    labelFiller3 = ttk.Label(wheretofindMats, text='', background='White')
    labelFiller3.grid(row=8, column=0, sticky='nw')

    label4 = ttk.Label(wheretofindMats, text='Control Modules', background='Yellow')
    label4_1 = ttk.Label(wheretofindMats, text='Neptune, Europa, The Void', background='White')
    label4.grid(row=9, column=3, sticky='nw')
    label4_1.grid(row=10, column=3, sticky='nw')

    # Filler label to create an empty row to make it slightly better visually
    labelFiller4 = ttk.Label(wheretofindMats, text='', background='White')
    labelFiller4.grid(row=11, column=0, sticky='nw')

    label5 = ttk.Label(wheretofindMats, text='Morphics', background='Yellow')
    label5_1 = ttk.Label(wheretofindMats, text='Mercury, Mars, Phobos, Europa, Pluto', background='White')
    label5.grid(row=12, column=3, sticky='nw')
    label5_1.grid(row=13, column=3, sticky='nw')

    # The exit button to close this window.
    def exit():
        wheretofindMats.destroy()

    exitButton = ttk.Button(wheretofindMats, text='EXIT', command=exit)
    exitButton.grid(row=14, columnspan=10)