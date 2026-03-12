lc = []
class animal :
    def __init__(self , c , n , a):
        self.code = c
        self.nom = n
        self.age = a
    def affich(self):
        print(self.code ,  self.nom , self.age , sep = "\t" , end = "\t")

class chat(animal):
    def __init__(self ,c , n, a , r , co):
        animal.__init__(self, c , n , a)
        self.race = r
        self.couleur = co
    def affich(self):
        animal.affich(self)
        print(self.race , self.couleur , sep = "\t" , end = "\n")

while True :
    print("*** MENU D'UTILISATION ***")
    print("1- Ajoute ")
    print("2- afficher ")
    print("3- rechercher ")
    print("4- supprimer ")
    print("5- serialiser ")
    print("6- quitter ")
    choix = int(input ("donner votre choix :"))

    if choix == 1 :

        while True:
            code = input("donner le code :")
            if not code or not code.isdigit():
                print("code incorrect ")
                continue
            break
        while True :
            nom = str(input("donner le nom :"))
            if not nom:
                print("nom incorrect")
                continue
            break
        while True:
            age = input("donner l'age :")
            if not age or not age.isdigit() or int(age) < 4 or int(age) > 10:
                print("l'age est incorrect , l'age doit etre entre 4 et 10 ans")
                continue
            break
        while True :
            race = input("donner le race :")
            if not race:
                print("race incorrect")
                continue
            break
        while True :
            couleur = input ("donner la couleur :")
            if not couleur :
                print("couleur incorrect")
                continue
            break

        chats = chat(int(code) , nom.upper() , int(age) , race , couleur )
        lc.append(chats)

    elif choix == 2 :
        if not lc :
            print ("list vide")
        for c in lc :
            c.affich()

    elif choix == 3 :
        codes = int(input ("donner le code pour recherche : "))
        for c in lc :
            if c.code == codes :
                c.affich()
                break
        else:
            print ("code introuvable")

    elif choix == 4 :
        coder = int(input("donner le code duchat pour supprimer :"))
        for i in range (len(lc)):
            if lc[i].code == coder :
                verification = int(input("vous allez vraiment supprimer se chat ? \n 1- OUI ou 2-NON \n donner votre choix :"))
                if verification == 1 :
                    lc.pop(i)
                    print("Suppression effectuée")
                    break
                else:
                    break

    elif choix == 5 :
        f = open("chat.txt" , "w")
        for c in lc :
            f.write(str(c.code))
            f.write("|")
            f.write(c.nom)
            f.write("|")
            f.write(str(c.age))
            f.write("|")
            f.write(c.race)
            f.write("|")
            f.write(c.couleur)
            print("\n")
        f.close()

    elif choix == 6 :
        print("aurevoir")
        break
    else :
        print ("votre choix et incorrect ")
        continue