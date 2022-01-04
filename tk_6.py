# Using icomns and images 

from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Icon Test")
root.iconbitmap("images/icon.icns")

my_img = ImageTk.PhotoImage(Image.open("images/image.png"))

my_label = Label(image = my_img)
button_quit = Button(root, text = "Exit Program", command = root.quit)
my_label.pack()
button_quit.pack()


root.mainloop()
