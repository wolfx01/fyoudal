import datetime

class voiture:
    def __init__(self):
        self.code = 0
        self.marque = ""
        self.module = 0
        self.puissance = 0
        self.couleur = ""
        self.press = 0

    def __init__(self, code, marque, module, puissance, couleur,press):
        self.code = code
        self.marque = marque
        self.module = module
        self.puissance = puissance
        self.couleur = couleur
        self.press = press
    def affiche(self):
        print(self.code, self.marque.upper(), self.module, self.puissance, self.couleur , self.press)
    def ancliennet(self):
        age = datetime.date.today().year - self.module
        return age
    def puissanse(self):
        if self.puissance >= 8:
            print("puissente")
        else:
            print(" non puissente")


    def prix(self):
        if self.couleur == "blanc":
            self.press =self.press -2000
        else:
            self.press =self.press +2000
    def age(self):
        if self.ancliennet() > 10:
            print("onsian")
        else:
            print("nouveu")

v = voiture(0 , "",0 ,0 ,""  ,0)
v1=voiture(100, "Fiat" , 2025 , 6  ,"grise" , 20000)
v2=voiture(200, "Mercedes" , 1998 ,10   ,"blanc" , 30000)

v.prix()
v1.prix()
v2.prix()
v1.affiche()
v2.affiche()
v1.puissanse()
v2.puissanse()
v.age()
v1.age()
v2.age()
print(v1.ancliennet())
print(v2.ancliennet())
print(v1.__class__)
print(v2.__class__)
print(v1.__module__)
print(v2.__module__)
print(v1.__dict__)
print(v2.__dict__)
print(v1.__doc__)
print(v2.__doc__)



