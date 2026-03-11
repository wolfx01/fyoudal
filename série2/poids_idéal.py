print("1-homme")
print("2-femme")
t  = float(input("donner t = "))
if t<140 :
    print("taille incorrect")
else:
    n = int(input("donner la nature n ="))
    if n==1:
        pi = (t - 100) * 0.9
        print("la poids idéal est  :", pi, "kg")
    else:
        if n==2 :
            pi = (t - 100) * 0.85
            print("la poids idéal est  :", pi, "kg")
        else:
            print("homme or femme !!!!")
