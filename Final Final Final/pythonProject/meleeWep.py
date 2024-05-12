import tkinter as tk
from tkinter import ttk
from tkinter import *


# Creating and displaying the initial window for the melee Weapons category.
def melee():
    meleeWeapons = tk.Toplevel()
    meleeWeapons.title('Melee Weapons')
    meleeWeapons.geometry('200x300')
    # Each of these labels down to the exit button show an item with yellow text that you can scroll over to display
    # Where to find the materials to make them.
    label1 = ttk.Label(meleeWeapons, text='Glaive Prime Blueprint', background='Yellow')
    label1_1 = ttk.Label(meleeWeapons, text='2x Glaive Prime Blade', background='Yellow')
    label1_2 = ttk.Label(meleeWeapons, text='Glaive Prime Disk', background='Yellow')
    label1_3 = ttk.Label(meleeWeapons, text='10x Orokin Cell', background='Yellow')
    label1.grid(row=0, column=0, sticky='nw')
    label1_1.grid(row=1, column=0, sticky='nw')
    label1_2.grid(row=2, column=0, sticky='nw')
    label1_3.grid(row=3, column=0, sticky='nw')

    # Filler label to create an empty row to make it slightly better visually.
    labelFiller = ttk.Label(meleeWeapons, text='', background='White')
    labelFiller.grid(row=4, column=0, sticky='nw')

    label2 = ttk.Label(meleeWeapons, text='Ankyros Prime Blueprint', background='Yellow')
    label2_1 = ttk.Label(meleeWeapons, text='2x Ankyros Prime Blade', background='Yellow')
    label2_2 = ttk.Label(meleeWeapons, text='2x Ankyros Gauntlet', background='Yellow')
    label2_3 = ttk.Label(meleeWeapons, text='10x Orokin Cell', background='Yellow')
    label2.grid(row=5, column=0, sticky='nw')
    label2_1.grid(row=6, column=0, sticky='nw')
    label2_2.grid(row=7, column=0, sticky='nw')
    label2_3.grid(row=8, column=0, sticky='nw')

    # Filler label to create an empty row to make it slightly better visually.
    labelFiller2 = ttk.Label(meleeWeapons, text='', background='White')
    labelFiller2.grid(row=9, column=0, sticky='nw')

    label3 = ttk.Label(meleeWeapons, text='Fang Prime Blueprint', background='Yellow')
    label3_1 = ttk.Label(meleeWeapons, text='2x Fang Prime Blade', background='Yellow')
    label3_2 = ttk.Label(meleeWeapons, text='2x Fang Prime Handle', background='Yellow')
    label3.grid(row=10, column=0, sticky='nw')
    label3_1.grid(row=11, column=0, sticky='nw')
    label3_2.grid(row=12, column=0, sticky='nw')

    # The mouseover label text at the bottom that displays where to find these items.
    mouseoverLabel = ttk.Label(meleeWeapons, text='', border=1, relief=SUNKEN, anchor=E)
    mouseoverLabel.grid(row=13, columnspan=10, ipady=2)

    # Defining an exit button and implementing it underneath so users can exit the window.
    def exit():
        meleeWeapons.destroy()

    exitButton = ttk.Button(meleeWeapons, text='EXIT', command=exit)
    exitButton.grid(row=14, columnspan=10)

    # Defining what text is displayed for each individual item.
    def label1Hover(e):
        mouseoverLabel.config(text="Relics: Lith G1, G2")

    def label1_1Hover(e):
        mouseoverLabel.config(text="Relics: Axi E1, L1")

    def label1_2Hover(e):
        mouseoverLabel.config(text="Relics: Meso F3, Neo S5")

    def label1_3Hover(e):
        mouseoverLabel.config(text="Saturn, Ceres, Deimos")

    def label2Hover(e):
        mouseoverLabel.config(text="Relics: Lith B1, B4")

    def label2_1Hover(e):
        mouseoverLabel.config(text="Relics: Axi R1, S3")

    def label2_2Hover(e):
        mouseoverLabel.config(text="Relics: Meso M1, Neo R1")

    def label2_3Hover(e):
        mouseoverLabel.config(text="Saturn, Ceres, Deimos")

    def label3Hover(e):
        mouseoverLabel.config(text="Relics: Lith R5, Meso V9, Axi A11")

    def label3_1Hover(e):
        mouseoverLabel.config(text="Relics: Axi L6, P7, B1, B2")

    def label3_2Hover(e):
        mouseoverLabel.config(text="Relics: Axi B8, Meso H5, Lith D2")

    # The action that takes place when you stop hovering over the item.
    def stopHover(e):
        mouseoverLabel.config(text='')

    # <Enter> Is when you initially hover over, it'll display the text above
    # <Leave> Tells the application to display nothing after your mouse leaves the label.
    label1.bind("<Enter>", label1Hover)
    label1.bind("<Leave>", stopHover)

    label1_1.bind("<Enter>", label1_1Hover)
    label1_1.bind("<Leave>", stopHover)

    label1_2.bind("<Enter>", label1_2Hover)
    label1_2.bind("<Leave>", stopHover)

    label1_3.bind("<Enter>", label1_3Hover)
    label1_3.bind("<Leave>", stopHover)

    label2.bind("<Enter>", label2Hover)
    label2.bind("<Leave>", stopHover)

    label2_1.bind("<Enter>", label2_1Hover)
    label2_1.bind("<Leave>", stopHover)

    label2_2.bind("<Enter>", label2_2Hover)
    label2_2.bind("<Leave>", stopHover)

    label2_3.bind("<Enter>", label2_3Hover)
    label2_3.bind("<Leave>", stopHover)

    label3.bind("<Enter>", label3Hover)
    label3.bind("<Leave>", stopHover)

    label3_1.bind("<Enter>", label3_1Hover)
    label3_1.bind("<Leave>", stopHover)

    label3_2.bind("<Enter>", label3_2Hover)
    label3_2.bind("<Leave>", stopHover)
