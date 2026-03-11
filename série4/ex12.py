n = int(input("donner  n  =  "))
s = 0
for i in range(1, n):
    if s % i == 0:
        s = s + 1

if s == 1:
    print(n, "est  parfait ")
else:
    print(n, "est pas parfait ")
