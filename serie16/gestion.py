from datetime import date
class profeeseur:
    def __init__(self, c ,  n , p ,  da ):
        self.code = c
        self.nom = n
        self.prenom = p
        self.date = da


    def affich(self):
        print(self.code , self.nom, self.prenom, self.date , sep="\t" , end="\t")
    def calculage(self):
        d = date.today().year - self.date
        return d

class profeeseurf(profeeseur):
    def __init__(self, c ,  n , p ,  da , e , g , s  ):
        profeeseur.__init__(self, c , n , p , da)
        self.echell = e
        self.grade = g
        self.salaire = s
    def affich(self):
        profeeseur.affich(self)
        print(self.echell , self.grade, self.salaire , sep="\t" , end="\t")
    def prince(self):
        if self.echell >= 19:
            self.salaire +=  2000


def mot ():
    print("* gestion client  * ")
    mdp = "bilal"
    b = 0
    while b < 3:
        mdps = input("donner le mot de passe  : ")  
        if mdps == mdp:
            return True
        else:
            print("le mot de passe n'est pas ")
            b += 1
    return False







if mot():
    lc  = []
    c= 0

    while True:
        print("\n**** Menu ****")
        print("1 - Ajout")
        print("2 - Affichage")
        print("3 - Recherche")
        print("4 - Suppression")
        print("5 - Modification")
        print("6 - Quitter")

        choix = input("Donner votre choix : ")

        if choix == "1":
            c += 100
            print("le code  de client  est  : " , c)
            while True  :
                n = input("Donner le nom : ")
                if not n :
                    print("Le nom n'existe pas")
                    continue
                break
            while True :
                p = input("Donner le prenom : ")
                if not p :
                    print("Le prenom n'existe pas")
                    continue
                break
            while True :
                d = input("Donner le date : ")
                if not d  or not d.isdigit()  or int(d) <= 19:
                    print("Le date n'existe pas et date>19")
                    continue
                break

            while True :
                sal= input("donner  le salaire : ")
                if not sal or not sal.isdigit() or int(sal) <= 8000  or int(sal) >= 27000   :
                    print("Le salaire n'existe pas")
                    continue
                break
            while True :
                ech = input("donner  le echell : ")
                if not ech or not ech.isdigit() or int(ech) <= 13  or int(ech) >= 25   :
                    print("Le echell n'existe pas")
                    continue
                break
            while True :
                gra = input("donner  le gra : ")
                if not ech or not ech.isdigit()   :
                    print("Le echell n'existe pas")
                    continue
                break















            cl = profeeseurf(c, n, p,d ,   ech  , gra , sal )
            lc.append(cl)
            print("Ajout effectué")

        elif choix == "2":
            for i in range(len(lc)):
                lc[i].affich()

        elif choix == "3":
            coder = int(input("Donner le code du client : "))
            existe = False
            for j in lc:
                if j.code == coder:
                    j.affich()
                    existe = True
            if not existe:
                print("Client introuvable")

        elif choix == "4":
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

        elif choix == "5":
            codem = int(input("Donner le code du client à modifier : "))
            pos = -1
            for i in range(len(lc)):
                if lc[i].code == codem:
                    pos = i
            if pos != -1:
                c = int(input("Donner nouveau code : "))
                n = input("Donner nouveau nom : ")
                p = input("Donner nouveau prenom : ")
                v = input("Donner nouvelle date : ")
                sal = input("Donner nouvelle  salaire : ")
                ech = input("Donner nouvelle echell : ")
                gra = input("Donner nouvelle grade : ")
                lc[pos] = profeeseurf(c, n,p , v  , ech , gra ,  sal )
                print("Modification effectuée")
            else:
                print("Client introuvable")

        elif choix == "6":
             p = input("quite !!  1-oui \t 2-non : ")
             if p == "1":
                 break
             elif p == "2":
                 continue



        else:
            print("Choix incorrect")


        f = open("clint.txt","w")
        for x in lc:
            f.write(str(x.code) + "|")
            f.write(x.nom + "|")
            f.write(x.prenom + "|")
            f.write(x.date + "|")
            f.write(x.salaire + "|")
            f.write(x.echell + "|")
            f.write(x.grade + "|")


else:
    print("error")


