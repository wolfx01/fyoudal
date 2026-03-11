class Client:
    def __init__(self, c, n, p, v):
        self.code = c
        self.nom = n
        self.prenom = p
        self.ville = v

    def afficher(self):
        print(
            self.nom.upper(),
            self.prenom.capitalize(),
            self.code,
            self.ville,
            sep=" | "
        )


lc = []

while True:
    print("\n**** Menu ****")
    print("1 - Ajout")
    print("2 - Affichage")
    print("3 - Recherche")
    print("4 - Suppression")
    print("5 - Modification")
    print("6 - Quitter")

    choix = int(input("Donner votre choix : "))

    if choix == 1:
        c = int(input("Donner le code : "))
        n = input("Donner le nom : ")
        p = input("Donner le prenom : ")
        v = input("Donner la ville : ")
        cl = Client(c, n, p, v)
        lc.append(cl)
        print("Ajout effectué")

    elif choix == 2:
        for i in range(len(lc)):
            lc[i].afficher()

    elif choix == 3:
        coder = int(input("Donner le code du client : "))
        existe = False
        for j in lc:
            if j.code == coder:
                j.afficher()
                existe = True
        if not existe:
            print("Client introuvable")

    elif choix == 4:
        cods = int(input("Donner le code du client à supprimer : "))
        pos = -1
        for i in range(len(lc)):
            if lc[i].code == cods:
                pos = i
        if pos != -1:
            confirm = int(input("Voulez-vous vraiment supprimer ? 1-Oui 2-Non : "))
            if confirm == 1:
                lc.pop(pos)
                print("Suppression effectuée")
            else:
                print("Suppression annulée")
        else:
            print("Client introuvable")

    elif choix == 5:
        codem = int(input("Donner le code du client à modifier : "))
        pos = -1
        for i in range(len(lc)):
            if lc[i].code == codem:
                pos = i
        if pos != -1:
            c = int(input("Donner nouveau code : "))
            n = input("Donner nouveau nom : ")
            p = input("Donner nouveau prenom : ")
            v = input("Donner nouvelle ville : ")
            lc[pos] = Client(c, n, p, v)
            print("Modification effectuée")
        else:
            print("Client introuvable")

    elif choix == 6:
         p = input("quite !!  1-oui \t 2-non : ")
         if p == "1":
             break
         elif p == "2":
             continue



    else:
        print("Choix incorrect")