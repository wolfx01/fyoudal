t = int(input("donner la total t  : "))
h = t // 3600
r1 = t % 3600
m = r1 // 60
r2 = r1 % 60
s = r2
print(t , "secoudes contient :" , h , "heurs " , m , "munite" , s , "seconde")