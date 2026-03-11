dec ={}
print(dec)

d = {
    "name" : "chouichou",
    "prenom" : "bilal",
    "age" :20 ,
}
print(d["name"])
print(d["prenom"])
print(d["age"])




print(d)
for v in d.values():
    print(v,end=" ")
for k in d.keys():
    print(k,end=" ")



g= len(d)
print(g)

del d["prenom"]
print(d)


d1 = {
    "name":"dahbi",
    "prenom":"bilal",
    "age":20,
    "filier":  "dd101"
}


d.update(d1)
print(d)
print(d1)


d= d1.copy()
print(d)
print(d1)



l= []
l=list(d.values())
print(l)




l=[]
for v in d.values():
    l.append(v)
print(l)









