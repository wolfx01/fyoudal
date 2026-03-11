from datetime import date
naisssonce = lambda j, m , a : (str(j) if j >=10 else "0" + str(j)) + "/" + (str(m) if m>=10 else "0" +str(m)) +"/"+str(a)
x= int(input("donner la jour x= "))
if x>31 or x<1:
    print("il n'y a pas de jour")
else :
    y= int(input("donner le mois y= "))
    if y>12 or y<1:
        print("il n'y a pas de mois")
    else:
        z= int(input("donner le year z= "))
        if z>date.today().year:
            print("avion invalede")
        else:
           print("la date de lessences",naisssonce(x,y,z))




