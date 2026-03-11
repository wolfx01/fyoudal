



class  fichier :
    def __init__(self ,  c  ,  t ,  mh) :
        self.code = c
        self.title = t
        self.mh = mh

    def afficher(self) :
        if(self.mh>  100) :
            print(self.code,self.title,self.mh)
        else:
            print(self.code,self.title,self.mh)
    def  toString(self):
        print(self.code,self.title,self.mh)





class personne( fichier) :
    def __init__(self , c , t , mh , n ,  p ) :
        fichier.__init__(self , c , t , mh)
        self.n = n
        self.p = p
    def afficher(self) :
        print(self.code,self.title,self.mh)
        fichier.afficher(self)




c = []
while True  :
    print("**********  menu ************")
    print("1-ajouter")
    print("2-afficher")
    print("3-modifier")
    print("4-supprimer")
    print("5-trier")
    print("6-quiter")
    choix = int(input("choix : "))
    if choix == 1 :
        c= input("donner code")