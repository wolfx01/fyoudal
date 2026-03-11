import datetime
class stagaire:
    def __init__(self,code , nom, prenom, age,  filier):
        self.code = code
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.filier = filier
    def afficher(self):
        print(self.code, self.nom.upper(), self.prenom.capitalize(), self.age, self.filier, end=" ")
    def calculage(self):
        a= datetime.date.today().year - self.age
        return a
    def dicessien(self):
        if self.calculage() >= 2007 :
            return "majeur"
        else:
            return "mineur"


s1 = stagaire(10,"alami" , "taha" ,19 ,"DD101")
s2 = stagaire(20, "dahbi", "aya", 18, "DD102")
s1.afficher()
print(" ")
s2.afficher()
print("lage de stagier s1 est :" , s1.calculage())
print(" ")
print("lage de stagier s2 est :", s2.calculage())
print(" ")
print("lage de stagier s1 est :" , s1.dicessien())
print(" ")
print("lage de stagir s2 est :", s2.dicessien())




