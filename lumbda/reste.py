reste = lambda x,y:x%y
a= int(input("donner a= "))
b= int(input("donner b= "))
if b == 0:
   print("impossible")
else:
    print("le reste est ", reste(a,b))

