n = int(input("Enter n number: "))
for i in range(n,0, -1):
    print(" " * (n - i) + "*" * i)