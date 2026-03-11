from datetime import date
age = lambda an : date.today().year - an
x=int(input("donner x= "))
print("lage est ",age(a),"ans")