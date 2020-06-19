# filename: lineEndings.py
# Author: Dan Pasiada, with inspiration from Ieva Burk and the Shakespeare Clinic
# purpose: counts English feminine words 
# bugs: # the program thinks husbandry is feminine, because of the -ry ending
        # can't hande double spaces
# TODO: acknowledge QT
        
import string #for string.punctuation
import tkinter as tk
from tkinter import Tk, Label, Button
from tkinter.filedialog import askopenfilenames, asksaveasfilename # to open files and save a file

class FemEnd(object):
    def __init__(self):
        '''create empty FemEnd '''
        self.text = ''
        self.lines = [] 
        self.numLines = 0
        self.numOpenLines = 0
        self.numFemEnds = 0
        self.lastWords = []

    def __repr__(self):
        '''
        display contents of FemEnd by running:
        NAME = FemEnd()
        NAME.someCommand
        print(NAME)
        '''
        s = ''
        #s += 'Lines: ' + str(self.lines) + '\n\n'
        s += 'Number of Lines: ' + str(self.numLines) + '\n\n'
        s += 'Number of Open Lines: ' + str(self.numOpenLines) + '\n\n'
        s += 'Number of FemEnds: ' + str(self.numFemEnds)
        #s += str(self.property2)
        return s

    def excelOutput(self):
        ''' output results in .xlsx spreadsheet format '''
        # TODO: but in the common interface for all programs

    def readTextFromFile(self, filename):
        ''' read a text file '''
        #TODO: put this into a parent for each program?
        f = open(filename) #, encoding = 'utf-8') 
        self.text = f.read()
        self.text = self.text.lower()
        f.close()

    def countLines(self):
        ''' count the number of lines in a text '''
        self.lines = [i for i in self.text.splitlines() if i] # list of lines from text with empty lines removed
        self.numLines = len(self.lines) # number of lines in text

    def countOpenLines(self):
        ''' count lines without punctuation at the end'''
        for line in self.lines:
            #if the last character in a line is not a punctuation mark
            if line[-1] not in string.punctuation: 
                self.numOpenLines += 1

    def countFemEnds(self):
        ''' count FEM endings (strategy in the header) '''
        # create lists or tuples with FEM / MASC words or endings
        f = open('FEMEND.txt')
        FEMEND = f.read()
        FEMEND = FEMEND.lower()
        FEMEND = tuple(FEMEND.splitlines()) #.endswith works with tuples
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

        #fill the list of last words in each line
        for line in self.lines:
            # TODO: (1) find a way to delete the empty line.
            # (we tried that in  countOpenLines() with .remove(), filter(), and a list comprehension, but nothing seems to remove all of the empty lines)
            # (2) remove the try/except structure
            try:
                temp = line.split()
                # print(temp)
                self.lastWords += temp[-1]
            except IndexError: 
                # print('')
                # print('')
                # print('error here')
                # print('')
                # print('')
                continue

        #logic from the header
        for word in self.lastWords:
            # strip punctuation
            word = word.translate(str.maketrans('', '', string.punctuation))
            #if the last word is a FEM word or has a FEM ending and
            if (word in FEMWORD) or (word.endswith(FEMEND)):
                # and if the last word is not a MASC word and it does not have a MASC ending
                if (word not in MASCWORD) and not (word.endswith(MASCEND)):
                    self.numFemEnds += 1

    def countLongLines(self):
        ''' count lines with 11 syllables,
            also known as hendecasyllables
        '''
        # TODO optional, because this will be slower than countFemEnds


class FemEndGUI(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        '''create a GUI '''
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        
        # self.master = master
        # master.title("lineEndings")

        self.label1 = Label(parent, text="1. Choose the files")
        self.label1.pack()

        self.getFiles_button = Button(parent, text="Browse", command=self.getFiles)
        self.getFiles_button.pack()

        self.label2 = Label(parent, text="2. Run program")
        self.label2.pack()

        self.run_button = Button(parent, text="Run", command=self.runProgram)
        self.run_button.pack()

        self.label3 = Label(parent, text="3. Save output")
        self.label3.pack()

        self.run_button = Button(parent, text="Save", command=self.saveProgram)
        self.run_button.pack()

        # properties that will change
        self.fileNames = []

    def getFiles(self):
        ''' get a list of filenames with a .txt extension'''
        self.fileNames = askopenfilenames(filetypes=[('Text file','*.txt')]) 
        # print(fileNames)
        
    def runProgram(self):
        ''' code to run the logic of lineEndings '''
        analysis = FemEnd()
        analysis.readTextFromFile('test.txt') # TODO change this to read from list
        analysis.countLines()
        analysis.countOpenLines()
        analysis.countFemEnds()
        # repr(analysis)

    def saveProgram(self):
        ''' excel?? '''
        #TODO
        # saveName = asksaveasfilename() 


if __name__ == "__main__":
    root = tk.Tk()
    FemEndGUI(root).pack(side="top", fill="both", expand=True)
    root.mainloop()