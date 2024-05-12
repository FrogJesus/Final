import tkinter as tk
from tkinter import ttk
from tkinter import *


# The creation of the Warframes window that displays Warframes.
def warframes():
    warframesList = tk.Toplevel()
    warframesList.title('Warframes')
    warframesList.geometry('500x400')

    # These labels show you what you need for different Warframes.
    label1 = ttk.Label(warframesList, text='Frost Prime Blueprint', background='Yellow')
    label1_1 = ttk.Label(warframesList, text='Frost Prime Neuroptics', background='Yellow')
    label1_2 = ttk.Label(warframesList, text='Frost Prime Chassis', background='Yellow')
    label1_3 = ttk.Label(warframesList, text='Frost Prime Systems', background='Yellow')
    label1_4 = ttk.Label(warframesList, text='3x Orokin Cell', background='Yellow')
    label1.grid(row=0, column=0, sticky='nw')
    label1_1.grid(row=1, column=0, sticky='nw')
    label1_2.grid(row=2, column=0, sticky='nw')
    label1_3.grid(row=3, column=0, sticky='nw')
    label1_4.grid(row=4, column=0, sticky='nw')

    # Unlike Weapons Warframes require a more thorough build path so we show what you need for the
    # Neuroptics, Chassis, and Systems
    label2 = ttk.Label(warframesList, text='Frost Prime Neuroptics', background='Yellow')
    label2_1 = ttk.Label(warframesList, text='150x Alloy Plate', background='Yellow')
    label2_2 = ttk.Label(warframesList, text='1x Neural Censor', background='Yellow')
    label2_3 = ttk.Label(warframesList, text='150x Polymer Bundle', background='Yellow')
    label2_4 = ttk.Label(warframesList, text='500x Rubedo', background='Yellow')
    label2.grid(row=0, column=1, sticky='nw')
    label2_1.grid(row=1, column=1, sticky='nw')
    label2_2.grid(row=2, column=1, sticky='nw')
    label2_3.grid(row=3, column=1, sticky='nw')
    label2_4.grid(row=4, column=1, sticky='nw')

    label3 = ttk.Label(warframesList, text='Frost Prime Chassis', background='Yellow')
    label3_1 = ttk.Label(warframesList, text='1000x Ferrite', background='Yellow')
    label3_2 = ttk.Label(warframesList, text='1x Morphics', background='Yellow')
    label3_3 = ttk.Label(warframesList, text='300x Rubedo', background='Yellow')
    label3.grid(row=0, column=3, sticky='nw')
    label3_1.grid(row=1, column=3, sticky='nw')
    label3_2.grid(row=2, column=3, sticky='nw')
    label3_3.grid(row=3, column=3, sticky='nw')

    label4 = ttk.Label(warframesList, text='Frost Prime Systems', background='Yellow')
    label4_1 = ttk.Label(warframesList, text='1x Control Module', background='Yellow')
    label4_2 = ttk.Label(warframesList, text='1x Morphics', background='Yellow')
    label4_3 = ttk.Label(warframesList, text='500x Salvage', background='Yellow')
    label4_4 = ttk.Label(warframesList, text='220x Plastids', background='Yellow')
    label4.grid(row=0, column=4, sticky='nw')
    label4_1.grid(row=1, column=4, sticky='nw')
    label4_2.grid(row=2, column=4, sticky='nw')
    label4_3.grid(row=3, column=4, sticky='nw')
    label4_4.grid(row=4, column=4, sticky='nw')

    # Filler label to create an empty row to make it slightly better visually.
    labelFiller = ttk.Label(warframesList, text='', background='White')
    labelFiller.grid(row=5, column=0, sticky='nw')

    label5 = ttk.Label(warframesList, text='Rhino Prime Blueprint', background='Yellow')
    label5_1 = ttk.Label(warframesList, text='Rhino Prime Neuroptics', background='Yellow')
    label5_2 = ttk.Label(warframesList, text='Rhino Prime Chassis', background='Yellow')
    label5_3 = ttk.Label(warframesList, text='Rhino Prime Systems', background='Yellow')
    label5_4 = ttk.Label(warframesList, text='3x Orokin Cell', background='Yellow')
    label5.grid(row=6, column=0, sticky='nw')
    label5_1.grid(row=7, column=0, sticky='nw')
    label5_2.grid(row=8, column=0, sticky='nw')
    label5_3.grid(row=9, column=0, sticky='nw')
    label5_4.grid(row=10, column=0, sticky='nw')

    label6 = ttk.Label(warframesList, text='Rhino Prime Neuroptics', background='Yellow')
    label6_1 = ttk.Label(warframesList, text='150x Alloy Plate', background='Yellow')
    label6_2 = ttk.Label(warframesList, text='2x Neural Censor', background='Yellow')
    label6_3 = ttk.Label(warframesList, text='150x Polymer Bundle', background='Yellow')
    label6_4 = ttk.Label(warframesList, text='750x Rubedo', background='Yellow')
    label6.grid(row=6, column=1, sticky='nw')
    label6_1.grid(row=7, column=1, sticky='nw')
    label6_2.grid(row=8, column=1, sticky='nw')
    label6_3.grid(row=9, column=1, sticky='nw')
    label6_4.grid(row=10, column=1, sticky='nw')

    label7 = ttk.Label(warframesList, text='Rhino Prime Chassis', background='Yellow')
    label7_1 = ttk.Label(warframesList, text='1000x Ferrite', background='Yellow')
    label7_2 = ttk.Label(warframesList, text='3x Morphics', background='Yellow')
    label7_3 = ttk.Label(warframesList, text='400x Plastids', background='Yellow')
    label7.grid(row=6, column=3, sticky='nw')
    label7_1.grid(row=7, column=3, sticky='nw')
    label7_2.grid(row=8, column=3, sticky='nw')
    label7_3.grid(row=9, column=3, sticky='nw')

    label8 = ttk.Label(warframesList, text='Rhino Prime Systems', background='Yellow')
    label8_1 = ttk.Label(warframesList, text='3x Control Module', background='Yellow')
    label8_2 = ttk.Label(warframesList, text='1x Morphics', background='Yellow')
    label8_3 = ttk.Label(warframesList, text='500x Ferrite', background='Yellow')
    label8_4 = ttk.Label(warframesList, text='500x Plastids', background='Yellow')
    label8.grid(row=6, column=4, sticky='nw')
    label8_1.grid(row=7, column=4, sticky='nw')
    label8_2.grid(row=8, column=4, sticky='nw')
    label8_3.grid(row=9, column=4, sticky='nw')
    label8_4.grid(row=10, column=4, sticky='nw')

    # Filler label to create an empty row to make it slightly better visually.
    labelFiller2 = ttk.Label(warframesList, text='', background='White')
    labelFiller2.grid(row=11, column=0, sticky='nw')

    label9 = ttk.Label(warframesList, text='Ember Prime Blueprint', background='Yellow')
    label9_1 = ttk.Label(warframesList, text='Ember Prime Neuroptics', background='Yellow')
    label9_2 = ttk.Label(warframesList, text='Ember Prime Chassis', background='Yellow')
    label9_3 = ttk.Label(warframesList, text='Ember Prime Systems', background='Yellow')
    label9_4 = ttk.Label(warframesList, text='1x Orokin Cell', background='Yellow')
    label9.grid(row=12, column=0, sticky='nw')
    label9_1.grid(row=13, column=0, sticky='nw')
    label9_2.grid(row=14, column=0, sticky='nw')
    label9_3.grid(row=15, column=0, sticky='nw')
    label9_4.grid(row=16, column=0, sticky='nw')

    label10 = ttk.Label(warframesList, text='Ember Prime Neuroptics', background='Yellow')
    label10_1 = ttk.Label(warframesList, text='150x Alloy Plate', background='Yellow')
    label10_2 = ttk.Label(warframesList, text='2x Neural Censor', background='Yellow')
    label10_3 = ttk.Label(warframesList, text='1000x Polymer Bundle', background='Yellow')
    label10_4 = ttk.Label(warframesList, text='750x Rubedo', background='Yellow')
    label10.grid(row=12, column=1, sticky='nw')
    label10_1.grid(row=13, column=1, sticky='nw')
    label10_2.grid(row=14, column=1, sticky='nw')
    label10_3.grid(row=15, column=1, sticky='nw')
    label10_4.grid(row=16, column=1, sticky='nw')

    label11 = ttk.Label(warframesList, text='Ember Prime Chassis', background='Yellow')
    label11_1 = ttk.Label(warframesList, text='1000x Ferrite', background='Yellow')
    label11_2 = ttk.Label(warframesList, text='3x Morphics', background='Yellow')
    label11_3 = ttk.Label(warframesList, text='300x Rubedo', background='Yellow')
    label11.grid(row=12, column=3, sticky='nw')
    label11_1.grid(row=13, column=3, sticky='nw')
    label11_2.grid(row=14, column=3, sticky='nw')
    label11_3.grid(row=15, column=3, sticky='nw')

    label12 = ttk.Label(warframesList, text='Ember Prime Systems', background='Yellow')
    label12_1 = ttk.Label(warframesList, text='1x Control Module', background='Yellow')
    label12_2 = ttk.Label(warframesList, text='1x Morphics', background='Yellow')
    label12_3 = ttk.Label(warframesList, text='1,200x Nanospores', background='Yellow')
    label12_4 = ttk.Label(warframesList, text='700x Plastids', background='Yellow')
    label12.grid(row=12, column=4, sticky='nw')
    label12_1.grid(row=13, column=4, sticky='nw')
    label12_2.grid(row=14, column=4, sticky='nw')
    label12_3.grid(row=15, column=4, sticky='nw')
    label12_4.grid(row=16, column=4, sticky='nw')

    # The mouseover label text at the bottom that displays where to find these items.
    mouseoverLabel = ttk.Label(warframesList, text='', border=1, relief=SUNKEN, anchor=E)
    mouseoverLabel.grid(row=17, columnspan=10, ipady=2)

    # Defining an exit button and implementing it underneath so users can exit the window.
    def exit():
        warframesList.destroy()

    exitButton = ttk.Button(warframesList, text='EXIT', command=exit)
    exitButton.grid(row=18, columnspan=10)

    # Defining what text is displayed for each individual item.
    def label1Hover(e):
        mouseoverLabel.config(text="Relics: Meso F2, F3, F4, Neo F1")

    def label1_1Hover(e):
        mouseoverLabel.config(text="Relics: Axi D4, E1, Neo E1")

    def label1_2Hover(e):
        mouseoverLabel.config(text="Relics: Lith G1, Meso E1, Neo B8")

    def label1_3Hover(e):
        mouseoverLabel.config(text="Relics: Lith G2, M8, Neo S5")

    def label1_4Hover(e):
        mouseoverLabel.config(text="Saturn, Ceres, Deimos")

    def label2Hover(e):
        mouseoverLabel.config(text="Relics: Axi D4, E1, Neo E1")

    def label2_1Hover(e):
        mouseoverLabel.config(text="Venus, Jupiter, Sedna, Ceres, Phobos, Pluto")

    def label2_2Hover(e):
        mouseoverLabel.config(text="Jupiter, Kuva Fortress")

    def label2_3Hover(e):
        mouseoverLabel.config(text="Mercury, Venus, Uranus")

    def label2_4Hover(e):
        mouseoverLabel.config(text="Phobos, Earth, Pluto, Europa, Sedna, and The Void")

    def label3Hover(e):
        mouseoverLabel.config(text="Relics: Lith G1, Meso E1, Neo B8")

    def label3_1Hover(e):
        mouseoverLabel.config(text="Mercury, Earth, Neptune, The Void, Zariman Ten Zero")

    def label3_2Hover(e):
        mouseoverLabel.config(text="Mercury, Mars, Phobos, Europa, Pluto")

    def label3_3Hover(e):
        mouseoverLabel.config(text="Phobos, Earth, Pluto, Europa, Sedna, and The Void")

    def label4Hover(e):
        mouseoverLabel.config(text="Relics: Lith G2, M8, Neo S5")

    def label4_1Hover(e):
        mouseoverLabel.config(text="Europa, Neptune, The Void")

    def label4_2Hover(e):
        mouseoverLabel.config(text="Mercury, Mars, Phobos, Europa, Pluto")

    def label4_3Hover(e):
        mouseoverLabel.config(text="Mars, Jupiter, Sedna")

    def label4_4Hover(e):
        mouseoverLabel.config(text="Phobos, Saturn, Uranus, Pluto, Eris")

    def label5Hover(e):
        mouseoverLabel.config(text="Relics: Axi R1, Neo R1")

    def label5_1Hover(e):
        mouseoverLabel.config(text="Relics: Lith B1, B4")

    def label5_2Hover(e):
        mouseoverLabel.config(text="Relics: Meso M1, N6")

    def label5_3Hover(e):
        mouseoverLabel.config(text="Relics: Axi S3, Neo B3")

    def label5_4Hover(e):
        mouseoverLabel.config(text="Saturn, Ceres, Deimos")

    def label6Hover(e):
        mouseoverLabel.config(text="Relics: Lith B1, B4")

    def label6_1Hover(e):
        mouseoverLabel.config(text="Venus, Jupiter, Pluto, Sedna")

    def label6_2Hover(e):
        mouseoverLabel.config(text="Jupiter")

    def label6_3Hover(e):
        mouseoverLabel.config(text="Mercury, Venus, Uranus")

    def label6_4Hover(e):
        mouseoverLabel.config(text="Earth, Lua, Phobos, Europa, Pluto, Sedna, The Void")

    def label7Hover(e):
        mouseoverLabel.config(text="Relics: Meso M1, N6")

    def label7_1Hover(e):
        mouseoverLabel.config(text="Mercury, Earth, Lua, Neptune, The Void")

    def label7_2Hover(e):
        mouseoverLabel.config(text="Mercury, Mars, Phobos, Europa, Pluto")

    def label7_3Hover(e):
        mouseoverLabel.config(text="Phobos, Saturn, Uranus, Pluto, Eris")

    def label8Hover(e):
        mouseoverLabel.config(text="Relics: Axi S3, Neo B3")

    def label8_1Hover(e):
        mouseoverLabel.config(text="Europa, Neptune, The Void")

    def label8_2Hover(e):
        mouseoverLabel.config(text="Mercury, Mars, Phobos, Europa, Pluto")

    def label8_3Hover(e):
        mouseoverLabel.config(text="Mercury, Earth, Lua, Neptune, The Void")

    def label8_4Hover(e):
        mouseoverLabel.config(text="Phobos, Saturn, Uranus, Pluto, Eris")

    def label9Hover(e):
        mouseoverLabel.config(text="Axi E1, Meso E1, Neo E1")

    def label9_1Hover(e):
        mouseoverLabel.config(text="Meso F3, Neo S5")

    def label9_2Hover(e):
        mouseoverLabel.config(text="Meso F2, Neo F1")

    def label9_3Hover(e):
        mouseoverLabel.config(text="Axi S2, Lith G1")

    def label9_4Hover(e):
        mouseoverLabel.config(text="Saturn, Ceres, Deimos")

    def label10Hover(e):
        mouseoverLabel.config(text="Meso F3, Neo S5")

    def label10_1Hover(e):
        mouseoverLabel.config(text="Venus, Phobos, Ceres, Jupiter, Pluto, Sedna")

    def label10_2Hover(e):
        mouseoverLabel.config(text="Jupiter")

    def label10_3Hover(e):
        mouseoverLabel.config(text="Mercury, Venus, Uranus")

    def label10_4Hover(e):
        mouseoverLabel.config(text="Earth, Lua, Phobos, Europa, Pluto, Sedna, The Void")

    def label11Hover(e):
        mouseoverLabel.config(text="Meso F2, Neo F1")

    def label11_1Hover(e):
        mouseoverLabel.config(text="Mercury, Earth, Lua, Neptune, The Void")

    def label11_2Hover(e):
        mouseoverLabel.config(text="Mercury, Mars, Phobos, Europa, Pluto")

    def label11_3Hover(e):
        mouseoverLabel.config(text="Earth, Lua, Phobos, Europa, Pluto, Sedna, The Void")

    def label12Hover(e):
        mouseoverLabel.config(text="Axi S2, Lith G1")

    def label12_1Hover(e):
        mouseoverLabel.config(text="Europa, Neptune, The Void")

    def label12_2Hover(e):
        mouseoverLabel.config(text="Mercury, Mars, Phobos, Europa, Pluto")

    def label12_3Hover(e):
        mouseoverLabel.config(text="Saturn, Neptune, Eris, Deimos")

    def label12_4Hover(e):
        mouseoverLabel.config(text="Phobos, Saturn, Uranus, Pluto, Eris")

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

    label4.bind("<Enter>", label4Hover)
    label4.bind("<Leave>", stopHover)

    label4_1.bind("<Enter>", label4_1Hover)
    label4_1.bind("<Leave>", stopHover)

    label4_2.bind("<Enter>", label4_2Hover)
    label4_2.bind("<Leave>", stopHover)

    label4_3.bind("<Enter>", label4_3Hover)
    label4_3.bind("<Leave>", stopHover)

    label4_4.bind("<Enter>", label4_4Hover)
    label4_4.bind("<Leave>", stopHover)

    label5.bind("<Enter>", label5Hover)
    label5.bind("<Leave>", stopHover)

    label5_1.bind("<Enter>", label5_1Hover)
    label5_1.bind("<Leave>", stopHover)

    label5_2.bind("<Enter>", label5_2Hover)
    label5_2.bind("<Leave>", stopHover)

    label5_3.bind("<Enter>", label5_3Hover)
    label5_3.bind("<Leave>", stopHover)

    label5_4.bind("<Enter>", label5_4Hover)
    label5_4.bind("<Leave>", stopHover)

    label6.bind("<Enter>", label6Hover)
    label6.bind("<Leave>", stopHover)

    label6_1.bind("<Enter>", label6_1Hover)
    label6_1.bind("<Leave>", stopHover)

    label6_2.bind("<Enter>", label6_2Hover)
    label6_2.bind("<Leave>", stopHover)

    label6_3.bind("<Enter>", label6_3Hover)
    label6_3.bind("<Leave>", stopHover)

    label6_4.bind("<Enter>", label6_4Hover)
    label6_4.bind("<Leave>", stopHover)

    label7.bind("<Enter>", label7Hover)
    label7.bind("<Leave>", stopHover)

    label7_1.bind("<Enter>", label7_1Hover)
    label7_1.bind("<Leave>", stopHover)

    label7_2.bind("<Enter>", label7_2Hover)
    label7_2.bind("<Leave>", stopHover)

    label7_3.bind("<Enter>", label7_3Hover)
    label7_3.bind("<Leave>", stopHover)

    label8.bind("<Enter>", label8Hover)
    label8.bind("<Leave>", stopHover)

    label8_1.bind("<Enter>", label8_1Hover)
    label8_1.bind("<Leave>", stopHover)

    label8_2.bind("<Enter>", label8_2Hover)
    label8_2.bind("<Leave>", stopHover)

    label8_3.bind("<Enter>", label8_3Hover)
    label8_3.bind("<Leave>", stopHover)

    label8_4.bind("<Enter>", label8_4Hover)
    label8_4.bind("<Leave>", stopHover)

    label9.bind("<Enter>", label9Hover)
    label9.bind("<Leave>", stopHover)

    label9_1.bind("<Enter>", label9_1Hover)
    label9_1.bind("<Leave>", stopHover)

    label9_2.bind("<Enter>", label9_2Hover)
    label9_2.bind("<Leave>", stopHover)

    label9_3.bind("<Enter>", label9_3Hover)
    label9_3.bind("<Leave>", stopHover)

    label9_4.bind("<Enter>", label9_4Hover)
    label9_4.bind("<Leave>", stopHover)

    label10.bind("<Enter>", label10Hover)
    label10.bind("<Leave>", stopHover)

    label10_1.bind("<Enter>", label10_1Hover)
    label10_1.bind("<Leave>", stopHover)

    label10_2.bind("<Enter>", label10_2Hover)
    label10_2.bind("<Leave>", stopHover)

    label10_3.bind("<Enter>", label10_3Hover)
    label10_3.bind("<Leave>", stopHover)

    label10_4.bind("<Enter>", label10_4Hover)
    label10_4.bind("<Leave>", stopHover)

    label11.bind("<Enter>", label11Hover)
    label11.bind("<Leave>", stopHover)

    label11_1.bind("<Enter>", label11_1Hover)
    label11_1.bind("<Leave>", stopHover)

    label11_2.bind("<Enter>", label11_2Hover)
    label11_2.bind("<Leave>", stopHover)

    label11_3.bind("<Enter>", label11_3Hover)
    label11_3.bind("<Leave>", stopHover)

    label12.bind("<Enter>", label12Hover)
    label12.bind("<Leave>", stopHover)

    label12_1.bind("<Enter>", label12_1Hover)
    label12_1.bind("<Leave>", stopHover)

    label12_2.bind("<Enter>", label12_2Hover)
    label12_2.bind("<Leave>", stopHover)

    label12_3.bind("<Enter>", label12_3Hover)
    label12_3.bind("<Leave>", stopHover)

    label12_4.bind("<Enter>", label12_4Hover)
    label12_4.bind("<Leave>", stopHover)
