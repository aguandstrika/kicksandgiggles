# Import Module
from tkinter import *

# create root window
root = Tk()

# root window title and dimension
root.title("junk foods")
# Set geometry(widthxheight)
root.geometry('350x200')

# adding a label to the root window
lbl = Label(root, text="random junk food")
lbl.grid()

# function to display text when
# button is clicked


def clicked():    
    #a simple junk food seceltor
    junk_Food_randomizer = {'Pizza', 'Hot Dog', 'Hamburger'}
    for e in junk_Food_randomizer:
        print(e)
        break
    lbl.configure(text=e)


# button widget with red color text
# inside
btn = Button(root, text="Click me",
             fg="red", command=clicked)
# set Button grid
btn.grid(column=1, row=0)

# Execute Tkinter
root.mainloop()
