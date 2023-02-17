import cmath
a=int(input("enter a:"))
b=int(input("enter b:"))
c=int(input("enter c:"))
d=(b**b)-(4*a*c)
sol1=(-b+cmath.sqrt(d))/(2*a)
sol2=(-b-cmath.sqrt(d))/(2*a)
print("solutions are :",sol1,sol2)
