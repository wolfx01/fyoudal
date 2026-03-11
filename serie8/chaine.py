ch = str(input("donner une chaine : "))
print(ch.upper())
print(ch.lower())
print(ch.capitalize())
l= len(ch)
print(l)


for i in range(65,91):
    print(chr(i),end=" ")
print()
for i in range(97,123):
    print(chr(i),end=" ")



b = str(input("donner une chaine : "))
k=""
for i in b:
    k=i+k
print(k)
if k == b :
    print("copy")
else:
    print("no copy")







m = str(input("donner une chaine : ")).lower()
c= 0
for j in m:
    if j =="a" or j=="e" or j=="u" or j=="y":
        c +=1
print(c)
