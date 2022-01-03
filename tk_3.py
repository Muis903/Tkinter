# Creating bottons

from tkinter import *
# from tkmacosx import Button
import random

root = Tk()

# Functions 

def generate_random_cifer():
    cifer = Label(root, text = random.randint(1, 99999), )
    cifer.pack()

# Button
myButton = Button(root, text = "Click me!", padx = 70, pady = 60,   #Sizes: padx - horizontaal, pady - verticaal
    command = generate_random_cifer,   # command - call the function if button is pressed.
    fg = "green", highlightbackground = "red") # fg - text collor, bg - background collor 
    #(Doesn't work on Mac OS), Use 'highlightbackground' of install 'tkmacosx'.

# Place button on screen
myButton.pack()

root.mainloop()
