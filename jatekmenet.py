import oldalak
from jatekos import Jatekos
import random

milanius = Jatekos("Milánius", 1, 1, 0, 0)
barlangi = Jatekos("Barlangi Ember", 7, 7, 0, 0)

def elso_lepes():
    ugyesseg_teremtmeny:int = (random.randint(1,6)) + (random.randint(1,6))
    barlangi.ugyesseg += ugyesseg_teremtmeny

def masodik_lepes():
    milanius_ugyesseg:int = (random.randint(1,6)) + (random.randint(1,6))
    milanius.ugyesseg += milanius_ugyesseg

def harmadik_lepes():
    if milanius.ugyesseg > barlangi.ugyesseg:
        negyedik_lepes()
    elif milanius.ugyesseg < barlangi.ugyesseg:
        otodik_lepes()
    elif milanius.ugyesseg == barlangi.ugyesseg:
        print(f"{milanius.nev} és {barlangi.nev} nem tudta legyőzni egymást!")
        elso_lepes()
        masodik_lepes()
        harmadik_lepes()

def negyedik_lepes():
    valasz:str = input("Szeretnél szerencsepontot használni? Igen/Nem ➝ ")
    szerencseproba:int = (random.randint(1,6)) + (random.randint(1,6))
    if valasz == "Igen":
        if milanius.szerencse > szerencseproba:
            barlangi.eletero - 4
            milanius.szerencse - 1
        elif milanius.szerencse < szerencseproba:
            barlangi.eletero += 1
            milanius.szerencse - 1
    elif valasz == "Nem":
        barlangi.eletero - 2

def otodik_lepes():
    valasz:str = input("Szeretnél szerencsepontot használni? Igen/Nem ➝ ")
    szerencseproba:int = (random.randint(1,6)) + (random.randint(1,6))
    if valasz == "Igen":
        if milanius.szerencse > szerencseproba:
            milanius.eletero - 1
            milanius.szerencse - 1
        elif milanius.szerencse < szerencseproba:
            milanius.eletero - 3
            milanius.szerencse - 1
    elif valasz == "Nem":
        milanius.eletero - 2
def hatodik_lepes():
    if milanius.eletero <= 0:
        print(f"{milanius.nev} meghalt a labirintusban. The End!")
    if barlangi.eletero <= 0:
        print(f"{milanius.nev} legyőzte a halállabirintust. The End!")

def hetedik_lepes():
    while (milanius.eletero >= 1 and barlangi.eletero >= 1):
        elso_lepes()
        masodik_lepes()
        harmadik_lepes()
    print(f"{milanius.nev}életereje: {milanius.eletero} \n {barlangi.nev} életereje {barlangi.eletero}!")


def labirintus():
    valasztas = input("A dobozt kinyitod (lapozz 270-re) vagy továbbmész (lapozz 66-ra)? ➝ ")
    if valasztas == "270":
        oldalak.Oldal270()
        milanius.arany += 3
        print("Begyűjtöd az aranyat!\n")
        oldalak.Oldal66()
        valasztas = input("Nyugat (lapozz 293-ra) vagy Kelet (lapozz 56-ra)? ➝ ")
        if (valasztas == "56"):
            oldalak.Oldal56()
            valasztas = input("Átmászol (lapozz 373-ra) vagy kettévágod (lapozz 215-re)? ➝ ")
        elif (valasztas == "293"):
            oldalak.Oldal293()
            valasztas = input("Nyugat (lapozz 387-re) vagy Észak (lapozz 137-ra)? ➝ ")
        if (valasztas == "137"):
            oldalak.Oldal137()
        elif (valasztas == "387"):
            oldalak.Oldal387()
            print("Elkezdesz harcolni a barlangi emberrel...")
            elso_lepes()
            masodik_lepes()
            harmadik_lepes()
            hatodik_lepes()
            hetedik_lepes()
    elif valasztas == "66":
        oldalak.Oldal66()
        valasztas = input("Nyugat (lapozz 293-ra) vagy Kelet (lapozz 56-ra)? ➝ ")
        if valasztas == "293":
            oldalak.Oldal293()
            valasztas = input("Ha továbbmész nyugat felé a lábnyomokat követve, lapozz a 137-re. Ha inkább észak felé mész a harmadik pár lábnyom után, lapozz a 387-re. ➝ ")
            if valasztas == "137":
                oldalak.Oldal137()  
            elif valasztas == "387":
                oldalak.Oldal387()
                print("Elkezdesz harcolni a barlangi emberrel...")
                elso_lepes()
                masodik_lepes()
                harmadik_lepes()
                hatodik_lepes()
                hetedik_lepes()
        elif valasztas == "56":
            oldalak.Oldal56()
            valasztas = input("Átmászol (lapozz 373-ra) vagy kettévágod (lapozz 215-re)? ➝ ")
            if valasztas == "373":
                oldalak.Oldal373()
            elif valasztas == "215":
                oldalak.Oldal215()
                milanius.eletero - 2