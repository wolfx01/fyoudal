a=float(input("donner a:"))
b=float(input("donner b:"))
c=float(input("donner c:"))


d=(b**2)-4*a*c
racine=d**0.5

if a == 0 and b == 0 and c == 0:
    print("imposible")
elif a == 0 and b !=0 and c != 0 :
    x = -c/b
    print("la solution=", x)
elif a == 0 and c ==0 :
    x = 1/b
    print("la solution=", x)
elif d<=0:
    print("nest pas solution")
elif d==0:
    x=(-b)/(2*a)
    print("la solution=",x)
else:
    x1 = (-b - racine) / (2 * a)
    x2 = (-b + racine) / (2 * a)
    print("les  eqution admins doux  adsolution est=""x1=",round(x2,2),"et","x2=",round(x1,2))