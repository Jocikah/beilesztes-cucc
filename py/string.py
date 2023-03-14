"""mondat=input("Amerre én járok arra bámul a világ-")
print(mondat.count(" ")+1)
print(len(mondat))
mgh=["a","á","e","é","i","í","o","ó","ö","ő","u","ú","ü","ű"]
db=0
for i in mondat:
    if i in mgh:
        db+1
print(db)

mennyiszer=int(input("hányszor:"))
print((mondat+" ")*mennyiszer)"""
mondat=input("adj meg egy mondatot")
szo=input("Szó:")
ind=mondat.index("")

elso=mondat[:ind+1]=szo
masod=mondat[ind:]
print(elso+masod)

