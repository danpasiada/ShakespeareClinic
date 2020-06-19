# LineEndings
## An adaptation of a Claremont McKenna Shakespeare Clinic program that counts feminine-ending-word lines in a play
How this works:
1) count lines in the text
2) count open lines -- i.e. no punctuation at the end 
3) count FEM endings -- i.e. words that end an iambic pentameter (I-5) line on an unstressed syllable, taDA, taDA, taDA, taDA, taDAda. (i.e. an 11th syllable) 


Strategy for FEM endings counting:  
ask if text contains specified feminine endings (FEMEND) or feminine words (FEMWRD) which are not listed among masculine-ending (MASCEND) or masculine-word exceptions, report % of feminine words.  See TC1 notes. 
Examples:
Look in thy glass and tell the face thou viewest, [f]
Now is the time that face should form another, [f]
Whose fresh repair if now thou not renewest, [f]
Thou dost beguile the world, unbless some mother. [f]
For where is she so fair whose uneared womb [m][open]
Disdains the tillage of thy husbandry? [m] # the program thinks husbandry is feminine, because of the -ry ending

Ieva's strategy for FEM endings counting:
if an ending word or ending is on 
either 
the feminine ending list 
or the feminine-ending word list
and 
not on either the masculine-ending 
nor the masculine word list, 
it counts as feminine. 

TODO: get screenshots
