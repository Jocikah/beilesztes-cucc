


"""x=(int(input("Add meg a végösszeget")))
if x<10000:
    print("Nincs kedvezmény a termékre")
elif x<=20000:
    print("2% kedvezmény jár a termékre így az ára:"(x*0,98))
elif x>20000:
    print("5% kedvezmény jár a termékre így az ára:"(x*0,95))
else:
    print("Rossz összeget adott meg")"""


"""y=int(input("Add meg az életkort"))
if y<=14:
    print("Gyermek")
elif y>14 and y<18:
    print("Fiatal")
else:
    print("Felnőtt")"""

"""c=(int(input("Add meg a dolgozat százalékát")))
if c>85:
    print("5")
elif c>70:
    print("4")
elif c>55:
    print("3")
elif c>40:
    print("2")
else:
    print("1")"""



"""a=(int(input("Add meg az A oldal hosszát")))
b=(int(input("Add meg a B oldal hosszát")))
c=(int(input("Add meg a c oldal hosszát")))
if a+b>c and b+c>a and c+a>b:
    if a==b and b==c:
        print("A háromszög szabályos")

    elif a==b or b==c or a==c:
        print("A háromszög egyenlőszárú")

    elif a**2+b**2==c**2:
        print("Derékszögű a háromszög")
    else:
        ("a háromszög szerkeszthető")

else:
    print("Nem szerkeszthető a háromszög")"""


a=(int(input("Milyen síkidom területét és kerületét szeretnéd kiszámolni? 1.Kör, 2.Négyzet, 3.Téglalap")))
if a==1:
    r=int(input("Adj egy sugár értéket"))
    pi=3.14
    print(f"A kör kerülete: {2*r*pi:.1f}m területe: {r**2**pi:.1f}m2")
elif a==2:
    b=int(input("Add meg az A oldalt"))
    print(f"A négyzet kerülete {b*4} és területe {b*b}")

elif a==3:
    c=int(input("Add meg az A oldalt"))
    d=int(input("Add meg a B oldalt"))
    print(f"A téglalap kerülete: {(c*d)*2}m területe: {c*d}m2")
