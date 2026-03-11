import statistics

l = [12,14,10,13,11]

n = len(l)
print(n)
print("\n\n")



for i in range(0, len(l)):
    print(l[i])


print("\n\n")
print("\n\n")

print(l[:])
print("\n\n")
print(l[2])
print("\n\n")
print(l[:2])
print("\n\n")
print(l[3:])
print("\n\n")
print(l[-3])
print("\n\n")
print(l[1:3])
print("\n\n")
l[3]=15
print("\n\n")
print(l[:])
print("\n\n")
l.append(17)
print("\n\n")
print(l[:])
print("\n\n")
""" supprime element 15"""
l.remove(15)
print("\n\n")
print(l[:])
print("\n\n")
del l[3]
print("\n\n")
print(l[:])
print("\n\n")
l.sort()
print("\n\n")
l.reverse()
print("\n\n")
print(l[:])
print("\n\n")
s= sum(l)
print("\n\n")
print(l[:])
print("\n\n")
print(l[:])
print("\n\n")
s = 0
for i in range(0,len(l)):
    s = s + l[i]
print(s)
print("\n\n")
m = statistics.mean(l)
print("\n\n")
print(m)
print("\n\n")
g = max(l)
print("\n\n")
print(g)
print("\n\n")
k= min(l)
print("\n\n")
print(k)
print("\n\n")
pos = l.index(g)
print("\n\n")
print(pos)
print("\n\n")


