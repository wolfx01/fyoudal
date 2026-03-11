a  = int(input("donner  la value a : "))
b = int(input("donner  la value b: "))
if a == 0 and b == 0 :
    print("infinete")
elif a == 0 and b != 0 :
    print("imposible")
else :
    x = -b/a
    print(x)