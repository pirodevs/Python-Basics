#  ____  _             
# |  _ \(_)_ __ ___    
# | |_) | | '__/ _ \  
# |  __/| | | | (_) | 
# |_|   |_|_|  \___/

# when run, it prints what is inside the parentheses
# needed for text/letters -> ""; not for numbers
# for text, except when there is already a variable, e.g. nev = Bela (the variable name does not need quotes)
print(10)

# -------------------------------------

nev = "Peti"
kor = 15
print(kor)
print(nev)
# a more advanced version:

print("A nevem:", nev)
print("Életkorom:", kor)

# -------------------------------------
# conversation

nev1 = input("Mi a neved? ")
print("Szia", nev1)

# -------------------------------------
# számos conversation
# input=integer, float=decimal

kor1 = int(input("How old are you? "))
print("Az igen!")

magassag = float(input("Hány centi magas vagy? "))
print("Az nem semmi!")

# -------------------------------------
# operations

a = 10
b = 3

print(a + b)  # addition
print(a - b)  # subtraction
print(a * b)  # multiplication
print(a / b)  # division

# -------------------------------------
# rectangle

a = float(input("Enter side a: "))
b = float(input("Enter side b: "))

area = a * b
perimeter = 2 * (a + b)

print("A rectangle területe:", area)
print("A rectangle kerülete:", perimeter)

# -------------------------------------
# circle

import math

r = float(input("Add meg a circle sugarát: "))

area = math.pi * r ** 2
perimeter = 2 * math.pi * r

print("A circle területe:", area)
print("A circle kerülete:", perimeter)

# -------------------------------------
# comparison (if, else)

kor = int(input("How old are you? "))

if kor >= 18:
    print("You are an adult.")
else:
    print("You are not an adult yet.")
    

# -------------------------------------
# elif 2+ options

jegy = int(input("What grade did you get on the test? "))

if jegy == 5:
    print("Excellent")
elif jegy == 4:
    print("Good")
elif jegy == 3:
    print("Average")
elif jegy == 2:
    print("Pass")
else:
    print("Fail")
      
# important commands:

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