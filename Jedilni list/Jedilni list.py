# -*- coding: UTF-8 -*-

''' Jedilni list
    Author: Damir Tešnjak'''

with open("Jedilni_list.txt", "w+") as file:
    file.write("\n\n--------------------")
    file.write("\n----Jedilni list----")
    file.write("\n--------------------\n")

print("----Jedilni list----"
      "\n\nZa prekinitev vpišite 'exit'"
      "\n--------------------")

while True:

    jed = raw_input("\nVnesite jed: ")

    if jed.lower() == "exit":
        break
    else:
        cena = raw_input("Vnesite ceno: ")

        if cena == "exit":
            break
        else:
            with open("Jedilni_list.txt", "a") as file:
                file.write(jed + "---- " + cena + " EUR\n")

            with open("Jedilni_list.txt", "r") as file:
                print(file.read())