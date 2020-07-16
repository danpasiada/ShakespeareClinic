# filename: lineEndings.py
# Author: Dan Pasiada, with inspiration from Ieva Burk and the Shakespeare Clinic
# purpose: counts English feminine words
# bugs: # the program thinks husbandry is feminine, because of the -ry ending
# can't hande double spaces

# TODO: check what needs to be installed and how, then provide a manual on how to do that in the README
import string  # for string.punctuation
import os  # for .name
import csv  # for saving as a csv file
import tkinter as tk
from tkinter import Tk, Label, Button, ttk
from tkinter.filedialog import askopenfilenames, asksaveasfilename # to open files and save a file
from tkinter.ttk import *
from tabulate import tabulate  # pip install tabulate #(needs to be installed)


class FemEnd(object):
    def endings():
        ''' 
        create lists or tuples with FEM / MASC words or endings
        used only once 
        '''
        f = open('FEMEND.txt')
        FEMEND = f.read()
        FEMEND = FEMEND.lower()
        FEMEND = tuple(FEMEND.splitlines())  # .endswith works with tuples
        f.close()

        f = open('FemEndWordsTC1.txt')
        FEMWORD = f.read()
        FEMWORD = FEMWORD.lower()
        FEMWORD = FEMWORD.splitlines()
        f.close()

        f = open('MASCEND.txt')
        MASCEND = f.read()
        MASCEND = MASCEND.lower()
        MASCEND = tuple(MASCEND.splitlines())
        f.close()

        f = open('MascExceptions.txt')
        MASCWORD = f.read()
        MASCWORD = MASCWORD.lower()
        MASCWORD = MASCWORD.splitlines()
        f.close()
        return (FEMEND, FEMWORD, MASCEND, MASCWORD)
    ''' class variables for FemEnd '''
    FEMEND, FEMWORD, MASCEND, MASCWORD = endings()

    def __init__(self):
        ''' instance variables for FemEnd '''
        self.text = ''
        self.lines = []
        self.numLines = 0

    def __repr__(self):
        '''
        for debugging, display contents of FemEnd by running:
        NAME = FemEnd()
        NAME.someCommand
        print(NAME)
        '''
        s = ''
        #s += 'Lines: ' + str(self.lines) + '\n\n'
        s += 'Number of Lines: ' + str(self.numLines) + '\n\n'
        s += 'Number of Open Lines: ' + str(countOpenLines()) + '\n\n'
        s += 'Number of FemEnds: ' + str(countFemEnds())
        return s

    def readTextFromFile(self, filename):
        ''' read a text file '''
        # TODO: put this into a parent for each program?
        f = open(filename)  # , encoding = 'utf-8')
        self.text = f.read()
        self.text = self.text.lower()
        f.close()

    def countLines(self):
        ''' count the number of lines in a text '''
        # create list of lines from text with empty lines removed
        self.lines = [i for i in self.text.splitlines() if i]
        # count number of lines in text
        self.numLines = len(self.lines)  

    def countOpenLines(self):
        ''' 
        count lines without punctuation at the end 
        return a percentage of open lines 
        '''
        numOpenLines = 0
        for line in self.lines:
            # if the last character in a line is not a punctuation mark
            if line[-1] not in string.punctuation:
                numOpenLines += 1
        return 100*numOpenLines/self.numLines

    def countFemEnds(self):
        ''' 
        count FEM endings (strategy in the header) 
        return a percentaage of FEM endings
        '''
        # fill the list of last words in each line
        lastWords = []
        numFemEnds = 0
        for line in self.lines:
            # TODO: (1) find a way to delete the empty line.
            # (we tried that in  countOpenLines() with .remove(), filter(), and a list comprehension, but nothing seems to remove all of the empty lines)
            # (2) remove the try/except structure
            try:
                temp = line.split()
                # print(temp)
                lastWords += temp[-1]
            except IndexError:
                # print('')
                # print('')
                # print('error here')
                # print('')
                # print('')
                continue

        # logic from the header
        for word in lastWords:
            # strip punctuation
            word = word.translate(str.maketrans('', '', string.punctuation))
            # if the last word is a FEM word or has a FEM ending and
            if (word in self.FEMWORD) or (word.endswith(self.FEMEND)):
                # and if the last word is not a MASC word and it does not have a MASC ending
                if (word not in self.MASCWORD) and not (word.endswith(self.MASCEND)):
                    numFemEnds += 1
        return 100*numFemEnds/self.numLines

    def countLongLines(self):
        ''' 
        count lines with 11 syllables,
        also known as hendecasyllables
        '''
        # TODO optional, because this will be slower than countFemEnds


class FemEndGUI(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        '''create a GUI '''
        tk.Frame.__init__(self, parent, *args, **kwargs)
        # self.parent = parent

        # box title
        self.master.title('lineEndings')

        self.label1 = Label(parent, text="1. Choose the files")
        self.label1.grid()

        self.getFiles_button = Button(
            parent, text="Browse", command=self.getFiles)
        self.getFiles_button.grid()

        self.label2 = Label(parent, text="2. Run program")
        self.label2.grid()

        self.run_button = Button(
            parent, text="Run", command=self.runProgram, state='disabled')
        self.run_button.grid()

        # TODO: find a more open-source format, maybe CSV?
        self.label3 = Label(parent, text="3. Save output as .csv")
        self.label3.grid()

        self.save_button = Button(
            parent, text="Save", command=self.saveProgram, state='disabled')
        self.save_button.grid()

        self.output = tk.Text(root, height=10, width=63, padx=2, pady=2)
        self.output.insert(tk.END, 'Output will be shown here. \n')

        self.output.grid(row=0, column=1, rowspan=6, sticky='nesw')

        # instance variables for use with FemEnd
        self.fileNames = []  # list of files
        self.data = []  # list of FemEnd Objects

    def getFiles(self):
        ''' 
        ask user for a list of filenames with their directory
        and a .txt extension
        '''
        self.fileNames = askopenfilenames(filetypes=[('Text file', '*.txt')])
        # TODO: potentially allow for other file extensions?
        # check if user has selected files
        if self.fileNames:
            # switch run_button state to normal
            self.run_button['state'] = 'normal'

    def runProgram(self):
        ''' code to run the logic of lineEndings and trigger textbox output'''
        # populate the data with the names of our files (deleting the directory)
        self.data = [os.path.basename(i) for i in self.fileNames]
        # delete extensions from filenames
        self.data = [[os.path.splitext(i)[0]] for i in self.data]

        # populate our data (a 2D list) with the results from analysing the text
        for i, name in enumerate(self.data):
            temp = FemEnd()
            # TODO change this to read from list
            temp.readTextFromFile(self.fileNames[i])
            temp.countLines()
            openLines = temp.countOpenLines()
            femEnds = temp.countFemEnds()
            name += [str(temp.numLines), str(openLines),
                     str(femEnds)]
        # trigger textbox output
        self.textOutput()
        # switch save_button state to normal
        self.save_button['state'] = 'normal'

    def textOutput(self):
        ''' print data as pure text in a GUI textbox '''
        # delete previous contents of the textbox
        self.output.delete(1.0, tk.END)
        # insert the top row (titles for each column)
        self.data.insert(
            0, ['Text Name', 'Lines', 'Open Lines (%)', 'Feminine Endings (%)'])
        # format the text output as a table
        table = tabulate(self.data[1:], headers=self.data[0], tablefmt='plain')
        # insert the now pretty table into the output box
        self.output.insert(tk.END, table)
        # TODO: make this unlock the save button

    def saveProgram(self):
        ''' saves the output in a user-chosen directory, in csv format '''
        fileName = asksaveasfilename(
            defaultextension=".csv", filetypes=[('CSV', '*.csv')])
        with open(fileName, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(self.data)


if __name__ == '__main__':
    root = tk.Tk()
    FemEndGUI(root).grid()
    # expand the textbox east, if output is too long
    root.grid_columnconfigure(1, weight=1)
    root.mainloop()
