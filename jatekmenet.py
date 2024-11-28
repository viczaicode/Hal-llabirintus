import oldalak

def alagut_kaland():
    valasztas = input("A dobozt kinyitod (lapozz 270-re) vagy továbbmész (lapozz 66-ra)? ➝")
    if valasztas == "270":
        oldalak.Oldal270()
        print("Begyűjtöd az aranyat!\n")
        oldalak.Oldal66()
        valasztas = input("Nyugat (lapozz 293-ra) vagy Kelet (lapozz 56-ra)? ➝")
        if (valasztas == "56"):
            oldalak.Oldal56()
            valasztas = input("Átmászol (lapozz 373-ra) vagy kettévágod (lapozz 215-re)? ➝")
        elif (valasztas == "293"):
            oldalak.Oldal293()
    elif valasztas == "66":
        oldalak.Oldal66()
        valasztas = input("Nyugat (lapozz 293-ra) vagy Kelet (lapozz 56-ra)? ➝")
        if valasztas == "293":
            oldalak.Oldal293()
            valasztas = input("Ha továbbmész nyugat felé a lábnyomokat követve, lapozz a 137-re. Ha inkább észak felé mész a harmadik pár lábnyom után, lapozz a 387-re. ➝")
            if valasztas == "137":
                oldalak.Oldal137()  
            elif valasztas == "387":
                oldalak.Oldal387()
        elif valasztas == "56":
            oldalak.Oldal56()
            valasztas = input("Átmászol (lapozz 373-ra) vagy kettévágod (lapozz 215-re)? ➝")
            if valasztas == "373":
                oldalak.Oldal373()
            elif valasztas == "215":
                oldalak.Oldal215()