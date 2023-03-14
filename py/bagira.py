#1 tölts fel egy 10 elemű listát 1-1000 véletlenszerű számokkal
import random
"""lista=[]
for i in range (10):
    lista.append(random.randint(1,1000))
lista.insert(4,50)
print(lista)
#Hanyadik helyen helyezkedik el?
print(lista.index(50))

#hány darab xy szám van a listában?
print(lista.count(50))

#Töröld ki az 50 es eleme
del lista(4)
#
lista=[1,2,3,4,5,6,7,8,9,10,11]
print(lista[:-1])"""

#szedjen ki bizonyos számokat
"""for i in range (10):
    lista.append(random.randint(1,1000))
print(lista)
print(lista[1:8:2])
print(lista[-3:-7:-1])"""

#számítsd ki az elemek összegét, a /len az az átlag
"""lista=[1,2,3,4,5,6,7,8,9,10,11]
print(sum(lista)/len(lista))

#számold meg hogy hány kétjegyú szám van a listában
lista=[]
db=0
for i in range (10):
    lista.append(random.randint(9,100))

print(lista)
for i in lista:
    if i>9 and i<100:
        db+=1
print(db)
print(len([x for x in lista if x>9 and x<100]))

#irasd ki az egyjegyű számok négyzetét
print([x**2 for x in lista if x<10])

#
print(sum([x for x in lista if x%3==0]))

print(len([x for x in lista if x%10==0]))

print(sum([x for x in lista if x%5==0]))

print(len([x for x in lista if x>500]))

print(sum([x for x in lista if x<10]))

#print(([]))-nél oda lehet írni a "sorted"-et is
print(([x for x in lista if x>9 and x<100]))
lista.sort()
print(lista)

print(sorted([x for x in lista if x%3==0][::-1]))"""



