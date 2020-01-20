from tkinter import *

root = Tk()
w = Canvas(root, width=200, height=200)
w.pack()
var = w.create_line(0, 0, 1000, 1000)
w.coords(var, 0, 0, 75, 25)
root.mainloop()