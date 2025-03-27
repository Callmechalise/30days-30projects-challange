
from functools import lru_cache
import math,numpy as np
import cmath
import time

from sympy import symbols,Eq,solve
from z3 import Int,Solver,sat

@lru_cache(maxsize=1000)
def quadratic():
    running=True
    while running:
        print("Enter a,b,c \"ax^2+bx+c\"")
        a=int(input("a:\n"))
        b=int(input("b:\n"))
        c=int(input("c:\n"))
        d=(b**2-4*a*c)
        if d<0:
            d=cmath.sqrt(d)
            print("Imaginary roots\n")
            x=(-b+d)/2*a
            print(f"x1={x}\n")
            x=(-b-d)/2*a
            print(f"x2={x}")
            running=False
        elif d>0:
            d=math.sqrt(d)
            print("Real roots\n")
            x=(-b+d)/2*a
            print(f"x1={x}\n")
            x=(-b-d)/2*a
            print(f"x2={x}")
            running = False
        elif d==0:
            d = math.sqrt(d)
            print("Real and equal roots\n")
            x = (-b + d) / 2 * a
            print(f"x={x}\n")
            running = False
@lru_cache(maxsize=1000)
def degree3():
    print("Enter a,b,c,d \"ax^3+bx^2+cx+d\"")
    a = int(input("a:\n"))
    b = int(input("b:\n"))
    c = int(input("c:\n"))
    d = int(input("d:\n"))
    coeff=[a,b,c,d]
    roots=np.roots(coeff)
    x=0
    for i in roots:
        print(f"x{x}:",round(i))
        x=x+1
@lru_cache(maxsize=1000)
def simple():
    x=symbols("x")
    print("Enter linear equation eg:(3*x+2=8):\n")
    s=input()
    lhs,rhs=s.split("=")
    eqn=Eq(eval(lhs),eval(rhs))
    solution=solve(eqn,x)
    for i in solution:
        print(f"X:{i}\n")
@lru_cache(maxsize=1000)
def simultaneous():
    x=Int("x")
    y=Int("y")

    eqn1=input("Enter first equation:\n")
    eqn2=input("Enter second equation:\n")
    eqn1=eqn1.replace("=","==")
    eqn2=eqn2.replace("=", "==")
    solver=Solver()
    solver.add(eval(eqn1, {"x": x, "y": y}))
    solver.add(eval(eqn2, {"x": x, "y": y}))
    if solver.check()==sat:
        model=solver.model()
        print(f"X:{model[x]}")
        print(f"Y:{model[y]}")

def menu():
    while True:
        print("Enter Operation:\n")
        print("1:quadratic eqn\n")
        print("2:simple\n")
        print("3:Third Degree\n")
        print("4:simultaneous\n")
        x=int(input())
        if x==1:
            quadratic()
            time.sleep(2)
        elif x==2:
            simple()
            time.sleep(2)
        elif x==3:
            degree3()
            time.sleep(2)
        elif x==4:
            simultaneous()
            time.sleep(2)
        else:
            print("Invalid input")
            time.sleep(2)
menu()