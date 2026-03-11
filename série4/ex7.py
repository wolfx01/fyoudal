n=int(input("donner n="))
t = 0
for i in range (1,n+1):
    if i % 2 == 0:
        t = t + i
    else:
        t = t - i
print("la valeur de t est :", t )