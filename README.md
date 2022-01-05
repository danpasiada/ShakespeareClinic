This is an modernised (Python!) adaptation of suite of text analysis software used in the Claremont McKenna Shakespeare Clinic

## lineEndings.py
- counts feminine-ending-word lines in a play

How this works:
1) count lines in the text
2) count open lines -- i.e. no punctuation at the end 
3) count FEM endings -- i.e. words that end an iambic pentameter (I-5) line on an unstressed syllable, taDA, taDA, taDA, taDA, taDAda. (i.e. an 11th syllable) 

## posCounter2
- counts unweighted differences in parts of speech between two texts

## whileCount
- counts amount of time 'while' is used specifically as a noun

## Flesch-Kincaid
- returns a Flesch-Kincaid grade-level score of a text

## posCounter2
- highlights each given string in a given file


### Strategy for FEM endings counting:  
ask if text contains specified feminine endings (FEMEND) or feminine words (FEMWRD) which are not listed among masculine-ending (MASCEND) or masculine-word exceptions, report % of feminine words.  See TC1 notes. 
Examples:
- Look in thy glass and tell the face thou viewest, [f]
- Now is the time that face should form another, [f]
- Whose fresh repair if now thou not renewest, [f]
- Thou dost beguile the world, unbless some mother. [f]
- For where is she so fair whose uneared womb [m][open]
- Disdains the tillage of thy husbandry? [m] # the program thinks husbandry is feminine, because of the -ry ending
