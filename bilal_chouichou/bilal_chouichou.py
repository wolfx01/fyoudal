import random


ls = []


lns = ["azizi", "alami", "mahdi", "fadili", "haddad", "bahdar", "achan"]
lnp = ["achraf", "aya", "ayoub", "zara", "fatima", "reda", "mohamed"]
lps = ["DD", "ID", "GESTION", "COMMERCE", "TDI", "TDM"]


mail = lambda nom, prenom: nom + "." + prenom + "@gmail.com"



def remplire(n):
    for i in range(n):
        nom = random.choice(lns)
        prenom = random.choice(lnp)
        filier = random.choice(lps)
        age = random.randint(20, 24)
        email = mail(nom, prenom)
        nmodule = random.randint(4, 6)

        lnote = [random.randint(0, 20) for _ in range(nmodule)]

        ls.append({
            "nom": nom,
            "prenom": prenom,
            "filier": filier,
            "age": age,
            "email": email,
            "note": lnote,
            "moyenne": 0
        })


def calculmoy(l):
    for i in range(len(l)):
        s = 0
        for note in l[i]["note"]:
            s += note

        l[i]["moyenne"] = round(s / len(l[i]["note"]), 2)


def trier(l):
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            if l[i]["moyenne"] > l[j]["moyenne"]:
                temp = l[i]
                l[i] = l[j]
                l[j] = temp


def serializer(l):
    f = open("stagaire.txt", "a")
    for i in l:
        line = str(i["nom"]) + " | " + str(i["prenom"]) + " | " + str(i["filier"]) + " | " + str(
            i["age"]) + " | " + str(i["moyenne"]) + "\n"
        f.write(line)
    f.close()

def afficher(l):
    for i in l:
        print(str(i["nom"]) + " | " + str(i["prenom"]) + " | " + str(i["age"]) + " | " + str(i["email"]) + " | " + str(i["filier"]) + " | " + str(
            i["moyenne"]))





n = int(input("donner le nombre du stagiers:"))

remplire(n)
calculmoy(ls)
trier(ls)
calculmoy(ls)
afficher(ls)
serializer(ls)