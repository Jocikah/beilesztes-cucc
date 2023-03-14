"""
szam=int(input("Gondolj egy számra"))

import random
veltipp=random.randint(0,100)
lepes=0
talalt=False

while talalt==False:
    if szam==veltipp:
        lepes=+1
        print(f"{lepes}-ből kitaláltad")
        talalt=True
    elif szam>veltipp:
        lepes=+1
        veltipp=random.randint(1,szam)
    elif szam<veltipp:
        lepes=+1
        veltipp=random.randint(szam,100)
    else:
        print("Nem jött össze")""" #ez nem jo

#1. feladat
"""
a=int(input("add meg az első számot"))
b=int(input("add meg a második számot"))

print(f"A megoldás{a+b*2}")"""

#2. feladat
"""szam=int(input("adj meg egy számot:"))
darab=0
while szam!=0:
    if szam>5:
        darab+=1
    szam=int(input("add meg a számot:"))
print(f"kiléptem a ciklusból:{darab}")"""

#3. feladat
"""homers=int(input("add meg a hőmérsékletet"))
osszeg=0
darab=0

while homers>0:
    darab+=1
    osszeg+=homers
    homers=int(input("adj meg mégegy hőmérsékletet"))
atlag=round(osszeg/darab,1)
print(f"{atlag}")"""

#4. feladat
"""szam=int(input("adj meg egy fokot"))
darab=0

while szam>-5:
    if szam>10:
       darab+=1
    szam=int(input("adj meg még egy fokot"))
print(f"ennyiszer volt a hőmérséklet 10 foknál nagyobb: {darab}")"""

#5. feladat
"""szam=int(input("adj meg egy számot"))"""


#10.feladat

"""n=int(input("Sorok száma: "))
m=int(input("Oszlopok száma: "))
i=0
while i<=n:
    j=0
    while j<=m:
        print("*", end="\t")
        j+=1
    print("")
    i+=1"""

"""n=int(input("asd"))
m=int(input("asd"))
i=0
while i<11:
    j=1
    while j<11:
        print(i*j, end="\t")
        j+=1
    print("")
    i+=1"""




