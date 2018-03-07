#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''FizzBuzz
    Avtor: Damir Tešnjak'''

while True:

    inputNum = raw_input("\nVnesite število med 1 in 100."
                         "\nZa izhod vtipkaj 'exit' brez navednic! ")

    if inputNum.lower() == "exit":
        print("\n-----------------------\nProgram je zaustavljen!")
        break

    elif inputNum.isalpha() == True:
        print("Vnos ni številka. Poskusite znova.")
    else:
        inputNum = int(inputNum)

        if inputNum < 1 or inputNum > 100:
            print("Vnesli ste število izven intervala! Poskusite znova")
        else:
            for i in range(1, inputNum + 1):
                if i % 3 == 0 and not i % 5 == 0:
                    print("fizz")
                elif i % 5 == 0 and not i % 3 == 0:
                    print("buzz")
                elif i % 3 == 0 and i % 5 == 0:
                    print("fizzbuzz")
                else:
                    print(i)

