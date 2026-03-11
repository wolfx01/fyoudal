
l = [14,10,13,12,11]
print(l)
n = len(l)
temp = l[0]
for i in range(0,n-1):
    l[i] = l[i+1]
l[n-1] = temp
print(l[:])