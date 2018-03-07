# -*- coding: UTF-8 -*-

''' CSI DNA Analysis
    Author: Damir Tešnjak'''

hairColor = {
    "Blonde": "TTAGCTATCGC",
    "Black": "CCAGCAATCGC",
    "Brown": "GCCAGTGCCG"
}

facialShape = {
    "Square": "GCCACGG",
    "Round": "ACCACAA",
    "Oval": "AGGCCTCA"
}

eyeColor = {
    "Blue": "TTGTGGTGGC",
    "Green": "GGGAGGTGGC",
    "Brown": "AAGTAGTGAC"
}

gender = {
    "Female": "TGAAGGACCTTC",
    "Male": "TGCAGGAACTTC"
}

race = {
    "White": "AAAACCTCA",
    "Black": "CGACTACAG",
    "Asian": "CGCGGGCCG"
}

def sortDict(dict, data):
    dict_to_list = dict.keys()               # shrani ključe (keys) kot novi seznam.
    dict_to_list.sort()                      # razvrsti elemente v seznamu po abecedi
    return dict[dict_to_list[int(data)]]     # pridobi vrednost ključa iz dict na podlagi indeksa elementa v seznamu

print("\n----CSI DNA Analysis----\n\nExit program any time typing EXIT")

#--------------------------------------------------------------------------
#                VNOS PODATKOV
#--------------------------------------------------------------------------

print("\nStep #1: Input suspect.\n")

while True:

    dataName = raw_input("Suspect name: ")
    if dataName.lower() == "exit":
        break
    else:
        dataGender = raw_input("Gender (Female: 0, Male: 1): ")
        if dataGender.lower() == "exit":
            break
        else:
            genderDNA = sortDict(gender, dataGender)

            dataRace = raw_input("Race (Asian: 0, Black: 1, White: 2): ")
            if dataRace.lower() == "exit":
                break
            else:
                raceDNA = sortDict(race, dataRace)

                dataHair = raw_input("Hair color (Blonde: 0, Black: 1, Brown: 2): ")
                if dataHair.lower() == "exit":
                    break
                else:
                    hairDNA = sortDict(hairColor, dataHair)

                    dataEye = raw_input("Eye color (Blue: 0, Brown: 1, Green: 2): ")
                    if dataEye.lower() == "exit":
                        break
                    else:
                        eyeDNA = sortDict(eyeColor, dataEye)

                        dataFace = raw_input("Facial shape (Oval: 0, Round: 1, Square: 2): ")
                        if dataFace.lower() == "exit":
                            break
                        else:
                            faceDNA = sortDict(facialShape, dataFace)


# --------------------------------------------------------------------------
#                DNK ANALIZA
# --------------------------------------------------------------------------

    print "\nStep #2: DNA Analysis.\n"
    openData = raw_input("Open DNA file, type its name. File must be in *.txt format (example: filename.txt). ")

    with open("" + openData, "r") as file:
        line = file.readline()
    print("\nAnalysis of DNA " + line[0:50] + "...")

    match = 0
    for i in (genderDNA, hairDNA, eyeDNA, faceDNA):
        if i in line:
            match += 1


# --------------------------------------------------------------------------
#                REZULTAT
# --------------------------------------------------------------------------

    negative_result = "Suspect DNA does NOT match DNA sample!"
    positive_result = "!!!Suspect DNA does MATCH DNA sample!!!\n" + str(float((4 / match) * 100)) + "% match!\n"

    if match == 4:
        print "\nCase: " + dataName + " " + positive_result
    else:
        print negative_result