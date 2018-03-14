#!/usr/bin/env python
# -*- coding: UTF-8 -*-

''' Ugani število
    Author: Damir Tešnjak'''

print "\n----Upravljalec voznega parka----\n"


# POMOČ UPORABNIKU

def help():
    print "______________________________________________"\
          "\n| Ukaz  | Opis                               |" \
          "\n----------------------------------------------" \
          "\n| S:    | Seznam vozil                       |" \
          "\n| KM:   | Ševilo prevoženih kilometrov       |" \
          "\n| SER:  | Datum zadnjega servisa             |" \
          "\n| V:    | Novo vozilo                        |" \
          "\n| O:    | Odstrani vozilo iz seznama         |" \
          "\n| I:    | Kadarkoli izhod iz posamezne opcije|" \
          "\n| END:  | Izhod iz programa                  |" \
          "\n| P:    | Pomoč                              |" \
          "\n----------------------------------------------"
    print "Če želite predčasno končati program, najprej" \
          "\nzapustite opcijo (I), šele nato končajte" \
          "\nprogram (END). Nepravilna uporaba ukazov in" \
          "\nnapačnih vnosov lahko 'podre' program in" \
          "\nPOVZROČI IZGUBO PODATKOV!"

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

    data_to_write = id_num + "," + \
                    vehicle.brand + "," + \
                    vehicle.model + "," + \
                    vehicle.km + "," + \
                    vehicle.service + ","
    writing_into_file( data_to_write )


# BRANJE DATOTEKE, OGLED SEZNAMA

def vehicle_list():

    print "\n----SEZNAM VOZIL----\n"
    print "_________________________________________________________________"
    print "| ID  | ZNAMKA     | MODEL      | KM         | DATUM SERVISA    |"
    print "-----------------------------------------------------------------"

    with open( "data_vozila.txt", "r+" ) as file:
        lines = file.readlines()
        lines.sort()

        if len( lines ) == 0:
            print "Seznam vozil je prazen!\n"
            return False
        else:
            for line in lines:
                try:
                    lineAsList = line.split(",")
                    print "| " + lineAsList[0] + " | " + lineAsList[1] + " " * (10 - len(lineAsList[1])) + \
                          " | " + lineAsList[2] + " " * (10 - len(lineAsList[2])) + \
                          " | " + lineAsList[3] + " " * (10 - len(lineAsList[3])) + \
                          " | " + lineAsList[4] + " " * (17 - len(lineAsList[4])) + "|"
                except IndexError:
                    continue
    print "-----------------------------------------------------------------\n"


# PISANJE V DATOTEKO

def writing_into_file( new_line ):

    with open( "data_vozila.txt", "a" ) as file:
        file.write( new_line + "\n")


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

            for line in t.split( "\n" ):
                if line != to_delete:
                    f.write( line + "\n" )
            f.truncate()

    except AttributeError:

        print "Vozilo v bazi podatkov ne obstaja!" \
              "\nPoskusite znova!"


def remove_empty_lines(): # Koda iz Stockoverflow
    """Overwrite the file, removing empty lines and lines that contain only whitespace."""
    with open("data_vozila.txt", 'r+') as f:
        lines = f.readlines()
        f.seek(0)
        f.writelines(line for line in lines if line.strip())
        f.truncate()


# SKUPNI DEFINICIJI PRI UREJANJU PODATKOV

def shared_def():

    if vehicle_list() == False:
        command()
    else:
        id_num = raw_input( "Vnesite ID številko vozila: " )

        if id_num.upper() == "I":
            return False
        else:
            selected_Vehicle = find_vehicle( id_num ).split(",")
            delete_vehicle( id_num )
            return selected_Vehicle


def shared_def2( selected_Vehicle ):

    new_line = ','.join( selected_Vehicle )
    writing_into_file( new_line )


# UREJANJE ŠT. KILOMETROV

def change_km():

    selected_Vehicle = shared_def()
    if selected_Vehicle == False:
        return False
    else:
        kilometers = raw_input( "Vnesite novo število kilometrov: " )

        if kilometers.upper() == "I":
            return False
        else:
            selected_Vehicle.insert( 3, kilometers )
            del selected_Vehicle[ 4 ]
            shared_def2( selected_Vehicle )


# UREJANJE DATUMA ZADNJEGA SERVISA

def change_date_service():

    selected_Vehicle = shared_def()

    if selected_Vehicle == False:
        return False
    else:
        service = raw_input( "Vnesite nov datum zadnjega servisa ( dd-mm-yyyy ): " )

        if service.upper() == "I":
            return False
        else:
            selected_Vehicle.insert( 4, service )
            del selected_Vehicle[ 5 ]
            shared_def2( selected_Vehicle )


# VNOS PODATKOV VOZILA

def input_vehicle():
    while True:
        brand = raw_input( "\nZnamka vozila: " )

        if brand.upper() == "I":
            break
        else:
            model = raw_input( "Model vozila: " )
            if model.upper() == "I":
                break
            else:
                km = raw_input( "Število prevoženih kilometrov: " )
                if km.upper() == "I":
                    break
                else:
                    service = raw_input( "Datum zadnjega servisa ( dd-mm-yyyy ): " )
                    if service.upper() == "I":
                        break
                    else:
                        id_num = raw_input( "Vnesite ID številko ( primer: 001, 002, 003... ). " )
                        if id_num.upper() == "I":
                            break
                        else:
                            try:
                                if find_vehicle( id_num ).split( " " )[ 0]   == id_num:
                                    print "Vozilo z ID " + id_num + " že obstaja. Poskusite znova."
                                    input_vehicle()
                            except AttributeError:
                                new_vehicle( brand, model, km, service, id_num )


# IZBIRA UPORABNIKA

def command():
    while True:

        option = raw_input( "\nIzberite opcijo. " )

        if option.upper() == "S":
            vehicle_list()

        elif option.upper() == "KM":
            if change_km() == False:
                continue
            else:
                change_km()
                remove_empty_lines()

        elif option.upper() == "SER":
            if change_date_service() == False:
                continue
            else:
                change_date_service()
                remove_empty_lines()
                vehicle_list()

        elif option.upper() == "V":
            vehicle_list()
            input_vehicle()
            vehicle_list()

        elif option.upper() == "O":
            vehicle_list()
            id_num = raw_input( "Vnesite ID številko ( primer: 001, 002, 003... ). " )

            if id_num.upper() == "I":
                continue
            else:
                warning = raw_input("Potrdtitev izbrisa (D/N). ")
                if warning.upper() == "D":
                    delete_vehicle(id_num)
                    remove_empty_lines()
                    vehicle_list()
                else:
                    continue

        elif option.upper() == "P":
            help()

        elif option.upper() == "END":
            print "----------------" \
                  "\nKonec programa."
            break

help()
command()