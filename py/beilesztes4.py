class verseny():
    def __init__(self,s):
        sor=s.split("\t")
        self.nev=sor[0]
        self.datum=sor[1]
        self.nemzet=sor[2]
        self.rajtszam=int(sor[3])

lista=[]

with open("versenyzok.txt", "r", encoding="UTF-8") as f:
    f.readline()
    for i in f:
        lista.append(verseny(i.strip()))

#Hány versenyző van?
print(len(lista))
#Hány német versenyző van?
db1=0
for i in lista:
    if i.nemzet=="cigany":
        db1+=1
print(db1)
#Milyen nemzetiségű versenyzők vannak a fájlban?
nemzet=[]
for i in lista:
    if i.nemzet in nemzet:
        continue
    else:
        nemzet.append(i.nemzet)
print(nemzet)
#Nemzetiség szerint hány versenyző indult?
nemzetek=[]
for i in lista:
    nemzetek.append(i.nemzet)
print(set(nemzetek))
#Írjuk ki nevsor.txt fájlba névsorban a neveket és a rajtszámokat!
#Ki indul az első helyről?
#Kinek ven a legrövidebb neve?
#Kérj be egy versenyző nevét!
	#Szerepel-e a versenyzők között vagy sem?
	#Kinek a neve hosszabb az általad megadott névnél?
	#Kinek a neve kezdődik az általad megadott név 	 kezdőbetűjével?


#Házi feladat nóbel.txt
