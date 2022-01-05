This is an modernised (Python!) adaptation of suite of text analysis software used in the Claremont McKenna Shakespeare Clinic.

## posCounter2.py
- counts unweighted differences in parts of speech between two texts

## whileCount.py
- counts amount of time 'while' is used specifically as a noun

## lineEndings.py
- counts feminine-ending-word lines in a play
FEM endings are words that end an iambic pentameter (I-5) line on an unstressed syllable, taDA, taDA, taDA, taDA, taDAda. (i.e. an 11th syllable)
Examples:
- Look in thy glass and tell the face thou viewest, [f]
- Now is the time that face should form another, [f]
- Whose fresh repair if now thou not renewest, [f]
- Thou dost beguile the world, unbless some mother. [f]
- For where is she so fair whose uneared womb [m][open]
- Disdains the tillage of thy husbandry? [m] # the program currently thinks husbandry is feminine, because of the -ry ending

## Flesch-Kincaid.py (written by Sam Ness)
- returns a Flesch-Kincaid grade-level score of a text

## kwFinderWidget.py (written by Sam Ness)
- highlights each given string in a given file
