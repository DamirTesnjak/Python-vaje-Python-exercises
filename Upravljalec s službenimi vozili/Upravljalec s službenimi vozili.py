#!/usr/bin/env python
# -*- coding: UTF-8 -*-

''' UPRAVLJALEC VOZNEGA PARKA
    Author: Damir Tešnjak
	Python 3.x'''

print ("\n----Upravljalec voznega parka----\n")


# POMOČ UPORABNIKU

def help():
    print ("Ukaz  Opis" \
          "\n\nS:    Seznam vozil" \
          "\nKM:   Ševilo prevoženih kilometrov" \
          "\nSER:  Datum zadnjega servisa" \
          "\nV:    Novo vozilo" \
          "\nO:    Odstrani vozilo iz seznama" \
          "\nI:    Izhod iz posamezne opcije" \
          "\nEND:  Izhod iz programa" \
          "\nP:    Pomoč")


# S CLASSOM USTVARJENO VOZILO

class object_Vehicle( object ):

    """"Novo vozilo iz vnešenih podatkov. Znamka, model, število prevoženih kilometrov, datum
        zadnjega servisa"""

    def __init__( self, brand, model, km, service ):
        self.brand = brand
        self.model = model
        self.km = km
        self.service = service


# VPIS VOZILA V DATOTEKO/BAZO

def new_vehicle( brand, model, km, service, id_num ):
    
    vehicle = object_Vehicle( brand, model, km, service )

    data_to_write = id_num + " Znamka: " + vehicle.brand + " Model: " + vehicle.model + " Prevoženi kilometri: " + \
                    vehicle.km + " km Datum servisa: " + vehicle.service
    writing_into_file( data_to_write )


# BRANJE DATOTEKE, OGLED SEZNAMA

def vehicle_list():
    print ("\n----SEZNAM VOZIL----\n")
    with open( "data_vozila.txt", "r+" ) as file:
        lines = file.readlines()
        lines.sort()
        if len( lines ) == 0:
            print ("Seznam vozil je prazen!")
        else:
            for line in lines:
                print (line)
    print ("\n--------------------\n")


# PISANJE V DATOTEKO

def writing_into_file( new_line ):
    with open( "data_vozila.txt", "a" ) as file:
        file.write( new_line + "\n" )


# ISKANJE VOZILA

def find_vehicle( id_num ):
    with open( "data_vozila.txt", "r" ) as file:
        lines = file.readlines()
        for line in lines:
            if id_num in line:
                return line


# BRISANJE IZ DATOTEKE

def delete_vehicle( id_num ):  # Koda iz Stockoverflow
    try:
        with open( "data_vozila.txt", "r+" ) as f:
            t = f.read()
            to_delete = find_vehicle( id_num ).strip()  # kaj izbrišemo
            f.seek( 0 )
            for line in t.split( '\n' )[ :-1]:
                if line != to_delete:
                    f.write( line + '\n' )
            f.truncate()
    except AttributeError:
        print ("Vozilo v bazi podatkov ne obstaja!\nPoskusite znova!")


# SKUPNI DEFINICIJI

def shared_def():
    vehicle_list()
    id_num = input( "Vnesite ID številko vozila: " )
    selected_Vehicle = find_vehicle( id_num ).split()
    delete_vehicle( id_num )
    return selected_Vehicle


def shared_def2( selected_Vehicle ):
    new_line = ' '.join( selected_Vehicle )
    writing_into_file( new_line )
    vehicle_list()


# UREJANJE ŠT. KILOMETROV

def change_km():
    selected_Vehicle = shared_def()
    kilometers = input( "Vnesite novo število kilometrov: " )
    selected_Vehicle.insert( 7, kilometers )
    del selected_Vehicle[ 8 ]
    shared_def2( selected_Vehicle )


# UREJANJE DATUMA ZADNJEGA SERVISA

def change_date_service():
    selected_Vehicle = shared_def()
    service = input( "Vnesite nov datum zadnjega servisa ( dd-mm-yyyy ): " )
    selected_Vehicle.insert( 11, service )
    del selected_Vehicle[ 12 ]
    shared_def2( selected_Vehicle )


# VNOS PODATKOV VOZILA

def input_vehicle():
    while True:
        brand = input( "\nZnamka vozila: " )

        if brand.upper() == "I":
            break
        else:
            model = input( "Model vozila: " )
            if model.upper() == "I":
                break
            else:
                km = input( "Število prevoženih kilometrov (brez 'km'): " )
                if km.upper() == "I":
                    break
                else:
                    service = input( "Datum zadnjega servisa ( dd-mm-yyyy ): " )
                    if service.upper() == "I":
                        break
                    else:
                        id_num = input( "Vnesite ID številko ( primer: 001, 002, 003... ). " )
                        if id_num.upper() == "I":
                            break
                        else:
                            try:
                                if find_vehicle( id_num ).split( " " )[ 0]   == id_num:
                                    print ("Vozilo z ID " + id_num + " že obstaja. Poskusite znova.")
                                    input_vehicle()
                            except AttributeError:
                                new_vehicle( brand, model, km, service, id_num )
                                vehicle_list()


# IZBIRA UPORABNIKA

def command():
    while True:
        option = input( "\nIzberite opcijo: " )
        if option.upper() == "S":
            vehicle_list()
        elif option.upper() == "KM":
            change_km()
        elif option.upper() == "SER":
            change_date_service()
        elif option.upper() == "V":
            vehicle_list()
            input_vehicle()
            vehicle_list()
        elif option.upper() == "O":
            vehicle_list()
            id_num = input( "Vnesite ID številko ( primer: 001, 002, 003... ). " )
            delete_vehicle( id_num )
            print ("Vozilo je izbrisano")
            vehicle_list()
        elif option.upper() == "P":
            help()
        elif option.upper() == "END":
            print ("Konec programa")
            break

help()
command()
