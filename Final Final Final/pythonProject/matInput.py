import tkinter as tk
from tkinter import ttk
from tkinter import *


# Creating the initial Window to display all materials listed in this application.
def materialInputWindow():
    materialInputs = tk.Toplevel()
    materialInputs.title('Material List for all items in application')
    materialInputs.geometry('400x150')

    # These Labels show all the fully made items in the application.
    label1 = ttk.Label(materialInputs, text='Frost Prime', background='light green', borderwidth=4, relief='solid')
    label1.grid(row=0, column=0, sticky=NW)
    label2 = ttk.Label(materialInputs, text='Rhino Prime', background='light green', borderwidth=4, relief='solid')
    label2.grid(row=0, column=1, sticky=W)
    label3 = ttk.Label(materialInputs, text='Ember Prime', background='light green', borderwidth=4, relief='solid')
    label3.grid(row=0, column=2, sticky=NW)
    label3 = ttk.Label(materialInputs, text='Placeholder Strech', background='', borderwidth=4, relief='solid')
    label3.grid(row=0, column=3, sticky=NW)

    label4 = ttk.Label(materialInputs, text='Boltor Prime', background='light green', borderwidth=4, relief='solid')
    label4.grid(row=1, column=0, sticky=NW)
    label5 = ttk.Label(materialInputs, text='Boar Prime', background='light green', borderwidth=4, relief='solid')
    label5.grid(row=1, column=1, sticky=NW)
    label6 = ttk.Label(materialInputs, text='Braton Prime', background='light green', borderwidth=4, relief='solid')
    label6.grid(row=1, column=2, sticky=NW)

    label7 = ttk.Label(materialInputs, text='Aklex Prime', background='light green', borderwidth=4, relief='solid')
    label7.grid(row=2, column=0, sticky=NW)
    label8 = ttk.Label(materialInputs, text='Lex Prime', background='light green', borderwidth=4, relief='solid')
    label8.grid(row=2, column=1, sticky=NW)
    label9 = ttk.Label(materialInputs, text='Sicarus Prime', background='light green', borderwidth=4, relief='solid')
    label9.grid(row=2, column=2, sticky=NW)

    label10 = ttk.Label(materialInputs, text='Glaive Prime', background='light green', borderwidth=4, relief='solid')
    label10.grid(row=3, column=0, sticky=NW)
    label11 = ttk.Label(materialInputs, text='Ankyros Prime', background='light green', borderwidth=4, relief='solid')
    label11.grid(row=3, column=1, sticky=NW)
    label12 = ttk.Label(materialInputs, text='Fang Prime', background='light green', borderwidth=4, relief='solid')
    label12.grid(row=3, column=2, sticky=NW)

    label13 = ttk.Label(materialInputs, text='Carrier Prime', background='light green', borderwidth=4, relief='solid')
    label13.grid(row=4, column=0, sticky=NW)
    label14 = ttk.Label(materialInputs, text='Dethcube Prime', background='light green', borderwidth=4, relief='solid')
    label14.grid(row=4, column=1, sticky=NW)
    label15 = ttk.Label(materialInputs, text='Shade Prime', background='light green', borderwidth=4, relief='solid')
    label15.grid(row=4, column=2, sticky=NW)
    # Mouseover text to display in a label when you scroll over the above labels, the items needed to make them.
    mouseoverLabel = ttk.Label(materialInputs, text='', border=3)
    mouseoverLabel.grid(row=5, column=0, columnspan=5)

    # Defining an exit button and implementing it underneath so users can exit the window.
    def exit():
        materialInputs.destroy()

    exitButton = ttk.Button(materialInputs, text='EXIT', command=exit)
    exitButton.grid(row=8)

    # A long method of displaying mouseover text for each individual item in the window.
    def label1Hover(e):
        mouseoverLabel.config(text="Blueprints, Neuroptics, Chassis, Systems, 3x Orokin Cell")

    def label2Hover(e):
        mouseoverLabel.config(text="Blueprints, Neuroptics, Chassis, Systems, 3x Orokin Cell")

    def label3Hover(e):
        mouseoverLabel.config(text="Blueprints, Neuroptics, Chassis, Systems, 3x Orokin Cell")

    def label4Hover(e):
        mouseoverLabel.config(text="Blueprint, Barrel, Reciever, Stock, 10x Orokin Cell")

    def label5Hover(e):
        mouseoverLabel.config(text="Blueprint, Barrel, Reciever, Stock, 10x Orokin Cell")

    def label6Hover(e):
        mouseoverLabel.config(text="Blueprint, Barrel, Reciever, Stock, 10x Orokin Cell")

    def label7Hover(e):
        mouseoverLabel.config(text="Blueprint, 2x Lex Prime, Link")

    def label8Hover(e):
        mouseoverLabel.config(text="Blueprint, Barrel, Receiver, 10x Orokin Cell")

    def label9Hover(e):
        mouseoverLabel.config(text="Blueprint, Barrel, Receiver, 10x Orokin Cell")

    def label10Hover(e):
        mouseoverLabel.config(text="Blueprint, Blade, Disk, 10x Orokin Cell")

    def label11Hover(e):
        mouseoverLabel.config(text="Blueprint, Blade, Gauntlet, 10x Orokin Cell")

    def label12Hover(e):
        mouseoverLabel.config(text="Blueprint, 2x Blade, 2x Handle")

    def label13Hover(e):
        mouseoverLabel.config(text="Blueprint, Carapace, Cerebrum, Systems, 6x Orokin Cell")

    def label14Hover(e):
        mouseoverLabel.config(text="Blueprint, Carapace, Cerebrum, Systems, 6x Orokin Cell")

    def label15Hover(e):
        mouseoverLabel.config(text="Blueprint, Carapace, Cerebrum, Systems, 6x Orokin Cell")

    # The action that takes place when you stop hovering over the item.
    def stopHover(e):
        mouseoverLabel.config(text='')

    # <Enter> Is when you initially hover over, it'll display the text above
    # <Leave> Tells the application to display nothing after your mouse leaves the label.
    label1.bind("<Enter>", label1Hover)
    label1.bind("<Leave>", stopHover)

    label2.bind("<Enter>", label2Hover)
    label2.bind("<Leave>", stopHover)

    label3.bind("<Enter>", label3Hover)
    label3.bind("<Leave>", stopHover)

    label4.bind("<Enter>", label4Hover)
    label4.bind("<Leave>", stopHover)

    label5.bind("<Enter>", label5Hover)
    label5.bind("<Leave>", stopHover)

    label6.bind("<Enter>", label6Hover)
    label6.bind("<Leave>", stopHover)

    label7.bind("<Enter>", label7Hover)
    label7.bind("<Leave>", stopHover)

    label8.bind("<Enter>", label8Hover)
    label8.bind("<Leave>", stopHover)

    label9.bind("<Enter>", label9Hover)
    label9.bind("<Leave>", stopHover)

    label10.bind("<Enter>", label10Hover)
    label10.bind("<Leave>", stopHover)

    label11.bind("<Enter>", label11Hover)
    label11.bind("<Leave>", stopHover)

    label12.bind("<Enter>", label12Hover)
    label12.bind("<Leave>", stopHover)

    label13.bind("<Enter>", label13Hover)
    label13.bind("<Leave>", stopHover)

    label14.bind("<Enter>", label14Hover)
    label14.bind("<Leave>", stopHover)

    label15.bind("<Enter>", label15Hover)
    label15.bind("<Leave>", stopHover)

