def fact(n):
    f= 1
    for i in range(1,n+1):
        f= f*i
    return f


x= int(input("donner x : "))
print("la fact est ",fact(x))
