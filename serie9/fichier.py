f=open("data.txt" , "w")
ch="je suis en DD 101\n"
f.write(ch)
f.close()


f= open("data.txt","a")
v= "nous sommes a le fin  module m101"
f.write(v)
f.close()

d= {"title": "\talgorithme\t", "ordre":"M102\t","maassehairer": "100dh"

}
l = list(d.values())


print(l[:])
f= open("data.txt","a")
for i in l:
    f.write(str(i))


f.close()

