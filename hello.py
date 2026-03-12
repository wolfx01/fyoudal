


class animal :
    def __init__(self , c , n , a  ):
        self.code = c
        self.nom = n
        self.age = a
    def  affich(self):
        print(self.code, self.nom.upper(), self.age  , end="" )

class chat(animal ) :
    def __init__(self , c , n , a , r , cl ):
        animal.__init__(self , c , n , a  )
        self.race = r
        self.couleur = cl
    def affich(self):
        animal.affich(self)
        print(self.race , self.couleur , end=" ")


lc = []
while True:
    print("***** menu *****")
    print("1-ajouter")
    print("2-afficher")
    print("3-rechercher")
    print("4-supprimer")
    print("5-serialiser")
    print("6-quitter")


    choix = int(input(" donner  le   choix : "))
    if choix == 1:
        c= int(input(" donner  le   code : "))
        n = str(input(" donner  le   nom : "))
        while True:
            a = int(input(" donner  le   age : "))
            if a >= 4  and 10 >= a:
                break
            else:
                print("donner  l'age entre 4 et 10")
        r = int(input(" donner  le   race : "))
        cl = int(input(" donner  le   couleur : "))

        chat = chat(c , n , a , r , cl)
        lc.append(chat)
    if choix == 2:
        for i in lc:
            i.affich()

    if choix == 3:
        cs = int(input(" donner  le   code : "))
        for i in lc:
            if i.code == cs:
                i.affich()
                break
            else :
                print("le code  indisponible")
                break
    if choix






