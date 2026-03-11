a = int(input("nombre de a"))
if  a%4==0 and a%100 !=0 or a%400==0:
    print("lanner", a , "est bissentile")
else:
    print("lanner", a , "est simple")