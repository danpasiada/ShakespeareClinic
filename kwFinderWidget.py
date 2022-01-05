#filename: kwFinderWidget.py
#author: Sam Ness
#purpose: highlits each given string in a given file
#tested to work in ipython

import tkinter
from tkinter import *
from nltk.tokenize import word_tokenize
from nltk import pos_tag
import re
import fileinput


window = tkinter.Tk()
window.title("KW-Finder")

tkinter.Label(window, text = "Hi! Welcome to Keyword Finder!").grid(row=0)
tkinter.Label(window, text = "First, please type in the name for the file you'd like to analyze").grid(row=1)
tkinter.Label(window, text = "Second, list up to 5 strings that you'd like to find annd to be returned in context!").grid(row=2)

tkinter.Label(window, text='File Name').grid(row=3)
tkinter.Label(window, text='String 1').grid(row=4)
tkinter.Label(window, text='String 2').grid(row=5)
tkinter.Label(window, text='String 3').grid(row=6)
tkinter.Label(window, text='String 4').grid(row=7)
tkinter.Label(window, text='String 5').grid(row=8)

fileName = Entry(window)
string1 = Entry(window, foreground = 'red', insertbackground = 'red', background = 'black')
string2 = Entry(window, foreground = 'white', insertbackground = 'white', background = 'black')
string3 = Entry(window, foreground = 'magenta', insertbackground = 'magenta', background = 'black')
string4 = Entry(window, foreground = 'yellow', insertbackground = 'yellow', background = 'black')
string5 = Entry(window, foreground = 'orange', insertbackground = 'orange', background = 'black')
fileName.grid(row=3, column=1)
string1.grid(row=4, column=1)
string2.grid(row=5, column=1)
string3.grid(row=6, column=1)
string4.grid(row=7, column=1)
string5.grid(row=8, column=1)

def fileRead():
    window2 = tkinter.Tk()
    window2.title("Results!")
    scrollbar = Scrollbar(window2)

    textbox = Text(window2, yscrollcommand=scrollbar.set, height = 20, width = 100, background = 'black', foreground = 'rosy brown')

    textbox.grid(column=0)


    scrollbar.config(command=textbox.yview)

    s1Count = 0
    s2Count = 0
    s3Count = 0
    s4Count = 0
    s5Count = 0

    filepath = fileName.get()

    with open(filepath) as fp:
        for cnt, line in enumerate(fp):

            if (string1.get() != '' and string1.get() in line) or (string2.get() != '' and string2.get() in line) or (string3.get() != '' and string3.get() in line) or (string4.get() != '' and string4.get() in line) or (string5.get() != '' and string5.get() in line):

                textbox.insert(INSERT, "{}: {}".format(cnt, line))


            if string1.get() in line:
                s1Count += 1
            if string2.get() in line:
                s2Count += 1
            if string3.get() in line:
                s3Count += 1
            if string4.get() in line:
                s4Count += 1
            if string5.get() in line:
                s5Count += 1

        def find(  ):

            # get string to look for (if empty, no searching)
            s = string1.get()
            s2 = string2.get()
            s3 = string3.get()
            s4 = string4.get()
            s5 = string5.get()
            if s:
                # start from the beginning (and when we come to the end, stop)
                idx = '1.0'


                while 1:
                    # find next occurrence, exit loop if no more
                    idx = textbox.search(s, idx, nocase=1, stopindex=END)
                    if not idx: break
                    # index right after the end of the occurrence

                    lastidx = '%s+%dc' % (idx, len(s))


                    # tag the whole occurrence (start included, stop excluded)
                    textbox.tag_add('found', idx, lastidx)
                    # prepare to search for next occurrence
                    idx = lastidx
                    # use a red foreground for all the tagged occurrences
                textbox.tag_config('found', foreground='red')

            if s2:
                # start from the beginning (and when we come to the end, stop)
                idx2 = '1.0'


                while 1:
                    # find next occurrence, exit loop if no more
                    idx2 = textbox.search(s2, idx2, nocase=1, stopindex=END)
                    if not idx2: break
                    # index right after the end of the occurrence

                    lastidx2 = '%s+%dc' % (idx2, len(s2))


                    # tag the whole occurrence (start included, stop excluded)
                    textbox.tag_add('s2', idx2, lastidx2)
                    # prepare to search for next occurrence
                    idx2 = lastidx2
                    # use a red foreground for all the tagged occurrences
                textbox.tag_config('s2', foreground='white')

            if s3:
                # start from the beginning (and when we come to the end, stop)
                idx3 = '1.0'


                while 1:
                    # find next occurrence, exit loop if no more
                    idx3 = textbox.search(s3, idx3, nocase=1, stopindex=END)
                    if not idx3: break
                    # index right after the end of the occurrence

                    lastidx3 = '%s+%dc' % (idx3, len(s3))


                    # tag the whole occurrence (start included, stop excluded)
                    textbox.tag_add('s3', idx3, lastidx3)
                    # prepare to search for next occurrence
                    idx3 = lastidx3
                    # use a red foreground for all the tagged occurrences
                textbox.tag_config('s3', foreground='magenta')

            if s4:
                # start from the beginning (and when we come to the end, stop)
                idx4 = '1.0'


                while 1:
                    # find next occurrence, exit loop if no more
                    idx4 = textbox.search(s4, idx4, nocase=1, stopindex=END)
                    if not idx4: break
                    # index right after the end of the occurrence

                    lastidx4 = '%s+%dc' % (idx4, len(s4))


                    # tag the whole occurrence (start included, stop excluded)
                    textbox.tag_add('s4', idx4, lastidx4)
                    # prepare to search for next occurrence
                    idx4 = lastidx4
                    # use a red foreground for all the tagged occurrences
                textbox.tag_config('s4', foreground='yellow')

            if s5:
                # start from the beginning (and when we come to the end, stop)
                idx5 = '1.0'


                while 1:
                    # find next occurrence, exit loop if no more
                    idx5 = textbox.search(s5, idx5, nocase=1, stopindex=END)
                    if not idx5: break
                    # index right after the end of the occurrence

                    lastidx5 = '%s+%dc' % (idx5, len(s5))


                    # tag the whole occurrence (start included, stop excluded)
                    textbox.tag_add('s5', idx5, lastidx5)
                    # prepare to search for next occurrence
                    idx5 = lastidx5
                    # use a red foreground for all the tagged occurrences
                textbox.tag_config('s5', foreground='orange')

        def find1():
            s = string1.get()
            if s:
                # start from the beginning (and when we come to the end, stop)
                idx = '1.0'


                while 1:
                    # find next occurrence, exit loop if no more
                    idx = textbox.search(s, idx, nocase=1, stopindex=END)
                    if not idx: break
                    # index right after the end of the occurrence

                    lastidx = '%s+%dc' % (idx, len(s))


                    # tag the whole occurrence (start included, stop excluded)
                    textbox.tag_add('found', idx, lastidx)
                    # prepare to search for next occurrence
                    idx = lastidx
                    # use a red foreground for all the tagged occurrences
                textbox.tag_config('found', foreground='red')

        def find2():
            s2 = string2.get()
            if s2:
                # start from the beginning (and when we come to the end, stop)
                idx2 = '1.0'


                while 1:
                    # find next occurrence, exit loop if no more
                    idx2 = textbox.search(s2, idx2, nocase=1, stopindex=END)
                    if not idx2: break
                    # index right after the end of the occurrence

                    lastidx2 = '%s+%dc' % (idx2, len(s2))


                    # tag the whole occurrence (start included, stop excluded)
                    textbox.tag_add('s2', idx2, lastidx2)
                    # prepare to search for next occurrence
                    idx2 = lastidx2
                    # use a red foreground for all the tagged occurrences
                textbox.tag_config('s2', foreground='white')

        def find3():
            s3 = string3.get()
            if s3:
                # start from the beginning (and when we come to the end, stop)
                idx3 = '1.0'


                while 1:
                    # find next occurrence, exit loop if no more
                    idx3 = textbox.search(s3, idx3, nocase=1, stopindex=END)
                    if not idx3: break
                    # index right after the end of the occurrence

                    lastidx3 = '%s+%dc' % (idx3, len(s3))


                    # tag the whole occurrence (start included, stop excluded)
                    textbox.tag_add('s3', idx3, lastidx3)
                    # prepare to search for next occurrence
                    idx3 = lastidx3
                    # use a red foreground for all the tagged occurrences
                textbox.tag_config('s3', foreground='magenta')

        def find4():
            s4 = string4.get()
            if s4:
                # start from the beginning (and when we come to the end, stop)
                idx4 = '1.0'


                while 1:
                    # find next occurrence, exit loop if no more
                    idx4 = textbox.search(s4, idx4, nocase=1, stopindex=END)
                    if not idx4: break
                    # index right after the end of the occurrence

                    lastidx4 = '%s+%dc' % (idx4, len(s4))


                    # tag the whole occurrence (start included, stop excluded)
                    textbox.tag_add('s4', idx4, lastidx4)
                    # prepare to search for next occurrence
                    idx4 = lastidx4
                    # use a red foreground for all the tagged occurrences
                textbox.tag_config('s4', foreground='yellow')

        def find5():
            s5 = string5.get()
            if s5:
                # start from the beginning (and when we come to the end, stop)
                idx5 = '1.0'


                while 1:
                    # find next occurrence, exit loop if no more
                    idx5 = textbox.search(s5, idx5, nocase=1, stopindex=END)
                    if not idx5: break
                    # index right after the end of the occurrence

                    lastidx5 = '%s+%dc' % (idx5, len(s5))


                    # tag the whole occurrence (start included, stop excluded)
                    textbox.tag_add('s5', idx5, lastidx5)
                    # prepare to search for next occurrence
                    idx5 = lastidx5
                    # use a red foreground for all the tagged occurrences
                textbox.tag_config('s5', foreground='orange')


        def undoAll(  ):

            # get string to look for (if empty, no searching)
            u1 = string1.get()
            u2 = string2.get()
            u3 = string3.get()
            u4 = string4.get()
            u5 = string5.get()
            textbox.tag_delete('found')
            textbox.tag_delete('s2')
            textbox.tag_delete('s3')
            textbox.tag_delete('s4')
            textbox.tag_delete('s5')

            if u1:
                # start from the beginning (and when we come to the end, stop)
                idr = '1.0'


                while 1:
                    # find next occurrence, exit loop if no more
                    idr = textbox.search(u1, idr, nocase=1, stopindex=END)
                    if not idr: break
                    # index right after the end of the occurrence

                    lastidr = '%s+%dc' % (idr, len(u1))


                    # tag the whole occurrence (start included, stop excluded)
                    textbox.tag_add('u1', idr, lastidr)
                    # prepare to search for next occurrence
                    idr = lastidr
                    # use a red foreground for all the tagged occurrences
                textbox.tag_config('u1', foreground='rosy brown')

            if u2:
                # start from the beginning (and when we come to the end, stop)
                idr2 = '1.0'


                while 1:
                    # find next occurrence, exit loop if no more
                    idr2 = textbox.search(u2, idr2, nocase=1, stopindex=END)
                    if not idr2: break
                    # index right after the end of the occurrence

                    lastidr2 = '%s+%dc' % (idr2, len(u2))


                    # tag the whole occurrence (start included, stop excluded)
                    textbox.tag_add('u2', idr2, lastidr2)
                    # prepare to search for next occurrence
                    idr2 = lastidr2
                    # use a red foreground for all the tagged occurrences
                textbox.tag_config('u2', foreground='rosy brown')

            if u3:
                # start from the beginning (and when we come to the end, stop)
                idr3 = '1.0'


                while 1:
                    # find next occurrence, exit loop if no more
                    idr3 = textbox.search(u3, idr3, nocase=1, stopindex=END)
                    if not idr3: break
                    # index right after the end of the occurrence

                    lastidr3 = '%s+%dc' % (idr3, len(u3))


                    # tag the whole occurrence (start included, stop excluded)
                    textbox.tag_add('u3', idr3, lastidr3)
                    # prepare to search for next occurrence
                    idr3 = lastidr3
                    # use a red foreground for all the tagged occurrences
                textbox.tag_config('u3', foreground='rosy brown')

            if u4:
                # start from the beginning (and when we come to the end, stop)
                idr4 = '1.0'


                while 1:
                    # find next occurrence, exit loop if no more
                    idr4 = textbox.search(u4, idr4, nocase=1, stopindex=END)
                    if not idr4: break
                    # index right after the end of the occurrence

                    lastidr4 = '%s+%dc' % (idr4, len(u4))


                    # tag the whole occurrence (start included, stop excluded)
                    textbox.tag_add('u4', idr4, lastidr4)
                    # prepare to search for next occurrence
                    idr4 = lastidr4
                    # use a red foreground for all the tagged occurrences
                textbox.tag_config('u4', foreground='rosy brown')

            if u5:
                # start from the beginning (and when we come to the end, stop)
                idr5 = '1.0'


                while 1:
                    # find next occurrence, exit loop if no more
                    idr5 = textbox.search(u5, idr5, nocase=1, stopindex=END)
                    if not idr5: break
                    # index right after the end of the occurrence

                    lastidr5 = '%s+%dc' % (idr5, len(u5))


                    # tag the whole occurrence (start included, stop excluded)
                    textbox.tag_add('u5', idr5, lastidr5)
                    # prepare to search for next occurrence
                    idr5 = lastidr5
                    # use a red foreground for all the tagged occurrences
                textbox.tag_config('u5', foreground='rosy brown')

        def undo1():
            u1 = string1.get()
            textbox.tag_delete('found')
            if u1:
                # start from the beginning (and when we come to the end, stop)
                idy = '1.0'


                while 1:
                    # find next occurrence, exit loop if no more
                    idy = textbox.search(u1, idy, nocase=1, stopindex=END)
                    if not idy: break
                    # index right after the end of the occurrence

                    lastidy = '%s+%dc' % (idy, len(u1))


                    # tag the whole occurrence (start included, stop excluded)
                    textbox.tag_add('u1', idy, lastidy)
                    # prepare to search for next occurrence
                    idy = lastidy
                    # use a red foreground for all the tagged occurrences
                textbox.tag_config('u1', foreground='rosy brown')

        def undo2():
            u2 = string2.get()
            textbox.tag_delete('s2')
            if u2:
                # start from the beginning (and when we come to the end, stop)
                idy2 = '1.0'


                while 1:
                    # find next occurrence, exit loop if no more
                    idy2 = textbox.search(u2, idy2, nocase=1, stopindex=END)
                    if not idy2: break
                    # index right after the end of the occurrence

                    lastidy2 = '%s+%dc' % (idy2, len(u2))


                    # tag the whole occurrence (start included, stop excluded)
                    textbox.tag_add('u2', idy2, lastidy2)
                    # prepare to search for next occurrence
                    idy2 = lastidy2
                    # use a red foreground for all the tagged occurrences
                textbox.tag_config('u2', foreground='rosy brown')

        def undo3():
            u3 = string3.get()
            textbox.tag_delete('s3')
            if u3:
                # start from the beginning (and when we come to the end, stop)
                idy3 = '1.0'


                while 1:
                    # find next occurrence, exit loop if no more
                    idy3 = textbox.search(u3, idy3, nocase=1, stopindex=END)
                    if not idy3: break
                    # index right after the end of the occurrence

                    lastidy3 = '%s+%dc' % (idy3, len(u3))


                    # tag the whole occurrence (start included, stop excluded)
                    textbox.tag_add('u3', idy3, lastidy3)
                    # prepare to search for next occurrence
                    idy3 = lastidy3
                    # use a red foreground for all the tagged occurrences
                textbox.tag_config('u3', foreground='rosy brown')

        def undo4():
            u4 = string4.get()
            textbox.tag_delete('s4')
            if u4:
                # start from the beginning (and when we come to the end, stop)
                idy4 = '1.0'


                while 1:
                    # find next occurrence, exit loop if no more
                    idy4 = textbox.search(u4, idy4, nocase=1, stopindex=END)
                    if not idy4: break
                    # index right after the end of the occurrence

                    lastidy4 = '%s+%dc' % (idy4, len(u4))


                    # tag the whole occurrence (start included, stop excluded)
                    textbox.tag_add('u4', idy4, lastidy4)
                    # prepare to search for next occurrence
                    idy4 = lastidy4
                    # use a red foreground for all the tagged occurrences
                textbox.tag_config('u4', foreground='rosy brown')

        def undo5():
            u5 = string5.get()
            textbox.tag_delete('s5')
            if u5:
                # start from the beginning (and when we come to the end, stop)
                idy5 = '1.0'


                while 1:
                    # find next occurrence, exit loop if no more
                    idy5 = textbox.search(u5, idy5, nocase=1, stopindex=END)
                    if not idy5: break
                    # index right after the end of the occurrence

                    lastidy5 = '%s+%dc' % (idy5, len(u5))


                    # tag the whole occurrence (start included, stop excluded)
                    textbox.tag_add('u5', idy5, lastidy5)
                    # prepare to search for next occurrence
                    idy5 = lastidy5
                    # use a red foreground for all the tagged occurrences
                textbox.tag_config('u5', foreground='rosy brown')



        def wordCount():
            window3 = tkinter.Tk()
            window3.title("Word Count!")

            tkinter.Label(window3, text='String 1 ({}) count: {}'.format(string1.get(), s1Count)).grid(row=0)
            tkinter.Label(window3, text='String 2 ({}) count: {}'.format(string2.get(), s2Count)).grid(row=1)
            tkinter.Label(window3, text='String 3 ({}) count: {}'.format(string3.get(), s3Count)).grid(row=2)
            tkinter.Label(window3, text='String 4 ({}) count: {}'.format(string4.get(), s4Count)).grid(row=3)
            tkinter.Label(window3, text='String 5 ({}) count: {}'.format(string4.get(), s5Count)).grid(row=4)


    tkinter.Button(window2, text = "Color All!", command = find).grid(column=0, row=1)
    tkinter.Button(window2, text = "Color {}!".format(string1.get()), command = find1, foreground = 'red', background = 'black').grid(column=0, row=2)
    tkinter.Button(window2, text = "Color {}!".format(string2.get()), command = find2, foreground = 'white', background = 'black').grid(column=0, row=3)
    tkinter.Button(window2, text = "Color {}!".format(string3.get()), command = find3, foreground = 'magenta', background = 'black').grid(column=0, row=4)
    tkinter.Button(window2, text = "Color {}!".format(string4.get()), command = find4, foreground = 'yellow', background = 'black').grid(column=0, row=5)
    tkinter.Button(window2, text = "Color {}!".format(string5.get()), command = find5, foreground = 'orange', background = 'black').grid(column=0, row=6)

    tkinter.Button(window2, text = "Undo All!", command = undoAll).grid(column=1, row=1)
    tkinter.Button(window2, text = "Undo {}!".format(string1.get()), command = undo1, foreground = 'red', background = 'black').grid(column=1, row=2)
    tkinter.Button(window2, text = "Undo {}!".format(string2.get()), command = undo2, foreground = 'white', background = 'black').grid(column=1, row=3)
    tkinter.Button(window2, text = "Undo {}!".format(string3.get()), command = undo3, foreground = 'magenta', background = 'black').grid(column=1, row=4)
    tkinter.Button(window2, text = "Undo {}!".format(string4.get()), command = undo4, foreground = 'yellow', background = 'black').grid(column=1, row=5)
    tkinter.Button(window2, text = "Undo {}!".format(string5.get()), command = undo5, foreground = 'orange', background = 'black').grid(column=1, row=6)

    tkinter.Button(window2, text = "Count", command = wordCount).grid(column=6, row=1)

    tkinter.Button(window2, text = "Replace {} with".format(string1.get()), command = replaceAll, foreground = 'red', background = 'black').grid(column=3, row=2)
    tkinter.Button(window2, text = "Replace {} with".format(string2.get()), command = undo2, foreground = 'white', background = 'black').grid(column=3, row=3)
    tkinter.Button(window2, text = "Replace {} with".format(string3.get()), command = undo3, foreground = 'magenta', background = 'black').grid(column=3, row=4)
    tkinter.Button(window2, text = "Replace {} with".format(string4.get()), command = undo4, foreground = 'yellow', background = 'black').grid(column=3, row=5)
    tkinter.Button(window2, text = "Replace {} with".format(string5.get()), command = undo5, foreground = 'orange', background = 'black').grid(column=3, row=6)

    replace1 = Entry(window2, foreground = 'red', insertbackground = 'red', background = 'black')
    replace2 = Entry(window2, foreground = 'white', insertbackground = 'white', background = 'black')
    replace3 = Entry(window2, foreground = 'magenta', insertbackground = 'magenta', background = 'black')
    replace4 = Entry(window2, foreground = 'yellow', insertbackground = 'yellow', background = 'black')
    replace5 = Entry(window2, foreground = 'orange', insertbackground = 'orange', background = 'black')
    replace1.grid(row=2, column=4)
    replace2.grid(row=3, column=4)
    replace3.grid(row=4, column=4)
    replace4.grid(row=5, column=4)
    replace5.grid(row=6, column=4)

    tkinter.Button(window2, text = "Count", command = replaceAll).grid(column=4, row=1)



    window2.mainloop()



tkinter.Button(window, text = "Find!", command = fileRead).grid(row=9)


window.mainloop()
