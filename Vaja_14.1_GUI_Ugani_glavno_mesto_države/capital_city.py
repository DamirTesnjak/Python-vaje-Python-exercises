#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''Guess Capital City
    Avtor: Damir Tešnjak'''

from Tkinter import *
import random

window = Tk()
window.title('Guess capital city | by Damir Tešnjak')
window.geometry('500x320')
window.resizable(0, 0)

infoText = Label(window, text="Guess the capital city of a country. You'll have 30 turns. Good luck!\n"
                              "WARNING! You must always select one answer before clicking button 'Next', to prevent\n"
                              "unstable behaviour of a program.", justify=LEFT)
infoText.pack(anchor=NW, padx=10, pady=10)

var = StringVar()
points = 0
step = 0

def get_answer():
    global points
    global step
    answer = var.get()
    answerIndex = {"A": 0, "B": 1, "C": 2}

    if answerIndex[answer.upper()] == ordDictKeys.index(country):
        global total_label
        points += 1
        total_label = Label(pointsFrame, text=str(points))
        total_label.pack()

        global total_step_label
        step += 1
        total_step_label = Label(stepFrame, text=str(step))
        total_step_label.pack()

        global result_label
        result_label = Label(window, text="Correct")
        result_label.place(x=225, y=250)
    else:
        result_label = Label(window, text="Incorrect! It is " + dictLines[ordDictKeys[randomIndex]] + "!")
        result_label.place(x=225, y=250)

        step += 1
        total_step_label = Label(stepFrame, text=str(step))
        total_step_label.pack()

        total_label = Label(pointsFrame, text=str(points))
        total_label.pack()


def question_frame():

    global dictLines
    dictLines = {}          # Prazen dictionary keys=COUNTRIES, value=CAPITAL CITY

    for y in range(3):
        with open("national_capital_cities.txt", 'r') as file:
            lines =file.readlines()                     # Branje vseh vrstic v datoteki
            selectedLine = random.choice(lines)         #Izbira naključne vrstice
            lineAsList = selectedLine.split(",")        #String pretvorimo v 'list', deliminator ','

        dictLines[lineAsList[1][0:]] = lineAsList[2]    #Vnos keys=COUNTRIES, value=CAPITAL CITY v dictionary

    global ordDictKeys
    ordDictKeys = dictLines.keys()          #Dobiti ključe

    global randomIndex
    randomIndex = random.randint(0,2)       #Naključen indeks

    global country
    country = ordDictKeys[randomIndex]      #Dobimo izbrano državo za katero iščemo glavno mesto

    #Izpis vpračanja

    global questionFrame
    questionFrame = LabelFrame(window)
    questionFrame.configure(relief=GROOVE, foreground="black", text="What is the capital city of " + country + "?",
                            width=450, height=75)
    questionFrame.place(x=20, y=120)

    global pointsFrame
    pointsFrame = LabelFrame(window)
    pointsFrame.configure(relief=GROOVE, foreground="black", text="Points", width=50, height=1)
    pointsFrame.place(x=60, y=70)

    global stepFrame
    stepFrame = LabelFrame(window)
    stepFrame.configure(relief=GROOVE, foreground="black", text="Turn", width=50, height=1)
    stepFrame.place(x=20, y=70)

    global A
    A = Radiobutton(questionFrame, text=dictLines[ordDictKeys[0]], padx=10, value="A", variable=var, command=get_answer)
    A.pack(anchor=W)

    global B
    B = Radiobutton(questionFrame, text=dictLines[ordDictKeys[1]], padx=10, value="B", variable=var, command=get_answer)
    B.pack(anchor=W)

    global C
    C = Radiobutton(questionFrame, text=dictLines[ordDictKeys[2]], padx=10, value="C", variable=var, command=get_answer)
    C.pack(anchor=W)

def deselect_radioButtons():
    A.deselect()
    B.deselect()
    C.deselect()

def steps(step):
    if step <= 31:
        step += 1
        next = Button(window, text="Next", command=lambda: [next.destroy(), questionFrame.destroy(),
                                                    result_label.destroy(), question_frame(), deselect_radioButtons(),
                                                    steps(step)])
        next.place(x=225, y=220)
    else:
        pointsFrame.destroy()
        questionFrame.destroy()
        result_label.destroy()
        result()

def kill_program():
    window.destroy()


def result():
    if points == 30:
        result_label = Label(window, text="EXPERT!")
        result_label.pack(anchor=CENTER, pady= 30)
        exit = Button(window, text="Exit", command=lambda: [kill_program()])
        exit.place(x=225, y=220)

    elif points > 20 and points <= 29:
        result_label = Label(window, text="Excellent!")
        result_label.pack(anchor=CENTER, pady= 50)
        exit = Button(window, text="Exit", command=lambda: [kill_program()])
        exit.place(x=225, y=220)

    elif points > 15 and points <= 20:
        result_label = Label(window, text="Good!")
        result_label.pack(anchor=CENTER, pady= 50)
        exit = Button(window, text="Exit", command=lambda: [kill_program()])
        exit.place(x=225, y=220)

    elif points > 10 and points <= 15:
        result_label = Label(window, text="It could be better!")
        result_label.pack(anchor=CENTER, pady= 50)
        exit = Button(window, text="Exit", command=lambda: [kill_program()])
        exit.place(x=225, y=220)

    else:
        result_label = Label(window, text="GO BACK TO SCHOOL!!!")
        result_label.pack(anchor=CENTER, pady= 50)
        exit = Button(window, text="Exit", command=lambda: [kill_program()])
        exit.place(x=225, y=220)

question_frame()
steps(step)

window.mainloop()