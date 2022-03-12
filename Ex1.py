print("Hello world")

for i in range(5):
    print("*"*(i+1))

A = ["apple","banana","orange"]
A.append("mango")
print(A)

B = {"red","blue","green"}
B.add("yellow")
print(B)


Q = 10
W = 20
if Q > W:
    print("yes")
else:
    print("No")

def about_love():
    Me = ("i love {}")
    print(Me.format("you"))
about_love()

def Test_function():
    A = ("My name is")
    print((A) + " " + ("peter"))
Test_function()

def Name(Fname,Lname):
    print(Fname + " " + Lname)
Name("peter","parker")

def ques(country = "thailand"):
    A = ("\nwhere are you from\n")
    print(A + ("I'm from ") + country)
ques()
ques("Japan")




