x = int(input("donner la valeur x :"))
y = int(input("donner la valeur y : "))
z = int(input("donner la valeur z :"))
if x > y and x > z:
    sup = x
    print("la plus grand" , sup)
elif y > x and y > z:
    sup = y
    print("la plus grand" , sup)
elif z > x and z > y:
    sup = z
    print("la plus grand" , sup)
elif x == y and x == z:
    print("les 3 entier sont égalt")
elif x==y  and x > z :
    sup = x
    print("la plus grand" , sup)
elif x==y and z > x:
    sup = z
    print("la plus grand" , sup)
elif y==z and y > x :
    sup = y
    print("la plus grand" , sup)
else:
    sup = x
    print("la plus grand" , sup)

