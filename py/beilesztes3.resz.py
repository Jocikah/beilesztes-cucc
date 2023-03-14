f=open("kutya.txt" ,"r", encoding="UTF-8")
lista=[]

for i in f:
    lista.append(i)
#print(lista)

#Hány sorból áll a txt?
print(len(lista))

#Melyik a leghosszabb név?
max_hossz=len(lista[0])
maxi=0

for i in range(len(lista)):
    if len(lista[i])>max_hossz:
        max_hossz=len(lista[i])
        maxi=i
print(lista[maxi])

#írjunk függvényt, hogy a bekért név szerepel-e a nevek közt
def benne(l,n):
    if n in l:
        return True
nev=input("Adj megy egy nevet:")
if benne(lista,nev)==True:
    print("Szerepel")
else:
    print("Nem szerepel")

#írjuk ki "nevek_i.txt" fájlba az i-re végződő neveket. KÖVI DOGA!!!
ki=open("evek_i.txt", "w", encoding="UTF-8")
for elem in lista:
    if elem.endswith("i"):
        ki.write(elem)
ki.close()

#Hány olyan név van, amely 5 karakter hosszú?
db=0
def kar():
    for i in lista:
        if len(i)==5:
            db+=1

print(db)