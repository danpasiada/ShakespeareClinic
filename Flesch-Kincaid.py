#filename: Flesch-Kincaid.py
#author: Sam Ness
#purpose: Return a Flesch Grade level score
#tested to work in ipython


import textstat # yoju must first run pip install textstat
#from textstat.textstat import textstat
import tkinter
from tkinter import *
from nltk.tokenize import word_tokenize
from nltk import pos_tag

window = tkinter.Tk()
window.title("FKGL Calculator")

tkinter.Label(window, text = "Hi! Welcome to Flesch-Kincaid Grade Level Calculator!").grid(row=0)
tkinter.Label(window, text = "Please type in the the name of the file you'd like to calculate below").grid(row=1)

tkinter.Label(window, text='File 1').grid(row=2)


e1 = Entry(window)
e1.grid(row=2, column=1)


def fkCalculator():
    window2 = tkinter.Tk()
    window2.title("Calculation Results!")
    tkinter.Label(window2, text="This is the new window")

    # file being read for calculating
    text1 = e1.get()

    f = open(text1)
    raw = f.read()
    textstat.flesch_kincaid_grade(text1)

    tkinter.Label(window2, text = "The Flesch Grade Level Score is {0}".format(textstat.flesch_kincaid_grade(text1))).grid(row=1)

    window2.mainloop()


tkinter.Button(window, text = "Calculate!", command = fkCalculator).grid(row=4)


window.mainloop()
