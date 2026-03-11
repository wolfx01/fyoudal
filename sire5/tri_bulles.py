l = [14,10,13,12,11]
n= len(l)
for i in range(0,n):
    for j in range(i+1,n):
        if l[i] > l[j]:
            temp = l[i]
            l[i] = l[j]
            l[j] = temp
print(l[:])

