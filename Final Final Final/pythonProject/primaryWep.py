import tkinter as tk
from tkinter import ttk
from tkinter import *


# The creation of the primary weapons window.
def primary():
    primaryWeapons = tk.Toplevel()
    primaryWeapons.title('Primary Weapons')
    primaryWeapons.geometry('200x380')

    # The items needed to make each primary weapon, displayed in labels in a grid.
    label1 = ttk.Label(primaryWeapons, text='Boltor Prime Blueprint', background='Yellow')
    label1_1 = ttk.Label(primaryWeapons, text='Boltor Prime Barrel', background='Yellow')
    label1_2 = ttk.Label(primaryWeapons, text='Boltor Prime Receiver', background='Yellow')
    label1_3 = ttk.Label(primaryWeapons, text='Boltor Prime Stock', background='Yellow')
    label1_4 = ttk.Label(primaryWeapons, text='10x Orokin Cell', background='Yellow')
    label1.grid(row=0, column=0, sticky='nw')
    label1_1.grid(row=1, column=0, sticky='nw')
    label1_2.grid(row=2, column=0, sticky='nw')
    label1_3.grid(row=3, column=0, sticky='nw')
    label1_4.grid(row=4, column=0, sticky='nw')

    # Filler label to create an empty row to make it slightly better visually.
    labelFiller = ttk.Label(primaryWeapons, text='', background='White')
    labelFiller.grid(row=5, column=0, sticky='nw')

    label2 = ttk.Label(primaryWeapons, text='Boar Prime Blueprint', background='Yellow')
    label2_1 = ttk.Label(primaryWeapons, text='Boar Prime Barrel', background='Yellow')
    label2_2 = ttk.Label(primaryWeapons, text='Boar Prime Receiver', background='Yellow')
    label2_3 = ttk.Label(primaryWeapons, text='Boar Prime Stock', background='Yellow')
    label2_4 = ttk.Label(primaryWeapons, text='10x Orokin Cell', background='Yellow')
    label2.grid(row=6, column=0, sticky='nw')
    label2_1.grid(row=7, column=0, sticky='nw')
    label2_2.grid(row=8, column=0, sticky='nw')
    label2_3.grid(row=9, column=0, sticky='nw')
    label2_4.grid(row=10, column=0, sticky='nw')

    # Filler label to create an empty row to make it slightly better visually.
    labelFiller2 = ttk.Label(primaryWeapons, text='', background='White')
    labelFiller2.grid(row=11, column=0, sticky='nw')

    label3 = ttk.Label(primaryWeapons, text='Braton Prime Blueprint', background='Yellow')
    label3_1 = ttk.Label(primaryWeapons, text='Braton Prime Barrel', background='Yellow')
    label3_2 = ttk.Label(primaryWeapons, text='Braton Prime Receiver', background='Yellow')
    label3_3 = ttk.Label(primaryWeapons, text='Braton Prime Stock', background='Yellow')
    label3_4 = ttk.Label(primaryWeapons, text='10x Orokin Cell', background='Yellow')
    label3.grid(row=12, column=0, sticky='nw')
    label3_1.grid(row=13, column=0, sticky='nw')
    label3_2.grid(row=14, column=0, sticky='nw')
    label3_3.grid(row=15, column=0, sticky='nw')
    label3_4.grid(row=16, column=0, sticky='nw')

    # The mouseover label text at the bottom that displays where to find these items.
    mouseoverLabel = ttk.Label(primaryWeapons, text='', border=1, relief=SUNKEN, anchor=E)
    mouseoverLabel.grid(row=17, columnspan=10, ipady=2)

    # Defining an exit button and implementing it underneath so users can exit the window.
    def exit():
        primaryWeapons.destroy()

    exitButton = ttk.Button(primaryWeapons, text='EXIT', command=exit)
    exitButton.grid(row=18, columnspan=10)

    # Defining what text is displayed for each individual item.
    def label1Hover(e):
        mouseoverLabel.config(text="Relics: Lith B4, Neo B3")

    def label1_1Hover(e):
        mouseoverLabel.config(text="Relics: Meso M1, N6")

    def label1_2Hover(e):
        mouseoverLabel.config(text="Relics: Lith B1, Neo R1")

    def label1_3Hover(e):
        mouseoverLabel.config(text="Relics: Axi R1, S3")

    def label1_4Hover(e):
        mouseoverLabel.config(text="Saturn, Ceres, Deimos")

    def label2Hover(e):
        mouseoverLabel.config(text="Relics: Meso F4, Neo B3, D1, N9")

    def label2_1Hover(e):
        mouseoverLabel.config(text="Relics: Axi D4, V2, Lith M2, Meso M1")

    def label2_2Hover(e):
        mouseoverLabel.config(text="Relics: Axi R1, S4, Lith L4, M1")

    def label2_3Hover(e):
        mouseoverLabel.config(text="Relics: Lith B1, Meso B1, B3, Neo B8")

    def label2_4Hover(e):
        mouseoverLabel.config(text="Saturn, Ceres, Deimos")

    def label3Hover(e):
        mouseoverLabel.config(text="Relics: Axi G11, A16, A7, Meso B9")

    def label3_1Hover(e):
        mouseoverLabel.config(text="Relics: Axi A17, Lith C11, N14, P4")

    def label3_2Hover(e):
        mouseoverLabel.config(text="Relics: Neo A11, Axi H6, H7, K10")

    def label3_3Hover(e):
        mouseoverLabel.config(text="Relics: Axi P7, A1, A4, A7, A8")

    def label3_4Hover(e):
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

    label1_3.bind("<Enter>", label1_3Hover)
    label1_3.bind("<Leave>", stopHover)

    label1_4.bind("<Enter>", label1_4Hover)
    label1_4.bind("<Leave>", stopHover)

    label2.bind("<Enter>", label2Hover)
    label2.bind("<Leave>", stopHover)

    label2_1.bind("<Enter>", label2_1Hover)
    label2_1.bind("<Leave>", stopHover)

    label2_2.bind("<Enter>", label2_2Hover)
    label2_2.bind("<Leave>", stopHover)

    label2_3.bind("<Enter>", label2_3Hover)
    label2_3.bind("<Leave>", stopHover)

    label2_4.bind("<Enter>", label2_4Hover)
    label2_4.bind("<Leave>", stopHover)

    label3.bind("<Enter>", label3Hover)
    label3.bind("<Leave>", stopHover)

    label3_1.bind("<Enter>", label3_1Hover)
    label3_1.bind("<Leave>", stopHover)

    label3_2.bind("<Enter>", label3_2Hover)
    label3_2.bind("<Leave>", stopHover)

    label3_3.bind("<Enter>", label3_3Hover)
    label3_3.bind("<Leave>", stopHover)

    label3_4.bind("<Enter>", label3_4Hover)
    label3_4.bind("<Leave>", stopHover)
