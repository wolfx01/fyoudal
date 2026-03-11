import math
class figure:
    def __init__(self):
        self.c = 0
        self.n = ""
    def __init__(self , c , n):
        self.code = c
        self.nature = n
    def affich(self ):
        print(self.code,self.nature , sep="\t" , end="\t")


class point(figure):
    def __init__(self ,  a , o , c , n ):
        figure.__init__(self , c , n  )
        self.absaices = a
        self.ordonnee = o
    def affich(self):

        print(self.absaices , self.ordonnee , sep="\t" , end="\t")
    def calculd(self):
        d =  math.sqrt(self.ordonnee**2 + self.absaices**2)
        return d
class cercle(figure):
    def __init__(self , c , n , s , r ):
        figure.__init__(self , c , n)
        self.centre = s
        self.rayon = r
    def affich(self):
        figure.affich(self)
        print(self.centre , self.rayon , sep="\t" , end="\t")
    def calculs(self):
        s = self.rayon * self.rayon*3.14
        return s


p1 = point(  2 , 1  , "" , "")
p2 = point( -1 , 3 , "" , "")
print("\n")
p1.affich()
print("\n")

p2.affich()
print("\n")
print(p1.calculd())
print("\n")

print(p2.calculd())
print("\n")


c1 = cercle("","" , 3 , 4  , )
c2 = cercle("","" , 3 , -1 , )
c1.affich()
print("\n")

c2.affich()
print("\n")

print(c1.calculs())
print("\n")

print(c2.calculs())
print("\n")

class  point3d(point):
    def __init__(self ,  a , o , c , n  , x):
        point.__init__(self  , a , o, n , c)
        self.x = x
    def affich(self):
        point.affich(self)
        print(self.x , sep="\t" , end="\t")
    def calculd1(self):
        d1 = math.sqrt(self.calculd() **2 +self.x**2)
        return d1


p31= point3d( 1 , 1 , ""  , "" , 3 , )
p32= point3d( 1 , 2 , ""  , "" , 4 , )
p31.affich()
print("\n")

p32.affich()
print("\n")

print(p31.calculd1())
print("\n")

print(p32.calculd1())



class rectongle(figure) :

    def __init__(self , c , n  , l , la):
        figure.__init__(self , c , n )
        self.long = l
        self.labort  = la

