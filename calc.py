adfasdf = input("how many thingys")
asd = int(adfasdf)
poo = []
while asd > 0:
    pee = int(input("enter number"))
    poo.append(pee)
    asd -=1
sumx=difx=quox=prodx=0
for x in poo:
    sumx += x
    difx -= x
    quox /= x
    prodx *= x
    
print("The sum is: " + sumx + '\n' + "The difference is: " + difx + '\n' + "The product is: " + prodx + '\n' + "The quotient is: " + quox)
