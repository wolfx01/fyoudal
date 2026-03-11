espace = lambda n : n*" "
etoile = lambda n : n*"*"
a = int(input("Enter a number: "))
for i in range(1,a+1 ):
    print( espace(a-i) , etoile(i))



