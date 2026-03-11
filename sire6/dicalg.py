

l=[14,12,10,13,11]
n= len(l)


def affich(l):
    print(l[:])


def decalg(l):
    temp = l[0]
    for i in range(n-1):
        l[i] = l[i+1]
    l[n-1] = temp



affich(l)
decalg(l)
affich(l)



