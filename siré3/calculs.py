print("1-somme")
print("2-produit")
print("3-différence")
print("4-division")
x = int(input("donner x: "))
y = int(input("donner y: "))
choix = int(input("donner choix: "))
if choix == 1:
    s = x + y
    print( "la somme est" ,s)
elif choix == 2:
    s = x * y
    print( "la product est" ,s)
elif choix == 3:
    s = x - y
    print( "la difference est" ,s)
elif choix == 4:
    if y == 0 :
        print("division imposible")
    else:
        s = y / x
        print( "la quotient est" ,s)
else:
    print("chois incorrect")

