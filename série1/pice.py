a = int(input("donner la argeut a : "))
b200 = a // 200
r1 = a % 200
b100 = r1 // 100
r2 = r1 % 100
b50 = r2 // 50
r3 = r2 % 50
b20 = r3 // 20
r4 = r3 % 20
p10 = r4 // 10
r5 = r4 % 10
p5 = r5 // 5
r6 = r5 % 5
p2 = r6 // 2
r7 = r6 % 2
p1 = r7

print(a,"===> : ")
print( "billet 200 ==>" , b200)
print("  /billet 100 ==> " , b100 )
print("/billet 50 : " , b50)
print("  /billet 20 : " , b20)
print("/piece 10 : " , p10)
print("/piece 5 : " , p5)
print("/piece 2 : " , p2)
print("/piece 1 : " , p1)