#filename: whileCount.py
#authors: Dan Pasiada and Sam Ness, Shakespeare Clinic
#purpose: counts amount of time 'while' is used as a noun
#tested to work in ipython -- seems to always return 4 noun plurals and 0 noun singulars uses; errors with unicode characters


import tkinter
from tkinter import *
from nltk.tokenize import word_tokenize
from nltk import pos_tag

window = tkinter.Tk()
window.title("While Count")

tkinter.Label(window, text = "Hi! Let's count how many 'while's that are nouns there are!").grid(row=0)
tkinter.Label(window, text = "Please type in the name for the file you'd like to analyze").grid(row=1)

tkinter.Label(window, text='File 1').grid(row=2)

e1 = Entry(window)
e1.grid(row=2, column=1)

def posCounter():
    window2 = tkinter.Tk()
    window2.title("Count Results!")
    tkinter.Label(window2, text="This is the new window")
    scrollbar = Scrollbar(window2)

    listbox = Listbox(window2, yscrollcommand=scrollbar.set, height = 20, width = 150)
    """for i in range(1000):
        listbox.insert(END, str(i))"""
    listbox.grid(column=0)

    scrollbar.config(command=listbox.yview)

    # dictionaries: key = POS tag, value = POS count
    posDic = {'NN':0, 'NNS':0}

    # files being read for tokenizing/ pos tagging
    text1 = e1.get()

    f = open(text1)
    raw = f.read()

    tokList = word_tokenize(raw)

    for i in tokList:
        if i == 'while':
            posList = pos_tag(i)

    # increasing value of POS key everytime POS tag appears
    for (token, pos) in posList: #UnboundLocalError: local variable 'posList' referenced before assignment
        if pos not in posDic.keys():
            pass
        else:
            posDic[pos] += 1


    listbox.insert(0, "There are {0} whiles that are nouns, singular in {1}!".format((posDic['NN']), text1))
    listbox.insert(1, "There are {0} whiles that are nouns plural in {1}!".format((posDic['NNS']), text1))



    window2.mainloop()


tkinter.Button(window, text = "Compare!", command = posCounter).grid(row=4)


window.mainloop()
