# Creating imput fileds

from tkinter import *
import random

root = Tk()

# Imput = Entry

# Create an input filed
e = Entry(root, width = 50, fg = "purple", borderwidth = 10)  # Arguments: root, sizes (width, height), fg, bg, borderwidth
# Place input filed
e.pack()
# Use input (like return)
# e.get()
e.insert(0, "Enter an cifer")

# Functions 

def generate_random_cifer():
    cifer = Label(root, text = random.randint(1, int(e.get())))
    cifer.pack()

# Button
myButton = Button(root, text = "Click me!", padx = 70, pady = 60,   #Sizes: padx - horizontaal, pady - verticaal
    command = generate_random_cifer)   # command - call the function if button is pressed.

# Place button on screen
myButton.pack()

root.mainloop()
