import tkinter 
from tkinter.filedialog import askopenfilenames, asksaveasfilename
fileNames = askopenfilenames()
saveName = asksaveasfilename()
# Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
# filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
# print(filename)

# from tkinter import *

# class Program:

#     def __init__(self):
#         b = Button(text="click me", command=self.callback)
#         b.pack()

#     def callback(self):
#         print("clicked!")

# program = Program()

# mainloop()

