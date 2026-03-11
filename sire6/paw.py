import math

def puissonce(a ,b):
    p = math.pow(a,b)
    return round(p)



x = int(input("donner x : "))
n = int(input("donner n : "))
print("la puissonce de ",x,"et",n," est",puissonce(x,n))
