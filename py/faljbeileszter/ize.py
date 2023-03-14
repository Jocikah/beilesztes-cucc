"""
lista=[]
s=open('gyumi.txt',"r",encoding="UTF-8")
ki=open("Csillag.txt","w",encoding="UTF-8")

for sor in s:
    lista.append(sor.strip())
s.close()
print(lista)
"""
"""
lista=s.readlines()
uj=[]
for i in lista:
    uj.append(i.strip())
print(uj)
"""
"""
dbE=0
dbe=0
while True:
    betu=s.read(1)
    if betu:
        if betu=="E" or betu=="e":
            ki.write("*")
            if betu=="E":
                dbE+=1
            elif betu=="e":
                dbe+=1
        else:
            ki.write(betu)
    else:
        break
s.close()
ki.close()
print(f"E-betük száma: {dbE},e-betük száma: {dbe}")

class Csoport():
    def __init__(self,s):
        sor=s.split(";")
        self.nev=sor[0]
        self.mag=int(sor[1])
lista=[]
with open("Csoport.txt","r", encoding="UTF-8") as f:
    for i in f:
        lista.append(Csoport(i.strip()))
f.close()

for i in lista:
    print(f"{i.nev} - {i.mag}")

osszeg=0
for i in lista:
    osszeg += i.mag
atlag=round(osszeg/len(lista),2)
print(atlag)

max_magassag=lista[0].mag
maxi=0
for index in range(len(lista)):
    if lista[index].mag>max_magassag:
        max_magassag=lista[index].mag
        maxi=index
print(f"Legmagasabb ember: {lista[maxi].nev}, magassága: {lista[maxi].mag}")"""

class eu():
    def __init__(self,s):
        sor=s.split(";")
        self.o=sor[0]
        self.d=sor[1]
lista=[]
with open("eu.txt","r",encoding="UTF-8") as f:
        for i in f:
             lista.append(eu(i.strip()))
f.close()

for i in lista:
     if "ország" in i.orsz:
          print(i.orsz)

van=False
if "Magyarország" in i.orsz:
    van=True
if van==True:
    print("Van benne magyarorszag")
else:
     print("nincs benne mo")
    

class forrasfajl():
    def __init__(self,s):
         sor=s.split(";")
         self.ev=sor[0]
         self.nyelv=sor[1]
         self.nev1=sor[2]
         self.nev2=sor[3]