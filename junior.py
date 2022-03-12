
from ast import Num
from dataclasses import replace
from random import random
from tkinter import N


A = 20
B = ("I am {} years old")
print(B.format(A))

animal = ["dog","cat","monkey"]
animal.append("bird")
print(animal)

I = 10
F = 4.0
S = "Hello"
B = 5 < 10
print(type(I))
print(type(F))
print(type(S))
print(type(B))

for x in range(1,10):
    print(x)

Number = "one"
print(Number.replace("one","two"))
print(Number.upper())
print(Number.lower())

if 2==0:
    print("Yes")
else:
    print("No")

color = ["red","blue","yellow"]
fruit = ["mango","banana","orange"]
for C in color:
    for P in fruit:
        print(C,P)  

"""
Ex_one = int(input())
Ex_two = int(input())
Ex = Ex_one + Ex_two
print(" = ",Ex)
"""

for o in range(0,50,5):
    print(o)

for x in range(10):
    if x == 5: continue
    print(x) 
else:
    print("finished!!")

for F in range(20):
    print("#"*(F+1))


     

