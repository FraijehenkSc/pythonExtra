import os
from time import sleep


def rename():
    bestandsnaam = input("Hallo, welk bestand wil je hernoemen?")


    huidige_map = os.getcwd()

    volledige_pad = os.path.join(huidige_map, bestandsnaam)
    print("Dit bestand gaan we hernoemen: " + volledige_pad)

    nieuwe_naam = input("Nieuwe bestandsnaam: ")    

    while True:
        if len(nieuwe_naam) >0:
        
            nieuwe_volledige_pad = os.path.join(huidige_map, nieuwe_naam)
        
            print("Bestand wordt hernoemd naar: " + nieuwe_volledige_pad)
            os.rename(volledige_pad, nieuwe_volledige_pad)
            print("Bestand hernoemd")
            break
        else:
            print("De nieuwe naam moet langer dan 1 letter zijn.")

rename()

choice = input("Wil je nog een bestand hernoemen?\n (y) or (n)")
if choice.lower == "y":
    rename()
else:
    print("Oke dan, tot ziens.")
    sleep(5)
    quit()



