"""#szám osztóinak meghatározása eljárással:
def osztoi(szam):
    i=1
    while i<=szam:
        if szam%i==0:
            print(i)
        i+=1
osztoi(50)

#függvénnyel:
def osztok(szam):
    l=[]
    i=1
    while i<=szam:
        if szam%i==0:
            l.append(i)
        i+=1
    return l #lista az adott érték

print(osztok(50))

def osszeg(a,b):
    return(a+b)
print(osszeg(7,3))
    
#eljárással írd ki a páros számokat
def osztok(szam):
    i=1
    while i<=szam:
        if i%2==0:
            print(i)
        i+=1
osztok(int(input("Adj meg egy számot:")))


#adott számig írd ki a páros számokat függvénnyel
def osztok(szam):
    l=[]
    i=1
    while i<=szam:
        if i%2==0:
            l.append(i)
        i+=1
    return len(l)

print(osztok(int(input("Adj meg egy számot:"))))



#feladatsor
def leghosszabb_szo(s): #ma nem eszek almát
    if s=="":
        return "HIBA"
    else:    
        l=s.split()
        max=len(l[0])
        maxi=0
        for i in range(len(l)):
            if max<len(l(i)):
                max=len(l[i])
                maxi=i
            return l[maxi]
print(leghosszabb_szo(input("Kérek egy mondatot: ")))
#hibas

def gyenge_jelszo(lista): #lista=["fgb", "jelszocska", "kugya233", "iXde123" ,"faIIIIsjodasji321"]

    gyenge=[]
    for i in lista:
        if len(i)<5:
            gyenge.append(i)
            print("Gyenge a jelszó!")
        elif i.isalpha():
            gyenge.append(i)
            print("Gyenge a jelszó!")
        elif "jelszo" in i or "123" in i:
            gyenge.append(i)
            print("Gyenge a jelszó!")
    return gyenge
lista=["fgb", "jelszocska", "kugya233", "iXde123" ,"faIIIIsjodasji321", "jelszo" , "123"]
print(gyenge_jelszo(lista))

def egyedi_szavak_szama(s): #ma nem eszunk kaposztat mert a kecske a kaposztat meg kaposztazta
    s=s.lower #egész szöveg kisbetű
    s=s.strip(".").strip(",")#s=s.replace(".", ",").replace
    l=s.split()
    halmaz=set(l)
    return len(halmaz)
print(egyedi_szavak_szama("ma nem eszunk kaposztat mert a kecske a kaposztat meg kaposztazta"))"""

def felvaltva(s):
    if s<len(len[0]):
        l=s.split=()
        if len(l)<2:
            return "HIBA"
        else:
            for i in range(len(l)):
                if i%2==0:
                    l[i]=l[i].lower()

return l   #nem jó

#hf a feladatsor, doga lesz
            
        


