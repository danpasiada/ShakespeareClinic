This is an modernised (Python!) adaptation of suite of text analysis software used in the Claremont McKenna College Shakespeare Clinic. The programs in this repo have been tested against the data in [Oxford by the Numbers](https://www1.cmc.edu/pages/faculty/welliott/UTConference/Oxford_by_Numbers.pdf). 

See [history of the Clinic](https://www1.cmc.edu/pages/faculty/welliott/shakes.htm) and [Ward Elliott's selected writings](https://www1.cmc.edu/pages/faculty/welliott/select.htm) for additional information on the Clinic and its research. 

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
