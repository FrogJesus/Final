import tkinter as tk
from tkinter import ttk
from tkinter import *


# Defining the companions list window.
def companions():
    companionsList = tk.Toplevel()
    companionsList.title('Companions')
    companionsList.geometry('200x380')

    # Displays in labels the items needed to make these companions.
    label1 = ttk.Label(companionsList, text='Carrier Prime Blueprint', background='Yellow')
    label1_1 = ttk.Label(companionsList, text='Carrier Prime Carapace', background='Yellow')
    label1_2 = ttk.Label(companionsList, text='Carrier Prime Cerebrum', background='Yellow')
    label1_3 = ttk.Label(companionsList, text='Carrier Prime Systems', background='Yellow')
    label1_4 = ttk.Label(companionsList, text='6x Orokin Cell', background='Yellow')
    label1.grid(row=0, column=0, sticky='nw')
    label1_1.grid(row=1, column=0, sticky='nw')
    label1_2.grid(row=2, column=0, sticky='nw')
    label1_3.grid(row=3, column=0, sticky='nw')
    label1_4.grid(row=4, column=0, sticky='nw')

    # Filler label to create an empty row to make it slightly better visually.
    labelFiller = ttk.Label(companionsList, text='', background='White')
    labelFiller.grid(row=5, column=0, sticky='nw')

    label2 = ttk.Label(companionsList, text='Dethcube Prime Blueprint', background='Yellow')
    label2_1 = ttk.Label(companionsList, text='Dethcube Prime Carapace', background='Yellow')
    label2_2 = ttk.Label(companionsList, text='Dethcube Prime Cerebrum', background='Yellow')
    label2_3 = ttk.Label(companionsList, text='Dethcube Prime Systems', background='Yellow')
    label2_4 = ttk.Label(companionsList, text='6x Orokin Cell', background='Yellow')
    label2.grid(row=6, column=0, sticky='nw')
    label2_1.grid(row=7, column=0, sticky='nw')
    label2_2.grid(row=8, column=0, sticky='nw')
    label2_3.grid(row=9, column=0, sticky='nw')
    label2_4.grid(row=10, column=0, sticky='nw')

    # Filler label to create an empty row to make it slightly better visually.
    labelFiller2 = ttk.Label(companionsList, text='', background='White')
    labelFiller2.grid(row=11, column=0, sticky='nw')

    label3 = ttk.Label(companionsList, text='Shade Prime Blueprint', background='Yellow')
    label3_1 = ttk.Label(companionsList, text='Shade Prime Carapace', background='Yellow')
    label3_2 = ttk.Label(companionsList, text='Shade Prime Cerebrum', background='Yellow')
    label3_3 = ttk.Label(companionsList, text='Shade Prime Systems', background='Yellow')
    label3_4 = ttk.Label(companionsList, text='6x Orokin Cell', background='Yellow')
    label3.grid(row=12, column=0, sticky='nw')
    label3_1.grid(row=13, column=0, sticky='nw')
    label3_2.grid(row=14, column=0, sticky='nw')
    label3_3.grid(row=15, column=0, sticky='nw')
    label3_4.grid(row=16, column=0, sticky='nw')

    # The mouseover label text at the bottom that displays where to find these items.
    mouseoverLabel = ttk.Label(companionsList, text='', border=1, relief=SUNKEN, anchor=E)
    mouseoverLabel.grid(row=17, columnspan=10, ipady=2)

    # Defining an exit button and implementing it underneath so users can exit the window.
    def exit():
        companionsList.destroy()

    exitButton = ttk.Button(companionsList, text='EXIT', command=exit)
    exitButton.grid(row=18, columnspan=10)

    # Defining what text is displayed for each individual item.
    def label1Hover(e):
        mouseoverLabel.config(text="Relics: Lith V7, Meso P12, V1, V3")

    def label1_1Hover(e):
        mouseoverLabel.config(text="Relics: Axi N2, Lith S5, V10")

    def label1_2Hover(e):
        mouseoverLabel.config(text="Relics: Lith C1, Meso C1, C2, C7")

    def label1_3Hover(e):
        mouseoverLabel.config(text="Relics: Axi A7, K12, V1, Lith N2")

    def label1_4Hover(e):
        mouseoverLabel.config(text="Saturn, Ceres, Deimos")

    def label2Hover(e):
        mouseoverLabel.config(text="Relics: Lith D1, D3, D4, Neo D3")

    def label2_1Hover(e):
        mouseoverLabel.config(text="Relics: Axi N7, Lith M6, T4, V9")

    def label2_2Hover(e):
        mouseoverLabel.config(text="Relics: Lith D2, Meso D4, D6, Neo A7")

    def label2_3Hover(e):
        mouseoverLabel.config(text="Relics: Axi I1, P2, Lith B8, S10")

    def label2_4Hover(e):
        mouseoverLabel.config(text="Saturn, Ceres, Deimos")

    def label3Hover(e):
        mouseoverLabel.config(text="Relics: Axi A18, W3, Meso B9, N14")

    def label3_1Hover(e):
        mouseoverLabel.config(text="Relics: Neo S18, Lith S15")

    def label3_2Hover(e):
        mouseoverLabel.config(text="Relics: Axi G11, Meso W5, Neo F2, N22")

    def label3_3Hover(e):
        mouseoverLabel.config(text="Relics: Lith A6, Axi B6, Meso P14")

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
