# Coordination TK


from tkinter import *

root = Tk()

# Create label (venster met tekst of widget)
mylabel1 = Label(root, text = "Hello World!")
mylabel2 = Label(root, text = "I'm the new programer!")

# Let label show on the screen
mylabel1.grid(row = 1, column = 1)       # Column --> verticaal 
mylabel2.grid(row = 4, column = 4)       # Row --> horizontaal

# Alle rijen of colomen moeten waarde hebben om volgende variabele door te kunnen schuiven.

root.mainloop()
