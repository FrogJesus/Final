import tkinter as tk
from tkinter import ttk
from tkinter import *


# Creating the window for the secondary weapons to display in.
def secondary():
    secondaryWeapons = tk.Toplevel()
    secondaryWeapons.title('Secondary Weapons')
    secondaryWeapons.geometry('200x280')

    # The start of the labels to display each item and what you need to make them.
    label1 = ttk.Label(secondaryWeapons, text='Aklex Prime Blueprint', background='Yellow')
    label1_1 = ttk.Label(secondaryWeapons, text='2x Lex Prime', background='Yellow')
    label1_2 = ttk.Label(secondaryWeapons, text='Aklex Prime Link', background='Yellow')
    label1.grid(row=0, column=0, sticky='nw')
    label1_1.grid(row=1, column=0, sticky='nw')
    label1_2.grid(row=2, column=0, sticky='nw')

    # Filler label to create an empty row to make it slightly better visually.
    labelFiller = ttk.Label(secondaryWeapons, text='', background='White')
    labelFiller.grid(row=3, column=0, sticky='nw')

    label2 = ttk.Label(secondaryWeapons, text='Lex Prime Blueprint', background='Yellow')
    label2_1 = ttk.Label(secondaryWeapons, text='Lex Prime Barrel', background='Yellow')
    label2_2 = ttk.Label(secondaryWeapons, text='Lex Prime Receiver', background='Yellow')
    label2_3 = ttk.Label(secondaryWeapons, text='10x Orokin Cell', background='Yellow')
    label2.grid(row=4, column=0, sticky='nw')
    label2_1.grid(row=5, column=0, sticky='nw')
    label2_2.grid(row=6, column=0, sticky='nw')
    label2_3.grid(row=6, column=0, sticky='nw')

    # Filler label to create an empty row to make it slightly better visually.
    labelFiller2 = ttk.Label(secondaryWeapons, text='', background='White')
    labelFiller2.grid(row=7, column=0, sticky='nw')

    label3 = ttk.Label(secondaryWeapons, text='Sicarus Prime Blueprint', background='Yellow')
    label3_1 = ttk.Label(secondaryWeapons, text='Sicarus Prime Barrel', background='Yellow')
    label3_2 = ttk.Label(secondaryWeapons, text='Sicarus Prime Receiver', background='Yellow')
    label3_3 = ttk.Label(secondaryWeapons, text='10x Orokin Cell', background='Yellow')
    label3.grid(row=8, column=0, sticky='nw')
    label3_1.grid(row=9, column=0, sticky='nw')
    label3_2.grid(row=10, column=0, sticky='nw')
    label3_3.grid(row=11, column=0, sticky='nw')

    # The mouseover label text at the bottom that displays where to find these items.
    mouseoverLabel = ttk.Label(secondaryWeapons, text='', border=1, relief=SUNKEN, anchor=E)
    mouseoverLabel.grid(row=12, columnspan=10, ipady=2)

    # Defining an exit button and implementing it underneath so users can exit the window.
    def exit():
        secondaryWeapons.destroy()

    exitButton = ttk.Button(secondaryWeapons, text='EXIT', command=exit)
    exitButton.grid(row=13, columnspan=10)

    # Defining what text is displayed for each individual item.
    def label1Hover(e):
        mouseoverLabel.config(text="Relics: Axi A2, Neo O1")

    def label1_1Hover(e):
        mouseoverLabel.config(text="Obtain 2 Lex Prime weapons")

    def label1_2Hover(e):
        mouseoverLabel.config(text="Relics: Axi A2")

    def label2Hover(e):
        mouseoverLabel.config(text="Relics: Axi A2, Lith P9, Neo A11, V9")

    def label2_1Hover(e):
        mouseoverLabel.config(text="Relics: Axi A2, Lith P8, Meso N11")

    def label2_2Hover(e):
        mouseoverLabel.config(text="Relics: Axi A2, V10, V8, Meso W4")

    def label2_3Hover(e):
        mouseoverLabel.config(text="Saturn, Ceres, Deimos")

    def label3Hover(e):
        mouseoverLabel.config(text="Relics: Axi E1, Neo F1")

    def label3_1Hover(e):
        mouseoverLabel.config(text="Relics: Meso F2, Neo F1")

    def label3_2Hover(e):
        mouseoverLabel.config(text="Relics: Axi S2, Neo S5")

    def label3_3Hover(e):
        mouseoverLabel.config(text="Saturn, Ceres, Deimos")

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

    label3_3.bind("<Enter>", label3_3Hover)
    label3_3.bind("<Leave>", stopHover)
