# Adding the frame to the app


from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Learn adding frame.")

frame = LabelFrame(root, padx = 25, pady = 25)


b = Button (frame, text = "Don't click here.")
b2 = Button (frame, text = "or here...")

frame.pack(padx = 100, pady = 100,)
b.grid(row = 0, column = 0)
b2.grid(row = 1, column = 1)

root.mainloop()
