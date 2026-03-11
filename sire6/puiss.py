import math


def puiss(a,b):

    p = int(math.pow(a,b))
    return p



x= int(input("donner x= "))
n = int(input("donner n= "))
print(x," a la puissonce ", n , "=",puiss(x,n))

