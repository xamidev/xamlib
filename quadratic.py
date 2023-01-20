from math import sqrt
from clint.textui import colored

def derivative(): #tbd
    pass

def resolve(delta, a, b, c):
    if delta>0:
        x1=(-b-sqrt(delta))/2*a
        x2=(-b+sqrt(delta))/2*a
        print(f"Equation has two solutions | x1={colored.cyan(x1)} x2={colored.cyan(x2)} | delta={colored.green(delta)}")
    elif delta==0:
        x=-b/2*a
        print(f"Equation has one solution | x={colored.cyan(x)} | delta={colored.green(delta)}")
    else:
        print(f"Equation has no solution | delta={colored.green(delta)}")
        #tbd

def delta(a, b, c):
    return b**2-4*a*c

def userInput():
    a=float(input("a: "))
    b=float(input("b: "))
    c=float(input("c: "))
    resolve(delta(a,b,c), a, b, c)

userInput()