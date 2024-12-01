import oldalak
from jatekos import Jatekos
import random

milanius = Jatekos("Milánius", 1, 1, 0, 0)
barlangi = Jatekos("Barlangi Ember", 7, 7, 0, 0)

def elso_lepes():
    ugyesseg_teremtmeny:int = (random.randint(1,6)) + (random.randint(1,6))
    barlangi.ugyesseg += ugyesseg_teremtmeny
    masodik_lepes()

def masodik_lepes():
    milanius_ugyesseg:int = (random.randint(1,6)) + (random.randint(1,6))
    milanius.ugyesseg += milanius_ugyesseg
    harmadik_lepes()

def harmadik_lepes():
    if milanius.ugyesseg > barlangi.ugyesseg:
        negyedik_lepes()
    elif milanius.ugyesseg < barlangi.ugyesseg:
        otodik_lepes()
    elif milanius.ugyesseg == barlangi.ugyesseg:
        print(f"{milanius.nev} és {barlangi.nev} nem tudta legyőzni egymást!")
        elso_lepes()

def negyedik_lepes():
    print(f"{milanius.nev} ereje nagyobb mint a teremtményé, így ő támad!")
    valasz:str = input("Szeretnél szerencsepontot használni? Igen/Nem ➝ ")
    szerencseproba:int = (random.randint(1,6)) + (random.randint(1,6))
    if valasz == "Igen":
        if milanius.szerencse > szerencseproba:
            barlangi.eletero -= 4
            milanius.szerencse -= 1
            print(f"{milanius.nev}-nak szerencséje volt🍀, egy kritikus csapást hajtott végre, 4 sebzéssel megnyomorítva: {barlangi.nev}💔")
        elif milanius.szerencse < szerencseproba:
            barlangi.eletero += 1
            milanius.szerencse -= 1
            print(f"{milanius.nev}-nak nem volt szerencséje🍀, {barlangi.nev} 1 életerőre tett szert💕")
    elif valasz == "Nem":
        barlangi.eletero - 2
        print(f"{milanius.nev} nem használt szerencsét!🍀, {barlangi.nev} 2 életerőt vesztett a csapástól!💔")

def otodik_lepes():
    print(f"{barlangi.nev} ereje nagyobb mint a Milániusé, így ő támad!")
    valasz:str = input("Szeretnél szerencsepontot használni? Igen/Nem ➝ ")
    szerencseproba:int = (random.randint(1,6)) + (random.randint(1,6))
    if valasz == "Igen":
        if milanius.szerencse > szerencseproba:
            milanius.eletero -= 1
            milanius.szerencse -= 1
            print(f"{milanius.nev}-nak szerencséje volt🍀, egy kritikus csapást került ki de a teremtmény még ígyis sebet ejtett rajta, 1 életerőt vesztett!💔")
        elif milanius.szerencse < szerencseproba:
            milanius.eletero -= 3
            milanius.szerencse -= 1
            print(f"{milanius.nev}-nak nem volt szerencséje🍀, egy kritikus csapást kapott, 3 életerőt vesztett!💔")
    elif valasz == "Nem":
        milanius.eletero -= 2
        print(f"{milanius.nev} nem használt szerencsét🍀, a teremtmény eltalálta, 2 életerőt vesztett!💔")
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
    while (milanius.eletero >= 1 or barlangi.eletero >= 1):
        valasztas = input("A dobozt kinyitod (lapozz 270-re) vagy továbbmész (lapozz 66-ra)? ➝ ")
        if valasztas == "270":
            oldalak.Oldal270()
            milanius.arany += 3
            print("Begyűjtöd az aranyat!\n")
            oldalak.Oldal66()
            valasztas = input("Nyugat (lapozz 293-ra) vagy Kelet (lapozz 56-ra)? ➝ ")
            if valasztas == "293":
                oldalak.Oldal293()
                valasztas = input("Ha továbbmész nyugat felé a lábnyomokat követve, lapozz a 137-re. Ha inkább észak felé mész a harmadik pár lábnyom után, lapozz a 387-re. ➝ ")
                if valasztas == "137":
                    oldalak.Oldal137()
                    oldalak.oldal999()
                    valasz = input("Levi / NemLevi / 1 ?")
                    if valasz == "Levi":
                        milanius.arany += 999
                        print(f"{milanius.nev} jelenlegi aranya: {milanius.arany}💰")
                        oldalak.Oldal1()
                    elif valasz == "NemLevi":
                        print(f"Rossz válasz! {milanius.nev} karóba lett húzva!")
                        break
                    elif valasz == "1":
                        oldalak.Oldal1()  
                elif valasztas == "387":
                    oldalak.Oldal387()
                    print("Elkezdesz harcolni a barlangi emberrel...")
                    elso_lepes()
                    if (barlangi.eletero <= 0):
                        print(f"{barlangi.nev} meghalt, {milanius.nev} legyőzte a Labirintust!")
                        break
                    elif (milanius.eletero <= 0):
                        print(f"{milanius.nev} újabb áldozata lett a Halállabirintusnak!")
                        break
            elif valasztas == "56":
                oldalak.Oldal56()
                valasztas = input("Átmászol (lapozz 373-ra) vagy kettévágod (lapozz 215-re)? ➝ ")
                if valasztas == "373":
                    oldalak.Oldal373()
                elif valasztas == "215":
                    oldalak.Oldal215()
                    milanius.eletero - 2
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
                    if (barlangi.eletero <= 0):
                        print(f"{barlangi.nev} meghalt, {milanius.nev} legyőzte a Labirintust!")
                        break
                    elif (milanius.eletero <= 0):
                        print(f"{milanius.nev} újabb áldozata lett a Halállabirintusnak!")
                        break
            elif valasztas == "56":
                oldalak.Oldal56()
                valasztas = input("Átmászol (lapozz 373-ra) vagy kettévágod (lapozz 215-re)? ➝ ")
                if valasztas == "373":
                    oldalak.Oldal373()
                elif valasztas == "215":
                    oldalak.Oldal215()
                    milanius.eletero - 2

        print(f"A jelenlegi állapotok: \n")
        print(f"{milanius.nev} támaóereje: {milanius.ugyesseg} \n  életereje: {milanius.eletero}❤️ \n {milanius.nev} szerencséje: {milanius.szerencse}🍀 \n {milanius.nev} aranya: {milanius.arany}💰 \n")
        print(f"A {barlangi.nev} támaóereje: {barlangi.ugyesseg} \n  életereje: {barlangi.eletero}❤️")