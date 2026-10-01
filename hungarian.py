#  ____  _             
# |  _ \(_)_ __ ___    
# | |_) | | '__/ _ \  
# |  __/| | | | (_) | 
# |_|   |_|_|  \___/

# futtatáskor kiirja ami a zárójelben van
# betűknél kell -> "" számoknál nem
# betűknél kivéve akkor ha van már pl: nev = Bela (a nev hez nem kell)
print(10)

# -------------------------------------

nev = "Peti"
kor = 15
print(kor)
print(nev)
# fokozva ez:

print("A nevem:", nev)
print("Életkorom:", kor)

# -------------------------------------
# beszélgetés

nev1 = input("Mi a neved? ")
print("Szia", nev1)

# -------------------------------------
# számos beszélgetés
# input=egész szám, float=tizedes

kor1 = int(input("Hány éves vagy? "))
print("Az igen!")

magassag = float(input("Hány centi magas vagy? "))
print("Az nem semmi!")

# -------------------------------------
# műveletek

a = 10
b = 3

print(a + b)  # összeadás
print(a - b)  # kivonás
print(a * b)  # szorzás
print(a / b)  # osztás

# -------------------------------------
# téglalap

a = float(input("Add meg az a oldalt: "))
b = float(input("Add meg a b oldalt: "))

terulet = a * b
kerulet = 2 * (a + b)

print("A téglalap területe:", terulet)
print("A téglalap kerülete:", kerulet)

# -------------------------------------
# kör

import math

r = float(input("Add meg a kör sugarát: "))

terulet = math.pi * r ** 2
kerulet = 2 * math.pi * r

print("A kör területe:", terulet)
print("A kör kerülete:", kerulet)

# -------------------------------------
# összehasonlítás (if, else)

kor = int(input("Hány éves vagy? "))

if kor >= 18:
    print("Nagykorú vagy.")
else:
    print("Még nem vagy nagykorú.")
    

# -------------------------------------
# elif 2+ lehetőség

jegy = int(input("Hányas lett a dolgozat? "))

if jegy == 5:
    print("Jeles")
elif jegy == 4:
    print("Jó")
elif jegy == 3:
    print("Közepes")
elif jegy == 2:
    print("Elégséges")
else:
    print("Elégtelen")
      
# fontos parancsok:

# if
# elif 
# else
# str
# import  
# and
# or
# not
# print()
# input()
# int()
# float()
###########
# +
# -
# *
# /
# **
# ==
# >
# <
# >=
# <=

#  ____  _             
# |  _ \(_)_ __ ___    
# | |_) | | '__/ _ \  
# |  __/| | | | (_) | 
# |_|   |_|_|  \___/