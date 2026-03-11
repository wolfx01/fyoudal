t  = float(input("donner t = "))
n = str(input("donner la nature n ="))
if t<140 :
    print("taille incorrect")
elif n=="homme":

    pi = (t - 100) * 0.9
    print("la poids idéal est  :", pi, "kg")

elif n=="femme" :
    pi = (t - 100) * 0.85
    print("la poids idéal est  :", pi, "kg")

else:
    print("homme or femme !!!!")

