email = lambda nom , prenom: nom + "." + prenom + "@gmail.com"

class client :
    def __init__(self ,c , n , p , e) :
        self.code = c
        self.nom = n
        self.prenom = p
        self.email = email(self.nom, self.prenom)

    def get_code(self) :
        return self.code
    def get_nom(self) :
        return self.nom
    def get_prenom(self) :
        return self.prenom
    def get_email(self) :
        return self.email
    def set_code(self ,value) :
            self.code = value
    def set_nom(self ,value) :
            self.nom = value
    def set_prenom(self ,value) :
            self.prenom = value
    def set_email(self ,value) :
            self.email = value
    def affich(self):
        print(self.code , self.nom.upper() , self.prenom.capitalize() , self.email)





c1= client(10 , "amid" , "salah ", "" )
c2= client(10 , "chouichou" , "bilal ", "" )
c1.affich()
c2.affich()


c1.affich()
c2.affich()


print(c1.get_code(), c1.get_nom())

print( c1.get_prenom(), c1.get_email())
c1.set_code(100)
c2.set_nom("dahbi")
c1.affich()
c2.affich()
