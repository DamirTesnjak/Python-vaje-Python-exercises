# -*- coding: UTF-8 -*-

''' Jedilni list
    Avthor: Damir Tešnjak'''

with open("Jedilni_list.txt", "w+") as file:
    file.write("\n\n--------------------")
    file.write("\n----Jedilni list----")
    file.write("\n--------------------\n")

print("----Jedilni list----"
      "\n\nZa prekinitev vpišite 'exit'"
      "\n--------------------")

meni = {}

while True:

    jed = raw_input("\nVnesite jed: ")

    if jed.lower() == "exit":
        break
    else:
        cena = raw_input("Vnesite ceno: ")

        if cena == "exit":
            break
        else:
            meni[jed] = cena

with open("Jedilni_list.txt", "a") as file:
    for jed in meni:
        file.write(jed + "---- " + meni[jed] + " EUR\n")

with open("Jedilni_list.txt", "r") as file:
    print(file.read())