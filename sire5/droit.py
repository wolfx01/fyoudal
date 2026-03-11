
l = [14,10,13,12,11]
print(l)
n = len(l)
temp = l[n-1]
for i in range(n-2,-1,-1):
   l[i+1] = l[i]
l[0] = temp
print(l[:])