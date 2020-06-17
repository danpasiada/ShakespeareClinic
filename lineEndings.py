# filename: lineEndings.py
# Author: Dan Pasiada, with inspiration from Ieva Burk and the Shakespeare Clinic
# purpose: counts English feminine words 
# not yet tested

import string #for string.punctuation

# TODO:
# 1) count lines in the text
# 2) count open lines -- i.e. no punctuation at the end 
# 3) count FEM endings -- i.e. words that end an iambic pentameter (I-5) line on an unstressed syllable, taDA, taDA, taDA, taDA, taDAda. (i.e. an 11th syllable) 


# Strategy for FEM endings counting:  
# ask if text contains specified feminine endings (FEMEND) or feminine words (FEMWRD) which are not listed among masculine-ending (MASCEND) or masculine-word exceptions, report % of feminine words.  See TC1 notes. 
# Examples:
# Look in thy glass and tell the face thou viewest, [f]
# Now is the time that face should form another, [f]
# Whose fresh repair if now thou not renewest, [f]
# Thou dost beguile the world, unbless some mother. [f]
# For where is she so fair whose uneared womb [m][open]
# Disdains the tillage of thy husbandry? [m]

# Ieva's strategy for FEM endings counting:
# if an ending word or ending is on 
# either 
# the feminine ending list 
# or the feminine-ending word list
# and 
# not on either the masculine-ending 
# nor the masculine word list, 
# it counts as feminine. 

class FemEnd(object):
    def __init__(self):
        '''create empty FemEnd '''
        self.text = ''
        self.lines = [] 
        self.numLines = 0
        self.numOpenLines = 0
        self.numFemEnds = 0
        

    def __repr__(self):
        '''
        display contents of FemEnd by running:
        NAME = FemEnd()
        NAME.someCommand
        print(NAME)
        '''
        s = 'Lines: ' + str(self.lines) + '\n\n'
        s += 'Number of Lines: ' + str(self.numLines) + '\n\n'
        s += 'Number of Open Lines: ' + str(self.numOpenLines)
        #s += str(self.property2)
        return s

    def excelOutput(self):
        ''' output results in .xlsx spreadsheet format '''
        # TODO: optional, until we figure out common interface for all programs

    def readTextFromFile(self, filename):
        ''' read a text file '''
        f = open(filename) #, encoding = 'utf-8') 
        self.text = f.read()
        f.close()
        

    def countLines(self):
        ''' count the number of lines in a text '''
        self.lines = self.text.splitlines() # list of lines from text
        self.numLines = len(self.lines) # number of lines in text

    def countOpenLines(self):
        ''' count lines without punctuation at the end'''
        for line in self.lines:
            #if the last character in a line is not a punctuation mark
            if line[-1] not in string.punctuation: 
                self.numOpenLines += 1

    def countFemEnds(self):
         ''' count FEM endings (strategy in the header) '''
        
        
    def countLongLines(self):
        ''' count lines with 11 syllables,
            also known as hendecasyllables
        '''
        # TODO optional, because this will be slower than countFemEnds
#aaa



    #'main' function instead of printing the below??    
A = FemEnd()
A.readTextFromFile('test.txt')
A.countLines()
A.countOpenLines()
print(A)