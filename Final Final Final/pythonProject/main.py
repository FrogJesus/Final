import tkinter as tk
from tkinter import ttk
from itemsWindow import itemWindow
from matWindow import materialWindow
from tkinter import *

# Exit button to exit out of the application overall.
def exit():
    window.destroy()


# The initial window opened upon launch, has resolution of screen and title on top left of the window.
window = tk.Tk()
window.geometry('300x100')
window.title('Warframe Helper')


# The Item and Material Buttons
button1 = ttk.Button(window, text='Items', command=itemWindow)
button1.pack(expand=True)

button2 = ttk.Button(window, text='Materials', command=materialWindow)
button2.pack(expand=True)

exitButton = ttk.Button(window, text='EXIT', command=exit)
exitButton.pack(expand=True)

# Runs the program
window.mainloop()
