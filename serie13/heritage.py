from datetime import date


class  personner :
    def __init__(self ):
        self.code = 0
        self.nom = ""
        self.prenom = ""
    def __init__(self,c , n ,  p ):
        self.code = c
        self.nom = n
        self.prenom = p
    def affich(self):
        print(self.code, self.nom.upper(), self.prenom.capitalize(), sep="\t" , end="\t")


class etudiant(personner):
    def __init__(self , c , n , p  , a , f):
        personner.__init__(self , c , n , p )
        self.age = a
        self.fillier = f
    def affich(self ):
        personner.affich(self)
        print(self.age, self.fillier , sep="\t" , end="\t")
    def nessense(self):
        if self.age < 18:
            return "meneur"
        else:
            return "majeur"
    def date(self):
        k = date.today().year - self.age
        return k



p = personner(0 , "" , "")
p1 = personner(10 , "bilal" , "chouichou")
e1 = etudiant(20 , "hamza" , "picala" , 19 , "DD101")
e2 = etudiant(30 , "bilal" , "sourie" , 20 , "DD101")


p.affich()
print("\n")
e1.affich()
print("\n")
e2.affich()
print("\n")
p1.affich()
print("\n")
e1.affich()
print("\n")
e2.affich()
print("\n")
print(e1.nessense())
print("\n")
print(e2.nessense())


print("\n")

print(e1.date())
print("\n")
print(e2.date())
